

def process(a,n):
    a.sort()
    
    
    for i in range(1,len(a),1):
        exp1=a[i-1]+1
        exp2=a[i-1]
        if a[i]!=exp1 and a[i] != exp2:
            return "NO"
            
    return "YES"        
            
    
    
            
            


t=int(input())


res=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    
    tans=process(a,n)
    res.append(tans)
    
for j in range(t):
    print(res[j])    