
def process(n,a):
    dp=[1]*n
    
    i=1
    while True:
        if i>= n:
            break
            
        if a[i]> a[i-1]:
            dp[i]=dp[i-1]+1
        i=i+1    
            
    mx=max(dp)   
    return mx     


n=int(input())
a = list(map(int, input().strip().split()))
tans=process(n,a)
print(tans)
