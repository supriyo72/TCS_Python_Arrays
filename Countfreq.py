alpha = [10,5,10,2,89,7,89,9,9,9]
res= [ ]
for i in alpha:
     if i not in res:
         dup= alpha.count(i)
         res.append(i)
         print(f"{i} : {dup}")