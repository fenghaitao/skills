#!/usr/bin/env python3
"""
Session log parser for ADK apply_agent sessions.

Provides tools to extract structured information from session.txt files:
- File reading sequence validation
- Tool usage analysis
- Error pattern extraction
- Build/test attempt tracking
"""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple


@dataclass
class ToolCall:
  """Represents a single tool invocation."""
  timestamp: str
  tool_name: str
  args: str
  result_type: Optional[str] = None  # 'success' or 'error'
  result_summary: Optional[str] = None


@dataclass
class SessionMetrics:
  """High-level session metrics."""
  duration_seconds: float
  total_events: int
  tool_calls: int
  build_attempts: int
  test_runs: int
  errors: int


def parse_session_header(session_path: str) -> Dict[str, str]:
  """Extract session metadata from header."""
  with open(session_path, 'r', encoding='utf-8') as f:
    header = f.read(2000)
  
  metadata = {}
  patterns = {
    'session_id': r'Session ID: ([a-f0-9-]+)',
    'user_id': r'User ID: (\S+)',
    'last_update': r'Last Update: (.+)',
    'total_events': r'Events: (\d+) total'
  }
  
  for key, pattern in patterns.items():
    match = re.search(pattern, header)
    if match:
      metadata[key] = match.group(1)
  
  return metadata


