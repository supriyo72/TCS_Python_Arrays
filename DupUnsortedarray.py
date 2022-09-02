arr= [4,3,9,2,4,1,10,89,34]
res=[]
for i in arr:
    cnt= arr.count(i)
    if cnt>1:
        if i not in res:
            res.append(i)
    else:
        res.append(i)
print(res)