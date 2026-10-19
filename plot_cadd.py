#py plot_cadd.py
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
plt.savefig("cadd_scores.png", dpi=300)
plt.show()
