from dotenv import load_dotenv
import os

import duckdb
from openai import OpenAI

load_dotenv()

DB_PATH = os.getenv("DUCKDB_PATH", "data/tpch.duckdb")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You translate analytical questions into DuckDB SQL.

Rules:
- Return only SQL (no backticks, no explanations).
- Prefer a single query.
- Add LIMIT 50 unless the question clearly asks for a single response or aggregation.
"""

def generate_sql(question: str) -> str:
    resp = client.responses.create(
        model="gpt-5",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    return resp.output_text.strip()

def run_sql(sql: str, max_rows: int = 50) -> dict:
    con = duckdb.connect(DB_PATH, read_only=True)
    try:
        res = con.execute(sql)
        cols = [d[0] for d in res.description] if res.description else []
        rows = res.fetchmany(max_rows)
        return {"ok": True, "columns": cols, "rows": rows, "truncated": len(rows) == max_rows}
    except Exception as e:
        return {"ok": False, "error": str(e), "sql": sql}
    finally:
        con.close()

def main():
    question = "Top 10 customers by total revenue last quarter"

    sql = generate_sql(question)
    print("\n--- Generated SQL ---\n")
    print(sql)

    result = run_sql(sql)

    print("\n--- DuckDB Result ---\n")
    if result["ok"]:
        print("Columns:", result["columns"])
        for r in result["rows"]:
            print(r)
        if result["truncated"]:
            print("\n(truncated)")
    else:
        print("ERROR:")
        print(result["error"])
        print("\nSQL that failed:\n")
        print(result["sql"])


if __name__ == "__main__":
    main()