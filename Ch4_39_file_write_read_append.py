from pathlib import Path

file_path = Path(__file__).parent / "sample.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("First line of text.\n")
    file.write("Second line of text.\n")
print("Data written using write mode.")

with open(file_path, "r", encoding="utf-8") as file:
    print("File contents:\n" + file.read())

with open(file_path, "a", encoding="utf-8") as file:
    file.write("Third line added using append mode.\n")
print("Data added using append mode.")

with open(file_path, "r", encoding="utf-8") as file:
    print("Updated file contents:\n" + file.read())