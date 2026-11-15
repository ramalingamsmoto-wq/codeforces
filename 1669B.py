from collections import Counter

def find_first_triple(items):
    counts = Counter()
    for item in items:
        counts[item] += 1
        if counts[item] == 3:
            return item  # Stops counting immediately
    return None

res=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    
    mc =find_first_triple(a)
    if mc==None:
        res.append(-1)
    else:
        res.append(mc) 
         
for e in res:
    print(e)          
    