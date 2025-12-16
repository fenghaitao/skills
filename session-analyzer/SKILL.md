---
name: session-analyzer
description: Analyze ADK apply agent session logs to identify performance issues, error patterns, and generate specific recommendations for improving agent instructions and memory documents. Reads from adk_openspec_apply_agent/ directory structure.
license: Apache-2.0
metadata:
  version: "2.0"
  source: "ADK OpenSpec Integration"
  compatible_with: ["ADK", "OpenSpec", "Simics"]
---

# Session Analyzer

This skill analyzes ADK apply agent session logs to systematically improve agent performance over time. It reads session files from the `adk_openspec_apply_agent/` directory and provides specific recommendations based on actual session data.

## 🎯 Mission

Transform raw apply agent session data into actionable intelligence that makes AI agents smarter, faster, and more reliable through systematic analysis and evidence-based improvements.

## Analysis Framework

### 🔍 CRITICAL: Start with Required File Reading (MANDATORY)
**You MUST read these specific files BEFORE any analysis. No exceptions.**

**Required Files to Read:**
1. **Agent Instructions**: `adk_openspec_apply_agent/apply_agent_instruction.md`
2. **Session Data**: `adk_openspec_apply_agent/apply_implement-wdt-initial_20251214_161520.session.txt` (or latest .session.txt)
3. **Memory Documents**: 2-3 key files from `openspec-memories/` directory

**⚠️ WARNING**: Analysis without reading these actual files is USELESS and wastes time!

**✅ SUCCESS PATTERN**: When files are read properly, expect comprehensive analysis with:
- Specific error quotes with timestamps
- Root cause identification for each issue
- Quantified improvement recommendations
- Clear next action items

### Step 1: Read Required Files
Execute these in order:
1. **Read agent instructions** to understand current capabilities and rules
2. **Read session file** completely (use multiple reads if the file is large)
3. **Read memory documents** to understand existing knowledge base
4. **ONLY THEN** proceed with analysis

### Step 2: Parse Session Timeline
Extract chronological events from session text:
- **Timestamps**: When each action occurred
- **Build attempts**: Each compilation try with outcomes
- **Error events**: All compilation failures and their messages
- **Fix attempts**: What the agent tried to resolve each error
- **Success points**: When problems were actually resolved

### Step 3: Error Pattern Analysis
Focus on extracting and categorizing:
- **Build errors**: Compilation failures, missing dependencies, syntax errors
- **Agent responses**: How the agent attempted to fix each error
- **Success patterns**: What approaches worked and why
- **Failure patterns**: What approaches consistently failed and why
- **Time analysis**: How long each error type took to resolve

**⚠️ CRITICAL ERROR COUNTING**: Group related errors together. 
Example: "unknown identifier: 'WDOGLOAD', 'WDOGPERIPHID0', 'WDOGPERIPHID1'" = 3+ separate errors, not 1 error pattern.

## 📊 Complete Analysis Workflow Example

Based on real ADK apply_agent sessions, here's the comprehensive analysis approach:

```markdown
## Session Analysis: apply_implement-wdt-initial_20251214_161520.session.txt

### 📈 Executive Summary
- **Duration**: 10.4 minutes (624 seconds)
- **Total build attempts**: 8 attempts
- **Total fix attempts**: 15 individual fixes
- **Final outcome**: ✅ Success (device built and tested)
- **Efficiency score**: 2/5 (significant room for improvement)

### 🔥 Critical Error Patterns (Prioritized by Impact)

#### 1. **DML Scope Confusion**: `unknown identifier: 'bank'` 
   - **Frequency**: 12 occurrences across 4 build attempts
   - **Time lost**: 3.2 minutes
   - **Root cause**: Agent used wrong scope context for register access
   - **Successful fix**: Changed from `bank.WDOGLOAD` to `BankName.WDOGLOAD` or direct `WDOGLOAD`
   - **Impact**: HIGH - Major compilation blocker

#### 2. **Legacy DML Pattern**: `unknown identifier: 'regs'`
   - **Frequency**: 8 occurrences across 3 build attempts  
   - **Time lost**: 2.1 minutes
   - **Root cause**: Agent used outdated DML 1.2 `regs.` prefix pattern
   - **Successful fix**: Removed `regs.` prefix entirely
   - **Impact**: MEDIUM - Compilation blocker but easier to fix

### 🧠 Agent Instruction Gaps Identified

#### Gap 1: **DML Context Awareness**
- **Evidence**: Agent consistently used wrong scope patterns
- **Current instruction missing**: Clear guidelines for when to use different register access patterns
- **Recommended addition**:
  ```
  ## DML Register Access Context Rules
  - **Device level**: Use `BankName.RegisterName`  
  - **Bank level**: Use `RegisterName` directly
  - **Register level**: Use `this` for self-reference
  - **Never use**: `regs.` prefix (DML 1.2 legacy)
  ```

### 📚 Memory Document Updates Needed

#### New Document: `08_DML_Common_Compilation_Errors.md`
```markdown
# Common DML Compilation Error Patterns

