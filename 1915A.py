t=int(input())
res=[]
for i in range(t):
    a,b,c=map(int,input().strip().split())
    r=a^b^c
    res.append(r)
    
for i in range(t):
    print(f"{res[i]}")    