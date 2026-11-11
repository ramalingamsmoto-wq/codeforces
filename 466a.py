n,m,a,b=map(int,input().strip().split())
dp=[0]*(n+1)
for i in range(1,n+1,1):
    v1=dp[i-1]+a
    v2=0
    if i-m >=0:
        v2=dp[i-m]+b
    else:
        v2=b    
    
    dp[i]=min(v1,v2)
    
#print(f"dp {dp}") 
   
print(dp[n])   