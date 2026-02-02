import duckdb

con = duckdb.connect("data/tpch.duckdb")

# Generate TPC-H at scale factor 0.1 (tiny but useful)
con.execute("CALL dbgen(sf=0.1);")

# Sanity check
tables = con.execute("SHOW TABLES;").fetchall()
print("Tables created:")
for t in tables:
    print("-", t[0])

con.close()