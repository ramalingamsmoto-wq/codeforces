from collections import Counter

def process(n,h):
    ans=[]
    cnt=0
    counts = Counter(h)
    #keys_asc = sorted(counts, key=counts.get)
    keys_asc = sorted(counts)
    cnt=cnt+len(keys_asc)
    ans.extend(keys_asc)
    
    
    
    #print(f"counts {counts}")
    #print(f"keyasc {keys_asc}")
    #counts.subtract(keys_asc)
    counts -= Counter(keys_asc)
    
    #print(f"counts {counts}")
    
    keys_desc=sorted(counts,reverse=True)
    cnt=cnt+len(keys_desc)
    
    #print(f" keydes {keys_desc}")
   
   
   # counts.subtract(keys_desc)
    counts -= Counter(keys_desc)
    
    #print(f"counts {counts}")
    
    flat_list = list(counts.elements())
    #print(f"fl  {flat_list}")
    
    ans.extend(flat_list)
    ans.extend(keys_desc)
    
    tup=(cnt,ans)
    return tup
    
    
    
    
    
    
    
    
    
    
    



t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    h=list(map(int,input().strip().split()))
    tans=process(n,h)
    res.append(tans)
for e in res:
    print(e[0])
    print(*e[1])    