



t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    q=n//3
    r=n%3
    tans=""
    if r==0:
        tans=f"{q} {q}"
    elif r==1:
        tans=f"{q+1} {q}"
    elif r==2:
        tans=f"{q} {q+1}"  
    res.append(tans)   

for e in res:
    print(e)    
        