

def process(a):
    al=list(a)
    
    fl=[al[1],al[0],al[2]]
    sl=[al[2],al[1],al[0]]
    tl=[al[0],al[2],al[1]]
    
    f="".join(fl)
    s="".join(sl)
    t="".join(tl)
    
    tgt="abc"
    if a==tgt or f==tgt or s==tgt or t==tgt:
        return "YES"
    else:
        return "NO"    
    
    

t=int(input())
res=[]
for _ in range(t):
    s=input()
    tans=process(s)
    res.append(tans)
for e in res:
    print(e)    