
import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def process(n,a):
    
    i=n-2
    while True:
        
        if i<0:
            break
            
        if a[i+1]%a[i]==0:
            a[i]=a[i]+1
            if a[i+1]%a[i]==0:
                a[i]=a[i]+1
            
        i=i-1
        
    return a    
                
             
        
    
    
res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    tans=process(n,a)
    res.append(tans)

for e in res:
    print(*e)