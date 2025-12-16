# Session Analyzer - Ready-to-Use Prompts

## 🎯 Essential Prompt (Recommended)

```
Read these files in order:
1. adk_openspec_apply_agent/apply_agent_instruction.md
2. Latest .session.txt file in adk_openspec_apply_agent/
3. 2-3 relevant files from openspec-memories/

Then analyze: What are the top 3 error patterns, their root causes, and specific improvements needed?

Create markdown report: {component}_implementation_analysis_{YYYYMMDD}.md
```

## 📋 Alternative Prompts

### Quick Analysis
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

## 🚨 Recovery Prompt (If Analysis is Too Generic)

```
Stop. You're giving generic advice. Please:
1. Show me the specific files you read
2. Quote exact error messages from the session
3. Provide specific text additions for instruction files
If you haven't read the session file, start over with file reading.
```
