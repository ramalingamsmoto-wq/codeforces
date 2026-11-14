t=int(input())
res=[]
for _ in range(t):
    a=list(map(int,input().strip().split()))
    a.sort()
    res.append(a[1])
for j in range(t):
    print(res[j])    