import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def process(n,k,x):
    se=[]
    tup=()
    for i in range(1,k+1,1):
        if i != x:
            se.append(i)
    if len(se)  == 0:
        tup=("NO",)  
    else:
        hs=set(se)      
        if 1 in hs:
            b=[1]*n
            tup=("YES",n,b)  
        else:
            if 2 in hs and 3 not in hs:
                if n<2:
                    tup=("NO",)
                elif n%2==0:
                    q=n//2
                    b=[2]*q
                    tup=("YES",q,b)
                else:
                    tup=("NO",)    
            if 2 in hs and 3 in hs:
                if n<2:
                    tup=("NO",)
                elif n%2==0:
                    q=n//2
                    b=[2]*q
                    tup=("YES",q,b)
                else:
                    q=n//2
                    q=q-1
                    b=[2]*q
                    b.append(3)
                    tup=("YES",q+1,b)
    return tup                
                
                        


res=[]
for _ in range(ii()):
    n,k,x=mi()
    t=process(n,k,x)
    res.append(t)
    
for tup in res:
    print(tup[0])   
    if tup[0] == "YES":
        print(tup[1])
        print(*tup[2])
        
        