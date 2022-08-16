from array import *
from numpy import *

arr= [13,5,7,6,8]
# print(min(arr))

min= arr[0]
i=0
while(i<len(arr)):
    if arr[i] < min:
        min= arr[i]
    i=i+1
        
print(min)