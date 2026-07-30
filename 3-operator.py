#Operators
print('''Enter following any one number
        1)Addition
        2)Subtraction
        3)Multiplication
        4)Divition...''')
value = int(input("enter a value:"))
val1=int(input("enter digite 1:" ))
val2=int(input("enter digite 2:" ))
if( value == 1):
    print("Sum is :" ,val1 + val2)
elif (value == 2):
    print("Subtraction is :", val1 - val2)
elif(value == 3):
    print("Multiplication is :" ,val1 * val2)
elif(value == 4):
    print("Divition is :", val1 / val2)
else :
    print("Your number is not valide")

    



