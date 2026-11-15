s=input()
n=len(s)
aux=[0]*(n+1)

for i in range(2,n+1,1):
    aux[i]=aux[i-1]
    if s[i-1]==s[i-2]:
        aux[i]=aux[i]+1
#print(f"aux {aux}")        
m=int(input())
res=[]
for _ in range(m):
    l,r=map(int,input().strip().split())
    cnt=aux[r]-aux[l]
    res.append(cnt)
    
for e in res:
    print(e)    