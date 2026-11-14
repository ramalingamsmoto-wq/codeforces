from collections import Counter

n = int(input())
a = list(map(int, input().strip().split()))
ac = Counter(a)
hs = dict()
for e, count in ac.items():
    hs[e] = e * count
    
sk = sorted(hs)  
l = len(sk)  
dp = [0] * l
et = [0] * l

if l == 1:
    dp[0] = hs[sk[0]]
    print(dp[0])
    
elif l == 2:
    dp[0] = hs[sk[0]]  # <-- FIXED: Initialize dp[0] so it isn't 0
    if sk[1] - sk[0] > 1:
        dp[1] = dp[0] + hs[sk[1]]
    else:
        if hs[sk[0]] > hs[sk[1]]: 
            dp[1] = dp[0]
        else:
            dp[1] = hs[sk[1]]
    print(dp[1])       

elif l > 2:
    dp[0] = hs[sk[0]]
    if sk[1] - sk[0] > 1:
        dp[1] = dp[0] + hs[sk[1]]
    else:
        if hs[sk[0]] > hs[sk[1]]: 
            dp[1] = dp[0]
        else:
            dp[1] = hs[sk[1]]
    
    for i in range(2, l, 1):
        if sk[i] - sk[i-1] > 1:
            v1 = dp[i-1] + hs[sk[i]]
        else:
            v1 = dp[i-2] + hs[sk[i]]
            
        v2 = dp[i-1]
        if v1 > v2:
            dp[i] = v1
        else:
            dp[i] = v2
            
    print(dp[l-1])  
    