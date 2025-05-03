class Example:
    def setname(self,name):
        self.__name=name

    def getname(self):
        return self.__name  
    
    def display(self):
        print(self.__name)

obj=Example()
obj.setname("vinoth") 

obj.display()