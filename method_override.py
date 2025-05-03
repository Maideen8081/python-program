# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def __add__(self,temp):
#         first=self.m1+self.m2
#         second=temp.m1+temp.m2 
#         total=student(first,second)

#         return total

# obj=student(10,20)
# obj1=student(20,30)
# obj2=obj+obj1
# print(obj2.m1)
# print(obj2.m2)      


class teacher:
    def __init__(self,num):
        self.num=num
    def __add__(self,temp):
        total=self.num+temp.num
        return total

obj=teacher(100)
obj1=teacher(200)
totals=obj+obj1
print(totals)       