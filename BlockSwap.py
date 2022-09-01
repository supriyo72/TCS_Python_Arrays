from array import *
from numpy import *
k=2
arr=[1,2,3,4,5]
res=[]
ress=[]
for i in range(k,len(arr)):
    res.append(arr[i])
   
for j in range(0,k):
    ress.append(arr[j])
    
    
print(concatenate([res,ress]))