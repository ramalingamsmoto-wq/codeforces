

def process(n,k):
    if n%2!=0 and (k>n or k%2==0):
        return "NO"
    else:
        return "YES"    
            


t=int(input())
res=[]
for _ in range(t):
    n,k=map(int,input().strip().split())
    tans=process(n,k)
    res.append(tans)
for e in res:
    print(e)    
    