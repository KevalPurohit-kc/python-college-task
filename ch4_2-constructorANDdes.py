class ca521:
    def __init__(self,name):
        print("Hello,\t")
        self.name = name
    def __del__(self):
        print("Destructor")
 
obj= ca521("Raj Kumar")
del obj

