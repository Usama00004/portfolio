import pandas as pd

# Load data
df = pd.read_csv("customers.csv")

# Clean data
df = df.drop_duplicates()
df["City"] = df["City"].fillna("Unknown")

# Process data (example filter)
df = df[df["City"] == "London"]

# Save result
df.to_csv("processed_customers.csv", index=False)

print("Done ")



import pandas as pd

# IMPORT
data = pd.read_csv("customers.csv")

# TRANSFORM
data = data.drop_duplicates()
data["City"] = data["City"].fillna("Unknown")

# LOAD
data.to_csv("customers_clean.csv", index=False)

print("ETL completed ")
