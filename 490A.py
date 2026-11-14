n=int(input())
a=list(map(int,input().strip().split()))
hs=dict()
hs[1]=[]
hs[2]=[]
hs[3]=[]
for i in range(n):
    e=a[i]
    hs[e].append(i+1)
    
limit=(2**35)   
mn=limit
for i in range(1,4,1):
    cnt=len(hs[i])
    mn=min(mn,cnt)
print(mn)
for i in range(mn):
    s=f"{hs[1][i]} {hs[2][i]} {hs[3][i]}"  
    print(s)