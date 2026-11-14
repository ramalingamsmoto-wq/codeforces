n,a,b,c=map(int,input().strip().split())
dp=[-1]*(n+1)
dp[0]=0
vs=[a,b,c]

for i in range(1,n+1,1):
    mx=-1
    for j in range(len(vs)):
        v=i-vs[j]
        if v >=0 and dp[v] >= 0:
            mx=max(mx,dp[v]+1)
    dp[i]=mx
    
#print(f"dp {dp}")    
print(dp[n])    