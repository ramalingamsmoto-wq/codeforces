
def process(h,m):
    cnt=60-m
    h=h+1
    cnt=cnt+((24-h)*60)
    return cnt


t=int(input())
res=[]
for _ in range(t):
    
    h,m=map(int,input().strip().split())
    tans=process(h,m)
    res.append(tans)
for e in res:
    print(e)    