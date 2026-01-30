from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You translate analytical questions into DuckDB SQL.
Assume a reasonable schema if not provided.
Return only SQL.
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

if __name__ == "__main__":
    q = "Top 10 customers by total revenue last quarter"
    print(generate_sql(q))