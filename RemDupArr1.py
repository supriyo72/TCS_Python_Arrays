arr= [1,1,23,3,3,4,4]
res=[]
for i in arr:
    cnt= arr.count(i)
    if cnt>1:
        if i not in res:
            res.append(i)
            
print(res)