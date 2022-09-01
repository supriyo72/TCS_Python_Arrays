from array import *
res=[]
arr = [10,5,10,2]
for i in range(0,len(arr)):
    count=0
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            if arr[i] not in res:
                res.append(arr[i])
                count+=1
                print(f"{arr[i]} : {count}")




