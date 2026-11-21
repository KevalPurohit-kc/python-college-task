import os
import sys

folder = sys.argv[1] if len(sys.argv) > 1 else "practice_folder"
os.makedirs(folder, exist_ok=True)

while True:
    print("\n1. List items  2. Create file  3. Create directory")
    print("4. Rename file  5. Delete file  6. Remove empty directory  0. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        print("\n".join(os.listdir(folder)) or "Folder is empty.")
    elif choice == "2":
        name = input("File name: ").strip()
        with open(os.path.join(folder, name), "w", encoding="utf-8") as file:
            file.write(input("Text to write: "))
        print("File created.")
    elif choice == "3":
        name = input("Directory name: ").strip()
        os.mkdir(os.path.join(folder, name))
        print("Directory created.")
    elif choice == "4":
        old_name = input("Current file name: ").strip()
        new_name = input("New file name: ").strip()
        os.rename(os.path.join(folder, old_name), os.path.join(folder, new_name))
        print("File renamed.")
    elif choice == "5":
        name = input("File name to delete: ").strip()
        path = os.path.join(folder, name)
        if os.path.isfile(path) and input("Delete this file? (y/n): ").lower() == "y":
            os.remove(path)
            print("File deleted.")
        else:
            print("File not deleted.")
    elif choice == "6":
        name = input("Empty directory name to remove: ").strip()
        os.rmdir(os.path.join(folder, name))
        print("Directory removed.")
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
