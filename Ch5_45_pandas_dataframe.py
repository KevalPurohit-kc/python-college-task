
import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Mina", "Jay"],
    "Marks": [85, 72, 90, 78],
}

df = pd.DataFrame(data)
print("Student data:")
print(df)
print("\nSummary:")
print(df["Marks"].describe())
print("\nAverage marks:", df["Marks"].mean())
print("Highest marks:", df["Marks"].max())
