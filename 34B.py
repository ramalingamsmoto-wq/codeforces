n,m=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
b=[]
for e in a:
    if e < 0:
        b.append(-e)
b.sort(reverse=True) 
mn=min(n,m) 
#print(f"min {mn}")
r=sum(b[0:mn])  
print(r)    