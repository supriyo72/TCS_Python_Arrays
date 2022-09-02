arr= [1,1,1,2,2,3,3,3,3,4,4]
res=[]
for i in arr:
    cnt= arr.count(i)
    if cnt>1:
        if i not in res:
            res.append(i)
# print(res)
a= len(arr)-len(res)
# print(a)
res1=[]
for j in range(a):
    x= '_'
    res1.append(x)
# print(res1)
for k in range(len(res1)):
    res.append(res1[k])
    
print(res)