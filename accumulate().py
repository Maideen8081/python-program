import itertools
list1=[1,2,3,4,5,6,7,8,9]
print(list(itertools.accumulate(list1,lambda x,y:x+y)))
