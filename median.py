from array import *
from numpy import *
arr= [2,5,1,7]
a=sort(arr)
l=len(a)
print(a)
if len(a) %2 ==0:
    c= l/2
    d= c+1
    res1= c-1
    res2= d-1
    res= a[int(res1)] + a[int(res2)]
    print(res/2)
else:
    g= l+1
    h= g/2
    res3= h-1
    res4= int(res3)
    print(a[res4])
    
    