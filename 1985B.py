t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    mx=-1
    v1=-1
    for i in range(2,n+1,1):
        fv=n//i
        s=(fv*(fv+1))//2
        s=s*i
        if s>mx:
            mx=s
            v1=i
    res.append(v1)
for e in res:
    print(e)    