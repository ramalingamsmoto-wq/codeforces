

def process(n,s):
    hs=set()
    cnt=0
    for c in s:
        if c not in hs:
            cnt=cnt+2
            hs.add(c)
        else:
            cnt=cnt+1
    return cnt        
                


t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    s=input()
    tans=process(n,s)
    res.append(tans)
for e in res:
    print(e)    