## "unknown identifier: '[register_name]'"
**Cause**: Wrong scope or missing register definition
**Fix checklist**:
1. Check current scope (device vs bank vs register)
2. Use appropriate access pattern for scope
3. Verify register is defined in current bank
4. Remove any legacy `regs.` prefixes
```

### ⚡ Priority Recommendations (Ordered by Expected Impact)

1. **🎯 HIGHEST**: Add DML scope context rules to agent instructions
   - **Expected impact**: Reduce scope-related build attempts by 80%
   - **Time savings**: ~5-6 minutes per session
   - **Implementation**: Add 4-line rule set to instruction file

2. **🎯 HIGH**: Create compilation error troubleshooting memory document  
   - **Expected impact**: Faster error resolution, better fix strategies
   - **Time savings**: ~2-3 minutes per session
   - **Implementation**: New memory doc with error patterns and fixes

### ✅ Success Patterns to Reinforce

- **RAG query usage**: Agent effectively used documentation when uncertain
- **Iterative refinement**: Good at making small, targeted changes
- **Test-driven approach**: Properly validated fixes with build attempts

### 🎯 Expected Impact After Improvements

- **Build attempts**: 8 → 2-3 attempts (62% reduction)
- **Time to completion**: 10.4 → 4-5 minutes (52% reduction)  
- **Error prevention**: 80% of scope-related errors avoided
```

## 📄 **Markdown Report Generation - MANDATORY OUTPUT**

### 🎯 **Always Create Analysis Report File**
After completing analysis, you MUST create a markdown report file in the project directory:

**File naming pattern**: `{component}_implementation_analysis_{YYYYMMDD}.md`
**Example**: `wdt_implementation_analysis_20251214.md`

**File location**: Same directory as the session file (adk_openspec_apply_agent/ directory)

### 📋 **Required Report Structure** 
Use this exact template structure:

```markdown
# {Component} Implementation Analysis from Apply Agent Session

## Session Overview
- **Date**: [Start time to end time]
- **Duration**: [X.X minutes]  
- **Change ID**: [change identifier]
- **Status**: [Completed/Failed/Partial]

## Implementation Summary
### [Component] Implementation (All Tasks Completed/Failed)
- **[Feature 1]**: [Description] ✓/✗
- **[Feature 2]**: [Description] ✓/✗
[List all implemented features with status]

### Core Functionality Implemented
[Bullet points of main functionality]

### Test Files Created  
[List all test files created]

## Error Patterns and Issues Identified
### Build Success/Failures
[Compilation results and fixes applied]

### Test Failures (Root Cause Analysis)  
[WHY tests failed, not just WHAT failed]

### Specific [Technology] Issues Encountered
[Technology-specific problems and solutions]

## Agent Instruction Gaps
### Missing [Error Type] Guidance
[Specific gaps in current instructions]

### [Infrastructure] Requirements
[Missing information about setup/requirements]

## Memory Document Improvements Needed
### [Technical Area] Enhancement
[Specific additions needed to memory docs]

### [Process Area] Best Practices
[Documentation improvements for processes]

## Performance and Architecture Assessment
### Efficient Implementation
[What was done well architecturally]

### Architectural Soundness  
[Assessment of design quality]

## Expected Impact Metrics
### Implementation Success Rate
[Quantified success percentages]

### Performance Characteristics
[Technical performance aspects]

## Recommendations for Future Work
### Immediate Actions
1. [Highest priority item]
2. [Second priority item]  
3. [Third priority item]

### Process Improvements
1. [Process enhancement]
2. [Workflow improvement]

## Analysis of Apply Agent Session
### Time Distribution
[How time was spent during session]

### Key Learning Points  
[Important technical insights discovered]

### Overall Quality Assessment
[Final assessment with rationale]
```

## 🚀 Usage Examples & Ready-to-Use Prompts

### 📋 Quick Analysis (5-10 minutes)
**Prompt**: 
```
"Read adk_openspec_apply_agent/apply_agent_instruction.md, then analyze the latest .session.txt file in adk_openspec_apply_agent/ directory. Focus on the top 3 error patterns by time impact and provide specific improvement recommendations.

MANDATORY: Create a markdown analysis report file using the template structure from session-analyzer skill."
```

