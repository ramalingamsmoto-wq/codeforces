from collections import Counter

res=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    counts = Counter(a)
    is_all_one = all(v == 1 for v in counts.values())
    if is_all_one:
        res.append("YES")
    else:
        res.append("NO") 
        
for e in res:
    print(e)           
    
    
    
