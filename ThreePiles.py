t=int(input())
res=[]
for _ in range(t):
    a,b,c=map(int,input().strip().split())
    if a-1==b+1==c or a-1==b==c+1 or a==b-1==c+1 or a+1==b-1==c or a+1==b==c-1 or a==b+1==c-1:
        res.append("YES")
    else:
        res.append("NO")  
for e in res:
    print(e)          