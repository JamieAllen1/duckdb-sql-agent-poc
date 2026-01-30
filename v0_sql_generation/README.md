# v0 – SQL generation only

This version demonstrates a common baseline: using an LLM to translate
natural language questions into SQL without any execution or validation.

## What this shows
- LLMs are good at producing syntactically plausible SQL
- They will confidently invent tables, columns, and business logic

## Why this is not an agent
- No observation of real schema
- No execution
- No feedback loop

This is a starting point, not a solution.