### 🔍 Deep Dive Analysis (15-20 minutes)  
**Prompt**:
```
"Perform comprehensive session analysis:
1. Read adk_openspec_apply_agent/apply_agent_instruction.md
2. Find and read the latest .session.txt file in adk_openspec_apply_agent/ directory
3. Read 2-3 key files from openspec-memories/
4. Provide complete error pattern breakdown with frequencies
5. Generate specific text additions for agent instruction file
6. Create new memory documents with example content
7. Include expected impact metrics for each recommendation

MANDATORY: Create a comprehensive markdown analysis report file using the template structure from session-analyzer skill."
```

### 📈 Instruction Improvement Focus
**Prompt**:
```
"Focus on improving agent instructions:
1. Read current apply_agent_instruction.md
2. Read session file to identify instruction gaps
3. Quote specific examples where current instructions failed
4. Provide exact text additions/modifications for instruction file
5. Show before/after comparisons

MANDATORY: Create a markdown analysis report focusing on instruction improvements."
```

### 🧠 Memory Document Gap Assessment  
**Prompt**:
```
"Analyze knowledge gaps in memory documents:
1. Read session file for errors caused by missing domain knowledge
2. Check openspec-memories/ for existing knowledge
3. Identify gaps where better examples could prevent errors  
4. Generate specific memory document content to fill gaps
5. Provide ready-to-use markdown content for new memory docs

MANDATORY: Create a markdown analysis report with new memory document content included."
```

## 📈 **Quality Validation - Is the Analysis Working?**

### ✅ **Good Analysis Indicators**
If you see these patterns, the skill is working correctly:
- **File reading confirmed**: Shows actual file paths and content being read
- **Specific quotes**: References exact error messages from session logs
- **Timeline analysis**: Mentions timestamps and sequence of events
- **Quantified metrics**: Provides specific numbers (build attempts, error counts, time spent)
- **Root cause identification**: Explains WHY errors occurred, not just WHAT happened
- **Actionable recommendations**: Gives specific text to add to instruction files

### ❌ **Poor Analysis Indicators**
Stop and re-prompt if you see these warning signs:
- **Generic advice**: Talks about "common DML patterns" without session specifics
- **No file reading**: Doesn't mention specific files being read
- **Vague recommendations**: Says "improve documentation" without specific examples
- **No error quotes**: Discusses errors but doesn't quote actual error messages
- **No metrics**: Provides recommendations without expected impact numbers

### 🔧 **When Analysis Goes Wrong - Recovery Prompts**
```
"Stop. You're giving generic advice. Please:
1. Show me the specific files you read
2. Quote exact error messages from the session
3. Provide specific text additions for instruction files
If you haven't read the session file, start over with file reading."
```

## 🔧 Claude Code-Specific Optimization

### 🎯 **MANDATORY Start Prompt for Claude Code**
```
"Read these files in order before analysis:
1. adk_openspec_apply_agent/apply_agent_instruction.md
2. Find and read the latest .session.txt file in adk_openspec_apply_agent/ directory (typically named apply_[change-id]_[timestamp].session.txt)
3. openspec-memories/ (browse and select 2-3 relevant files)

ONLY after reading all files, provide analysis with specific quotes from the session. Do NOT give generic advice without reading the actual files.

MANDATORY OUTPUT: Create a markdown analysis report file in the project directory using the template structure from session-analyzer skill. Name it: {component}_implementation_analysis_{YYYYMMDD}.md"
```

### 🛠️ **Troubleshooting Claude Code Issues**

### **Issue: Skill gives generic advice**
**Solution**: Always use the MANDATORY Start Prompt above and verify file reading

### **Issue: "Files not found"**
**Solution**: Files are in current project directory:
- `./adk_openspec_apply_agent/apply_agent_instruction.md`
- `./adk_openspec_apply_agent/*.session.txt`
- `./openspec-memories/`

### **Issue: Analysis too high-level**
**Solution**: Demand specific quotes with line numbers from session file

### **Issue: No concrete recommendations**
**Solution**: Require exact text additions for instruction file and specific memory document content

## 💡 Pro Tips

1. **Start with agent instructions**: Understand current rules before analyzing failures
2. **Quote specific errors**: Always reference exact error messages from session
3. **Quantify improvements**: Provide metrics for expected time/attempt savings  
4. **Generate ready-to-use content**: Provide exact text for instruction updates
5. **Focus on patterns**: Look for recurring issues across multiple build attempts
6. **🆕 VALIDATE**: Always read actual session files before providing recommendations
7. **🆕 BE SPECIFIC**: Reference line numbers, timestamps, and exact quotes

---

This skill transforms raw session data into actionable intelligence for improving ADK apply agent performance. **Always read the required files from adk_openspec_apply_agent/ and openspec-memories/ directories first.**