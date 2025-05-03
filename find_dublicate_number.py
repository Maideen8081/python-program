list1=[1,2,1,3,4,2,4,3,1,2,4,5]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            print(list1[i])
            break


def dublication(num):
    dublicate=set()
    seen=set()
    for i in num:
        if i in seen:
            dublicate.add(i)
        else:
            seen.add(i)
    return list(dublicate)  
list1=[1,2,1,3,1,23,2,3,1,4,5,3]

print(dublication(list1))