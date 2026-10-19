
import sqlite3
import pandas as pd

# Connect to the SQLite database
connection = sqlite3.connect("genomics.db")

# Load variant data into a DataFrame
df = pd.read_sql_query(
    "SELECT * FROM variants",
    connection
)

# Filter variants
filtered = df[
    (df["AF"] <= 0.01) &
    (df["CADD"] > 20)
]

# Sort by CADD score, highest first
result = filtered.sort_values(
    by="CADD",
    ascending=False
)

print(result)

connection.close()


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
connection = sqlite3.connect("genomics.db")

# Load data into pandas
df = pd.read_sql_query(
    "SELECT * FROM variants",
    connection
)

connection.close()

# Create a bar chart
plt.bar(df["gene"], df["CADD"])

plt.xlabel("Gene")
plt.ylabel("CADD Score")
plt.title("CADD Scores by Gene")

plt.tight_layout()
plt.show()
