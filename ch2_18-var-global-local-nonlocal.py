x = "variable"

def main():
    val = 10

    def fun():
        global x
        x = "not valid"
        print("call function inside:", x)
        nonlocal val
        val = 20
        print("non-local val:", val)

    fun()
    print("value in main:", val)

main()

print("call function outside:", x)
