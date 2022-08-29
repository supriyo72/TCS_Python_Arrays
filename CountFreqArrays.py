from array import *

arr = [10,5,10,15,10,5]

for i in range(0,len(arr)):
    count=0
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            count+=1
            
    print(f"{arr[i]} : {count}")