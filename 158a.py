n,k=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
cnt=0
ts=a[k-1]
for i in range(n):
    if a[i] > 0 and a[i] >= ts:
        cnt=cnt+1
print(cnt)    