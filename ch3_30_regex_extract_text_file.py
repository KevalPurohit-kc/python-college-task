import re

file_name = input("Enter text file path: ").strip()

with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
phones = re.findall(r"\b\d{10}\b", text)
dates = re.findall(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b", text)

print("Email addresses:", emails)
print("Phone numbers:", phones)
print("Dates:", dates)
