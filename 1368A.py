import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def process(a,b,n):
    
    cnt=0
    
    while True:
        
        if a<=b:
            a=a+b
            cnt=cnt+1
            if a>n:
                break
        else:
            b=b+a 
            cnt=cnt+1   
            if b>n:
                break
    return cnt            
            
            
            

res=[]
for _ in range(ii()):
    a,b,n=mi()
    tans=process(a,b,n)
    res.append(tans)

for e in res:
    print(e)    
    