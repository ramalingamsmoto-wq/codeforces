

def process(a,b):
    delta=0
    if a < b:
        delta=b-a
    else:
        delta=a-b
    if delta==0:
        return 0
    else:
        q=delta//10
        rem=delta%10
        if rem!=0:
            q=q+1
            
        return q        
            
                        

t=int(input())
res=[]
for _ in range(t):
    a,b=map(int,input().strip().split())
    tans=process(a,b)
    res.append(tans)
for s in res:
    print(s)    