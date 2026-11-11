n=int(input())
a=list(map(int,input().strip().split()))
mx=max(a)
s=0
for e in a:
    s=s+mx-e
print(s)    