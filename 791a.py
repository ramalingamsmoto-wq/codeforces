a,b=map(int,input().strip().split())
cnt=0
while True:
    if a > b:
        break
    else:
        a=3*a
        b=2*b
        cnt=cnt+1
print(cnt)