number1=100
number2=1000
for i in range(number1,number2+1):
    temp=i
    value=0
    count=len(str(i))

    while temp>0:
        digit=temp % 10
        value =value+digit **count
        temp=temp//10

    if i==value:

        list1=[]
        list1.append(i) 
        print(list1)   
   