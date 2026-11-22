
from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent / "students.csv"

if not file_path.exists():
    file_path.write_text(
        "Name,Marks\nAsha,85\nRavi,72\nMina,90\n",
        encoding="utf-8",
    )

df = pd.read_csv(file_path)
print("DataFrame created from CSV:")
print(df)

