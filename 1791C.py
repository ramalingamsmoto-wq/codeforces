

def process(n,s):
    il=[int(c) for c in s]
    i=0
    j=len(il)-1
    while i < j:
        if il[i] != il[j]:
            i=i+1
            j=j-1
        else:
            break    
    v=j-i+1
    return v        

t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    s=input()
    tans=process(n,s)
    res.append(tans)
for j in range(t):
    print(res[j])   