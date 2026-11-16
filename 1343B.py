
def process(n):
    q=n//2
    tup=()
    if q%2!=0:
        tup=("NO",)
        return tup
        
        
    a=[]    
    for i in range(1,q+1,1):
        a.append(i*2)
        
    b=[]
    i=1
    cnt=0
    while True:
        if cnt>=q-1:
            break
        b.append(i)   
        i=i+2 
        cnt=cnt+1
    #print(f"b {b} a {a}")    
        
    as1=sum(a)  
    bs1=sum(b)  
    e=as1-bs1
    b.append(e)
    a.extend(b)
    tup=("YES",a)
    return tup

res=[]
for _ in range(int(input())):
    n=int(input())
    tans=process(n)
    res.append(tans)
    
    
for tup in res:
    rs=tup[0]    
    if rs=="NO":
        print(rs)
    else:
        print(rs) 
        a=tup[1]
        print(*a)
        
           