t=int(input())
res=[]
for _ in range(t):
    b=input()
    a=b[0:2]
    r=[b[i] for i in range(3,len(b),2)]
    rs="".join(r)
    res.append(a+rs)
for e in res:
    print(e)    