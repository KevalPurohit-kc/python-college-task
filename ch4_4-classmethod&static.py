class Files:
    def display(self,name):
        self.name = name
        print("class name is:",name)
    @staticmethod
    def static(Mname):
        print("Method name is:",Mname)
        
obj = Files()
obj.display("Files")
obj.static("static")
