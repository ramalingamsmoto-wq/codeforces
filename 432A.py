n,k=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
pending=[5-e for e in a]
cnt=0
for e in pending:
    if e>=k:
        cnt=cnt+1
q=cnt//3
print(q)        