info = int(input("select number 1 for login \n2 for register:"))


if (info == 1):
    if (admin == 'adminlog' and password == 4542):
        admin = input("Enter user name:")
        password = int(input("enter password:"))
        print("success login")
elif(info == 2):
    new = input("enter new user name :")
    npass = int(input("enter new password:"))
    print("success Register")


else:
    print("your user name and password are wrong")


    
