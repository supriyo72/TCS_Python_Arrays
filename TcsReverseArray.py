from array import *

vals= [3,4,5,2,15,78]
res=[]
# vals.reverse()
# print(vals)

i= len(vals)-1
while(i>=0):
    result= vals[i]
    res.append(result)
    
    i-=1
    
print(res)