from itertools import groupby

t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    s=input()
    temp1 = [key for key, _ in groupby(s)]
    is_unique = len(temp1) == len(set(temp1))
    if is_unique:
        res.append("YES")
    else:
        res.append("NO")  
        
for e in res:
    print(e)          
    
    