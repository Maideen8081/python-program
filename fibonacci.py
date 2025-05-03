input=10
#input=int(input("Enter the number"))
n1=0
n2=1
if input<=0:
    print("Enter the positive number")
elif input==1:
    print("enter the morthan 1 ")
else:
    print("fibonacci number")
    count=0  

    while count<=input:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count +=1
