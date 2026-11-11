

# computes time from prev to current
def getTime(n,curr,prev):
    if curr==prev:
        return 0
    elif prev < curr:
        t=curr-prev
        return t  
    elif curr < prev:
        v1=n-prev
        t=v1+curr
        return t
              


n,m=map(int,input().strip().split())
a=list(map(int,input().strip().split()))

a.insert(0,1)
l=len(a)

ans=0
for i in range(1,l,1):
    t=getTime(n,a[i],a[i-1])
    ans=ans+t
    
print(ans)    