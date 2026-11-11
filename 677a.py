n,h=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
l=len(a)
w=0
for i in range(l):
    if a[i] <= h:
        w=w+1
    else:
        w=w+2 
print(w)           