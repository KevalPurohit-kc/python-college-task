import os
import shutil

operation = input("Choose operation (copy/move/delete): ").strip().lower()
source = input("Source file path: ").strip()

if not os.path.isfile(source):
    print("File not found.")
elif operation == "copy":
    destination = input("Destination path: ").strip()
    shutil.copy2(source, destination)
    print("File copied.")
elif operation == "move":
    destination = input("Destination path: ").strip()
    shutil.move(source, destination)
    print("File moved.")
elif operation == "delete":
    if input("Delete this file? (y/n): ").strip().lower() == "y":
        os.remove(source)
        print("File deleted.")
    else:
        print("File not deleted.")
else:
    print("Invalid operation.")
