t=int(input())
res=[]
for _ in range(t):
    a,b,c=map(int,input().strip().split())
    c=c%2
    a=a+c
    if a==b:
        res.append("Second")
    elif a < b:
        res.append("Second")
    elif b <a:
        res.append("First")
        
for e in res:
    print(e)        