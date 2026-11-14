
def process(n,a):
    ind=[[],[]]
    for i in range(n):
        if i%2 != a[i]%2:
            mv=i%2
            ind[mv].append(i)
    if len(ind[0]) != len(ind[1]):
        return -1
    else:
        return len(ind[0])           



t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    tans=process(n,a)
    res.append(tans)
for e in res:
    print(e)    