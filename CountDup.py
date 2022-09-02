arr= [1,1,23,3,3,4,4]
count=0
for i in arr:
    cnt= arr.count(i)
    if cnt>1:
        count+=1
        
print(count)