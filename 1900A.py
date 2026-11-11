

def process(n,s):
    
    pat="..."
    if pat in s:
        return 2
    else:
        r=s.count(".")
        return r
    


t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    s=input()
    tans=process(n,s)
    res.append(tans)
for e in res:
    print(e)    