def extract_tool_calls(session_path: str) -> List[ToolCall]:
  """Extract all tool calls with timestamps and results."""
  tool_calls = []
  
  with open(session_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  
  i = 0
  while i < len(lines):
    line = lines[i]
    
    if '🔧' in line:
      timestamp_match = re.search(
        r'\[apply_agent\] ([\d-]+ [\d:]+ UTC)',
        lines[i-1] if i > 0 else ''
      )
      timestamp = timestamp_match.group(1) if timestamp_match else 'unknown'
      
      tool_match = re.search(r'🔧 (\w+)\((.*?)\)', line)
      if tool_match:
        tool_name = tool_match.group(1)
        args = tool_match.group(2)
        
        result_type = None
        result_summary = None
        for j in range(i+1, min(i+10, len(lines))):
          if '📤' in lines[j]:
            result_type = 'success'
            result_summary = lines[j].split('→')[1].strip() if '→' in lines[j] else ''
            break
          elif '❌' in lines[j]:
            result_type = 'error'
            result_summary = lines[j].split('→')[1].strip() if '→' in lines[j] else ''
            break
        
        tool_calls.append(ToolCall(
          timestamp=timestamp,
          tool_name=tool_name,
          args=args,
          result_type=result_type,
          result_summary=result_summary
        ))
    
    i += 1
  
  return tool_calls


def validate_file_reading_sequence(tool_calls: List[ToolCall]) -> Dict:
  """Check if agent followed required file reading protocol."""
  read_files = [tc for tc in tool_calls if tc.tool_name == 'read_file']
  
  violations = []
  compliance = {
    'read_agents_md_first': False,
    'read_memory_indices': False,
    'sequence_correct': True
  }
  
  if not read_files:
    return {
      'compliant': False,
      'violations': ['No files read'],
      'compliance': compliance
    }
  
  first_file = read_files[0].args
  if 'AGENTS.md' in first_file or 'openspec/AGENTS.md' in first_file:
    compliance['read_agents_md_first'] = True
  else:
    violations.append(f"First file should be AGENTS.md, was: {first_file}")
  
  memory_indices_read = []
  for tc in read_files[:5]:
    if '00_DML_Best_Practices_Index.md' in tc.args or \
       '00_Test_Best_Practices_Index.md' in tc.args:
      memory_indices_read.append(tc.args)
  
  if len(memory_indices_read) >= 2:
    compliance['read_memory_indices'] = True
  else:
    violations.append(
      f"Should read both memory indices early, found: {memory_indices_read}"
    )
  
  compliance['sequence_correct'] = len(violations) == 0
  
  return {
    'compliant': compliance['sequence_correct'],
    'violations': violations,
    'compliance': compliance,
    'file_sequence': [tc.args for tc in read_files[:10]]
  }


def extract_build_attempts(session_path: str) -> List[Dict]:
  """Extract all build attempts with outcomes."""
  builds = []
  
  with open(session_path, 'r', encoding='utf-8') as f:
    content = f.read()
  
  build_pattern = r'🔧 build_simics_project\((.*?)\)'
  matches = re.finditer(build_pattern, content)
  
  for match in matches:
    start_pos = match.start()
    context_before = content[max(0, start_pos-200):start_pos]
    timestamp_match = re.search(
      r'\[apply_agent\] ([\d-]+ [\d:]+ UTC)',
      context_before
    )
    timestamp = timestamp_match.group(1) if timestamp_match else 'unknown'
    
    context_after = content[match.end():match.end()+5000]
    
    success = False
    error_messages = []
    
    if '📤 build_simics_project → {\'success\': True' in context_after:
      success = True
    elif '📤 build_simics_project → {\'success\': False' in context_after:
      error_section = context_after.split('📤 build_simics_project')[1]
      error_section = error_section.split('\n\n')[0]
      error_lines = [
        line for line in error_section.split('\\n')
        if 'error:' in line.lower()
      ]
      error_messages = error_lines[:10]
    
    builds.append({
      'timestamp': timestamp,
      'success': success,
      'error_count': len(error_messages),
      'error_messages': error_messages
    })
  
  return builds


def extract_write_operations(tool_calls: List[ToolCall]) -> List[Dict]:
  """Extract all file write/replace operations."""
  write_ops = []
  
  for tc in tool_calls:
    if tc.tool_name in ['write_file', 'replace_string_in_file']:
      file_match = re.search(r'file_path=([^,)]+)', tc.args)
      file_path = file_match.group(1) if file_match else 'unknown'
      
      write_ops.append({
        'timestamp': tc.timestamp,
        'tool': tc.tool_name,
        'file_path': file_path,
        'operation': 'create' if tc.tool_name == 'write_file' else 'modify'
      })
  
  return write_ops


def calculate_session_metrics(
  session_path: str,
  tool_calls: List[ToolCall]
) -> SessionMetrics:
  """Calculate high-level session metrics."""
  metadata = parse_session_header(session_path)
  
  build_attempts = len([
    tc for tc in tool_calls if tc.tool_name == 'build_simics_project'
  ])
  test_runs = len([
    tc for tc in tool_calls if tc.tool_name == 'run_simics_test'
  ])
  errors = len([tc for tc in tool_calls if tc.result_type == 'error'])
  
  timestamps = [tc.timestamp for tc in tool_calls if tc.timestamp != 'unknown']
  duration = 0.0
  if len(timestamps) >= 2:
    try:
      first = datetime.strptime(timestamps[0], '%Y-%m-%d %H:%M:%S UTC')
      last = datetime.strptime(timestamps[-1], '%Y-%m-%d %H:%M:%S UTC')
      duration = (last - first).total_seconds()
    except:
      pass
  
  return SessionMetrics(
    duration_seconds=duration,
    total_events=int(metadata.get('total_events', 0)),
    tool_calls=len(tool_calls),
    build_attempts=build_attempts,
    test_runs=test_runs,
    errors=errors
  )


def analyze_session(session_path: str) -> Dict:
  """Complete session analysis - main entry point."""
  tool_calls = extract_tool_calls(session_path)
  metrics = calculate_session_metrics(session_path, tool_calls)
  file_sequence = validate_file_reading_sequence(tool_calls)
  builds = extract_build_attempts(session_path)
  writes = extract_write_operations(tool_calls)
  
  return {
    'metrics': metrics,
    'file_reading_compliance': file_sequence,
    'build_attempts': builds,
    'write_operations': writes,
    'tool_calls_summary': {
      'total': len(tool_calls),
      'by_tool': _count_by_tool(tool_calls),
      'errors': [tc for tc in tool_calls if tc.result_type == 'error']
    }
  }


def _count_by_tool(tool_calls: List[ToolCall]) -> Dict[str, int]:
  """Helper to count tool calls by tool name."""
  counts = {}
  for tc in tool_calls:
    counts[tc.tool_name] = counts.get(tc.tool_name, 0) + 1
  return counts


if __name__ == '__main__':
  import sys
  import json
  
  if len(sys.argv) < 2:
    print("Usage: python session_parser.py <session.txt>")
    sys.exit(1)
  
  session_file = sys.argv[1]
  analysis = analyze_session(session_file)
  
  print(json.dumps(analysis, indent=2, default=str))
