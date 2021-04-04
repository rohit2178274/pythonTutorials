#map functions
def myFunc(a):
    return a*a
x = map(myFunc,[1,2,3,4])
print(x)

print(list(x))
print(tuple(x))

#with two arguments

def myFunc(a,b):
    return a*b
x = map(myFunc,[1,2,3,4],[5,6,7,8])
print(x)
print(list(x))

x = list(map(lambda a,b:a+b,[1,3,4,5],[6,7,8,9]))
print(x)

y = list(map(lambda a:a+3,[2,3,4,5]))
print(y)


#filter functions using lambda funtions
def new1(a):
    if(a>3):
        return a
j = filter(new1,(3,4,5,6,2,3,6,4))
print("filter function",tuple(j))

new1 = (9,4,3,5,8)
y = list(filter(lambda a:a>3,new1))
print("filter function using lambda function",y)

#reduce function using lambda function
from functools import reduce
def a(x,y):
    return x+y
z = reduce(a,[2,3,4,5,6,7])
print("sum of all values",z)

z = reduce(lambda p,q:p*q,(2,3,4,5))
print("using reduce function",z)

#filter eithin map function
c = map(lambda x:2*x,filter(lambda a:a>3,(3,4,5,2,4,5)))
print(list(c))
