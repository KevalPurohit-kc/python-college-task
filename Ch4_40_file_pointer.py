from pathlib import Path

file_path = Path(__file__).parent / "file_pointer.txt"

with open(file_path, "w+", encoding="utf-8") as file:
    file.write("Python file pointer example.")
    print("Pointer after writing:", file.tell())

    file.seek(0)
    print("Pointer after seek(0):", file.tell())

    print("First 6 characters:", file.read(6))
    print("Pointer after reading 6 characters:", file.tell())

    file.seek(7)
    print("Pointer after seek(7):", file.tell())
    print("Text from position 7:", file.read())