from collections import Counter

def getIdx(item,a):
    for i in range(len(a)):
        if a[i]==item:
            return i+1
    return -1        

res=[]
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    counts=Counter(a)
    target_count = 1
    me = [item for item, count in counts.items() if count == target_count]
    idx=getIdx(me[0],a)
    res.append(idx)
    
for j in range(t):
    print(res[j])    