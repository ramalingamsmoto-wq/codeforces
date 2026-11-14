n=int(input())
laptops=[]
for i in range(n):
    p,q=list(map(int,input().strip().split()))
    tup=(p,q)
    laptops.append(tup)
    
sl = sorted(laptops, key=lambda x: x[1])
found=False
for i in range(1,n,1):
    if sl[i][0] < sl[i-1][0]:
        found=True
        break
if found:1367
    print("Happy Alex")
else:
    print("Poor Alex")            