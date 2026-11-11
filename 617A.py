import sys
x=int(input())
dp=[1]*(x+1)

dp[0]=-1
for i in range(6,x+1,1):
    mv=sys.maxsize//100
    for j in range(1,6,1):
        mv=min(mv,dp[i-j]+1)
        
    dp[i]=mv
    
print(dp[x])    
