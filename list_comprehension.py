#normal list to append the value

list1=[]
for i in "HUMAN":
    list1.append(i)

print(list1)   


# to impliment the lis comprehension

list2=[x for x in "ANIMAL"]
print(list2)

list3=[y for y in range(1,11,2)]
print(list3)


list4=[i for i in range(1,100) if i%2==0 and i%5==0]
print(list4)

list5=[x for x in range(1,100) if x%2==0]
print(list5)