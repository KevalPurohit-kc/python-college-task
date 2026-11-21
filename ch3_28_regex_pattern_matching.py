import re

text = input("Enter an identifier: ")

if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", text):
    print("Pattern matched.")
else:
    print("Pattern did not match.")
