# method overloading implimented by using the dispatch package

from multipledispatch import dispatch

@dispatch(int,int)
def function(a,b):
    print(a+b)
@dispatch(int,int)
def function(a,b):
    print(a+b)
@dispatch(int,int,int)    
def function(a,b,c):
    print(a+b+c) 

function(10,20)           