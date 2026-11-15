t=int(input())
res=[]
for _ in range(t):
    s=input()
    l=len(s)
    a=s[:l//2]
    b=s[l//2:]
    if l%2==0 and a==b:
        res.append("YES")
    else:
        res.append("NO") 
        
for e in res:
    print(e)           