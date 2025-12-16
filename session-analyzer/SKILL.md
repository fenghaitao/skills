---
name: session-analyzer
description: Analyze ADK apply agent sessions to identify error patterns and generate specific improvements for agent instructions and memory documents.
license: Apache-2.0
metadata:
  version: "2.1"
  source: "ADK OpenSpec Integration"
  compatible_with: ["ADK", "OpenSpec", "Simics"]
---

# Session Analyzer

Analyzes ADK apply agent session logs to systematically improve agent performance. Reads from `adk_openspec_apply_agent/` directory.

## Python Tools Available

Use `scripts/session_parser.py` for efficient session analysis:

```python
from session_analyzer.scripts.session_parser import analyze_session

# Complete analysis
analysis = analyze_session('path/to/session.txt')
# Returns: metrics, file_reading_compliance, build_attempts, write_operations
```

**CLI usage:**
```bash
python scripts/session_parser.py path/to/session.txt
```

**Key functions:**
- `analyze_session(path)` - Complete analysis with all metrics
- `validate_file_reading_sequence(tool_calls)` - Check protocol compliance
- `extract_build_attempts(path)` - All builds with success/failure
- `extract_write_operations(tool_calls)` - Track file modifications

## Quick Start

**Essential prompt:**
```
Read these files in order:
1. adk_openspec_apply_agent/apply_agent_instruction.md
2. Latest .session.txt file in adk_openspec_apply_agent/
3. 2-3 relevant files from openspec-memories/

Then analyze: What are the top 3 error patterns, their root causes, and specific improvements needed?

Create markdown report: {component}_implementation_analysis_{YYYYMMDD}.md
```

**With Python tools:**
```
Use scripts/session_parser.py to analyze the latest session file.
Then provide detailed analysis of top error patterns and recommendations.
```

## What It Does

- **Extracts error patterns** from session logs with frequencies and time impact
- **Identifies instruction gaps** where agent lacked necessary guidance
- **Generates specific improvements** with exact text to add to instruction files
- **Creates memory document content** to fill knowledge gaps
- **Quantifies expected impact** in time savings and error reduction
- **Validates file reading sequence** against required protocol

## Analysis Workflow

### 1. Read Required Files (MANDATORY)
- Agent instructions: `adk_openspec_apply_agent/apply_agent_instruction.md`
- Session log: `adk_openspec_apply_agent/*.session.txt` (use .txt not .json)
- Memory docs: Browse `openspec-memories/` and read 2-3 relevant files

### 2. Extract Key Metrics
```bash
# Use Python tool for structured analysis
python scripts/session_parser.py session.txt

# Or manual extraction
grep "👤 \[user\]" session.txt | head -1  # Start
tail -100 session.txt | grep "🤖" | tail -1  # End
grep -c "build_simics_project" session.txt
grep "error:" session.txt | grep -o "'[A-Z][A-Z0-9_]*'" | sort | uniq -c
```

### 3. Identify Root Causes
For each error pattern:
- What was the agent trying to do?
- Why did it fail? (missing knowledge, wrong pattern, syntax error)
- How long did it take to fix?
- What instruction/memory gap caused this?

### 4. Generate Specific Improvements
Provide EXACT text additions, not generic advice:

**❌ Bad:** "Improve register access documentation"

**✅ Good:** 
```
Add to apply_agent_instruction.md:
"DML Register Access: Use bank.REGISTER at device level, 
REGISTER at bank level, this at register level"
```

## Output Format

### Required Report Structure
```markdown
# {Component} Implementation Analysis ({YYYYMMDD})

## Summary
- Duration: X.X minutes
- Build attempts: X (Y failed)
- Final status: Build ✅/❌ | Tests ✅/❌
- File reading compliance: ✅/❌

## Top Error Patterns
### 1. {Error Type} (X occurrences, Y minutes wasted)
- Root cause: [Why it happened]
- Fix applied: [What worked]
- Instruction gap: [What agent should have known]

## Recommendations
### 1. Add to apply_agent_instruction.md:
```
[EXACT TEXT TO ADD]
```
Expected impact: [Quantified improvement]

### 2. Update/Create openspec-memories/{filename}.md:
[Content outline with examples - specify if updating existing or creating new]
Expected impact: [Quantified improvement]

## Expected Impact
- Build attempts: X → Y (Z% reduction)
- Time to completion: X min → Y min (Z% faster)
- {Error type} errors: X → 0 (100% reduction)
```

## Common Use Cases

### Post-Implementation Review
```
Analyze the latest .session.txt in adk_openspec_apply_agent/.
Focus on top 3 error patterns by time impact.
Provide specific instruction file updates.
Create analysis report.
```

### Pattern Discovery (Multiple Sessions)
```
Analyze all .session.txt files from this week.
Identify errors appearing 3+ times across sessions.
Recommend systemic improvements.
```

### Before/After Comparison
```
Compare these sessions:
- BEFORE: apply_implement-wdt_20251214.session.txt
- AFTER: apply_implement-uart_20251215.session.txt

Did the improvements work? What metrics changed?
```

## Critical Error Counting

**⚠️ Common mistake:** Counting error lines instead of actual errors.

One build failure may contain multiple errors:
```
error: unknown identifier: 'WDOGLOAD'
error: unknown identifier: 'WDOGPERIPHID0'
error: unknown identifier: 'WDOGPERIPHID1'
```
This is **3 errors**, not 1.

Extract actual identifiers:
```bash
grep "unknown identifier" session.txt | grep -o "'[A-Z][A-Z0-9_]*'" | wc -l
```

## Quality Checklist

Before submitting analysis:
- [ ] Read actual session file (not guessing)
- [ ] Extracted specific error messages with counts
- [ ] Identified root cause for each major pattern
- [ ] Provided EXACT text for instruction updates
- [ ] Calculated quantified before/after metrics
- [ ] Focused on patterns (3+ occurrences)
- [ ] Created markdown report file
- [ ] Validated file reading sequence compliance

## Tips

1. **Use Python tools** - Faster and more accurate than manual parsing
2. **Use .txt files** - Easier than JSON, same information
3. **Focus on patterns** - 3+ occurrences, not one-off issues
4. **Be specific** - Quote exact errors with timestamps
5. **Quantify impact** - Time wasted, builds failed, expected savings
6. **Provide ready-to-use content** - Exact text for instruction files

## Troubleshooting

**Issue:** Analysis is too generic
**Fix:** Demand specific quotes from session file with line numbers

**Issue:** No file reading confirmed
**Fix:** Start over with mandatory file reading step

**Issue:** Can't find session files
**Fix:** Check `adk_openspec_apply_agent/*.session.txt` (not .json)

---

Transform session data into actionable intelligence. Always read actual files before providing recommendations.
