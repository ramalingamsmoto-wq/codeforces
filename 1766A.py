import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def er(n):
    sn=str(n)
    
    
    us= sn.replace("0", "")
    nl=len(us)
    
    return nl==1
    
maxn=999_999

dp=[0]*(maxn+1)
for i in range(1,maxn+1,1):
    if er(i):
        dp[i]=1
        
for i in range(1,maxn+1,1):
    dp[i]=dp[i]+dp[i-1]

r=[]
for _ in range(ii()):
    n=ii()
    r.append(dp[n])
    
for e in r:
    print(e)    