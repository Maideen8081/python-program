class sample:
    def function(self,*ref):
        temp=0
        for i in ref:
            temp=temp+i
        print(temp) 
obj=sample()
obj.function(10,20,30)      