

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    print(int("hello"))
except ValueError:
    print("Error: Invalid value.")

try:
    print("2" + 2)
except TypeError:
    print("Error: Cannot combine these types.")
