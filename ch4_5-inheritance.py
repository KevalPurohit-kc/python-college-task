#single inheritance
class A:
    def methodA(self):
        print("===Single inheritance=== \nclass A")
class B(A):
    def method(self):
        print("class B")
obj = B()
obj.methodA()
obj.method()
#multileve inheritance
class A1:
    def fun1(self):
        print("====Multilevel==== \nClass A1")
class A2(A1):
    def fun2(self):
        print("Class A2")  
class A3(A2):
    def fun(self):
        print("Class A3")
obj1 = A3()
obj1.fun1()
obj1.fun2()
obj1.fun()
#multiple inheritance
class B1:
    def func1(self):
        print("===Multiple=== \nbase Class B1")
class B2:
    def func2(self):
        print("Class base B2")
class B3(B1,B2):
    def func3(self):
        print("derived Class B3")
obj2 = B3()
obj2.func1()
obj2.func2()
obj2.func3()