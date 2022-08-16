from array import *
from numpy import *

arr= [13,5,7,66,8]
# print(min(arr))

max= arr[0]
i=0
while(i<len(arr)):
    if arr[i] > max:
        max= arr[i]
    i=i+1
        
print(max)