
import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,k):
    if n%2==0 and k%2==0:
        return "YES"
    elif n%2!=0 and k%2!=0:
        return "YES"  
    else:
        no_odd=0
        if n%2!=0:
            no_odd=(n//2)+1
        else:
            no_odd=n//2    
        if k<=no_odd:
            return "YES"   
        return "NO"    
        
res=[]
for _ in range(ii()):
    n,k=mi()
    
    tans=process(n,k)
    res.append(tans)

for e in res:
    print(e)    
        