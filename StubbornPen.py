def process(n,s):
    penc='R'
    cnt=0
    for i in range(n):
        paperc=s[i]
        if paperc!=penc:
            cnt=cnt+1
            
        if paperc=='R':
            penc='B'
        else:
            penc='R'        
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