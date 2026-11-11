n=int(input())

a=[-1]*(n+1)
b=[-1]*(n+1)

mx=-1
for i in range(1,n+1,1):
    ai,bi=map(int,input().strip().split())
    a[i]=ai
    b[i]=bi
    
tc=0
    
for i in range(1,n+1,1):
    tc=tc-a[i]
    tc=tc+b[i] 
    mx=max(mx,tc) 
    
print(mx)      