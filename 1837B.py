
def process(n,s):
    mx=-1
    l=len(s)
    for i in range(l):
        c=s[i]
        cnt=1
       # print(f"c {c}")
        for j in range(i+1,l,1):
            if s[j]==c:
                #print(f"s[j] {s[j]}")
                cnt=cnt+1
                
            else:
                break    
        mx=max(mx,cnt)
    return mx+1         
        
        
    
    

t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    s=input()
    tans=process(n,s)
    res.append(tans)
    
for e in res:
    print(e)    