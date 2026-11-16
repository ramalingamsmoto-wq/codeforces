

res=[]
for _ in range(int(input())):
    a,b,c,d=map(int,input().strip().split())
    if a==b==c==d:
        res.append("YES")
    else:
        res.append("NO")  
        
for e in res:
    print(e)          