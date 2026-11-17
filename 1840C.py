import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def process(n,k,q,a):
    aux=[]
    
    i=0
    flag=False
    start=-1
    end=-1
    while True:
        if i>=n:
            if start != -1 and end!= -1:
                
                tup=(start,end)   
                aux.append(tup)  
                start=-1
                end=-1
                flag=False
            break
            
        if a[i] <=q and flag==False:
            start=i   
            flag=True
            
            
        if flag:
            if a[i]<=q:
                end=i
            else:
                tup=(start,end)   
                aux.append(tup)  
                start=-1
                end=-1
                flag=False
        i=i+1  
        
    ways=0
    #print(f"aux {aux}")
    for tup in aux:
        
        cnt=tup[1]-tup[0]+1
        if cnt>=k:
            v1=cnt-k+1
            v2=(v1*(v1+1))//2  
            ways+=v2  
            
    return ways        

res=[]
for _ in range(ii()):
    n,k,q=mi()
    a=li()
    tans=process(n,k,q,a)
    res.append(tans)
    
for e in res:
    print(e)    