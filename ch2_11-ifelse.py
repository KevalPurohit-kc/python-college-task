info = int(input("select number 1 for login \n2 for register:"))


if (info == 1):
    admin = input("Enter user name:")
    password = int(input("enter password:"))
    if (admin == 'adminlog' and password == 4542):
        print("success login")
    else:
        print("your user name and password are wrong")
elif(info == 2):
    new = input("enter new user name :")
    npass = int(input("enter new password:"))
    print("success Register")
else:
    print("Please select either 1 or 2")
