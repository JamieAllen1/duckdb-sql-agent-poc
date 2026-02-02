# v1 – Tool execution (DuckDB)

This version executes LLM-generated SQL against a real DuckDB database (TPC-H sf=0.1).
The model is still blind to the schema, so failures are expected and useful.

## What changed from v0
- Added DuckDB execution (`run_sql`)
- Prints the generated SQL and the database error/result

## What this demonstrates
- “Plausible SQL” is not “correct SQL”
- Execution provides the feedback needed for iteration (agent behaviour comes later)

## Run
python v1_tool_execution/main.py