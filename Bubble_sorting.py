def function(num):
    n=len(num)
    for i in range(n):
        for j in range(0,n-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]

numbers=[3,2,4,2,3,1]
function(numbers)
print(numbers)


