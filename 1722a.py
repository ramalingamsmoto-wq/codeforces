
def process(s):
    sl=list(s)
    sl.sort()
    a="".join(sl)
    
    if a=="Timru":
        return "YES"
        
    return "NO"    



t=int(input())
res=[]
for _ in range(t):
    n=input()
    s=input()
    tans=process(s)
    res.append(tans)
for e in res:
    print(e)    
    