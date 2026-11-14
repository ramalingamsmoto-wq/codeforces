s=set("codeforces")
t=int(input())
res=[]
for _ in range(t):
    c=input()
    if c in s:
        res.append("YES")
    else:
        res.append("NO")   
         
for s in res:
    print(s)