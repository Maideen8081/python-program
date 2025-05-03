#skip second nunber

list1=[10,20,30,40,50,60,70,80]
temp=[]
for i in range(0, len(list1),2):
    temp.append(list1[i])

print("  ".join(map(str,temp)))


# map function is used to map the two strings 

def odd_number(num):
    odd=[]
    for i in range(0,len(num)):
        if(i%2==0):
            odd.append(num[i])
    return odd
        
num=[1,2,3,4,5,6]
result=odd_number(num)
print(result)    



# find even number in the given list

num=[10,20,30,40,50]
var=[num[i] for i in range(0,len(num)) if i%2!=0]
print(var)


def find_number(x,y,z):
    for i in range(0,z):
        if(x[i]==y):
            return i
    return None

x=[10,20,30,40,33]
y=40
z=len(x)

result=find_number(x,y,z)

if(result==None):
    print("not fount")

else:
    print("present",result)    
            
