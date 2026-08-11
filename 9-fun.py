def fun():
    print("Funcation call")
def fun1(x,y,name):
    print(x)
    print(y, name)
def fun3(age,*name):
    print(age,*name);
fun1(12,60,"keval")
fun()
fun3(25,"Raj","Rohan")
