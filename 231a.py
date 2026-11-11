n=int(input())
cnt=0
for i in range(n):
    a,b,c=map(int,input().strip().split())
    if a+b+c >=2:
        cnt+=1
print(cnt)        