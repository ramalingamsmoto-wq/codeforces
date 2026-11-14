

def process(n,arr):
    is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    if not is_sorted:
        return 0
    else:
        v=[] 
        for i in range(1,n,1):
            v1=arr[i]-arr[i-1]
            v2=(v1//2)+1
            v.append(v2)   
    
    return min(v)
    


t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    tans=process(n,a)
    res.append(tans)
for e in res:
    print(e)    