
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Mina", "Jay"],
    "Marks": [85, None, 90, 78],
    "City": ["Surat", "Rajkot", None, "Ahmedabad"],
}

df = pd.DataFrame(data)
print("Original data:")
print(df)

print("\nRows after dropna():")
print(df.dropna())

filled_df = df.copy()
filled_df["Marks"] = filled_df["Marks"].fillna(filled_df["Marks"].mean())
filled_df["City"] = filled_df["City"].fillna("Unknown")
print("\nData after fillna():")
print(filled_df)

