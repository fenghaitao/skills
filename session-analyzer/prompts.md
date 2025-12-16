# Session Analyzer - Claude Code Prompts

## 🎯 **MAIN PROMPT (Use This First!)**

```
Read these files in order before analysis:
1. adk_openspec_apply_agent/apply_agent_instruction.md
2. adk_openspec_apply_agent/apply_implement-wdt-initial_20251214_161520.session.txt
3. openspec-memories/ (browse and select 2-3 relevant files)

ONLY after reading all files, provide analysis with specific quotes from the session. Do NOT give generic advice without reading the actual files.

Focus on:
- Error patterns with frequencies and timestamps
- Specific agent instruction gaps with evidence
- Memory document improvements needed
- Concrete recommendations with expected impact metrics

Quote exact error messages and reference line numbers from the session file.
```

## 📋 **Alternative Prompts**

### **Quick Analysis**
```
Read adk_openspec_apply_agent/apply_agent_instruction.md, then analyze the latest .session.txt file in adk_openspec_apply_agent/ directory. Focus on the top 3 error patterns by time impact and provide specific improvement recommendations.
```

### **Deep Analysis**
```
Perform comprehensive session analysis:
1. Read adk_openspec_apply_agent/apply_agent_instruction.md
2. Read adk_openspec_apply_agent/apply_implement-wdt-initial_20251214_161520.session.txt  
3. Read 2-3 key files from openspec-memories/
4. Provide complete error pattern breakdown with frequencies
5. Generate specific text additions for agent instruction file
6. Create new memory documents with example content
7. Include expected impact metrics for each recommendation
```

### **Instruction Improvement Focus**
```
Focus on improving agent instructions:
1. Read current apply_agent_instruction.md
2. Read session file to identify instruction gaps
3. Quote specific examples where current instructions failed
4. Provide exact text additions/modifications for instruction file
5. Show before/after comparisons
```

### **Memory Document Gap Analysis**
```
Analyze knowledge gaps in memory documents:
1. Read session file for errors caused by missing domain knowledge
2. Check openspec-memories/ for existing knowledge
3. Identify gaps where better examples could prevent errors  
4. Generate specific memory document content to fill gaps
5. Provide ready-to-use markdown content for new memory docs
```

## 🚨 **Validation Prompt**
```
Before providing any recommendations:
1. Quote at least 3 specific error messages from the session
2. Show timestamps of when issues occurred
3. Reference specific agent responses from the log
4. Only then provide improvement recommendations

If you cannot quote specific errors, you haven't read the session properly.
```