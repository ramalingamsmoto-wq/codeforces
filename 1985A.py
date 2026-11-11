t=int(input())
res=[]
for _ in range(t):
    a,b=input().strip().split()
    fa=a[0]
    fb=b[0]
    na=b[0]+a[1:]
    nb=a[0]+b[1:]
    s=f"{na} {nb}"
    res.append(s)
for e in res:
    print(e)    