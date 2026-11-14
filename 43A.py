n=int(input())
hs=dict()
for _ in range(n):
    s=input()
    if s in hs:
        cnt=hs[s]
        hs[s]=cnt+1
    else:
        hs[s]=1    
mk = max(hs, key=hs.get)   
print(mk)     