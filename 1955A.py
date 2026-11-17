import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,a,b):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=a
    for i in range(2,n+1,1):
        
        
        v1=dp[i-1]+a
           
        v2=dp[i-2]+b
        dp[i]=min(v1,v2)
    return dp[n]
    
res=[]
for _ in range(ii()):
    n,a,b=mi()
    t=process(n,a,b)
    res.append(t)
    
for e in res:
    print(e)    