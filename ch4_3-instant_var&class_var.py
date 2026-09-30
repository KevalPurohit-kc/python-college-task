class var:
    var = "class variable"
    def __init__(self,acc_no):
        print(self.var)
        self.acc_no = acc_no
        print(self.acc_no)
obj = var(2521)
print(obj.acc_no)
    