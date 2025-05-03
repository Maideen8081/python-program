number=1532
value=0
temp=number
count=len(str(number) )

while temp>0:
    degit=temp % 10
    value=value + degit **count
    temp= temp//10

if value==number:
    print("armstrong")  
else:
    print("not armstrong")     