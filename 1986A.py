import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def distancebetween(i,x1,x2,x3):
    d1=abs(i-x1)
    d2=abs(i-x2)
    d3=abs(i-x3)
    d=d1+d2+d3
    return d
    
def process(x1,x2,x3):
    min1=min(x1,x2,x3)
    max1=max(x1,x2,x3)
    
    limit=2**70
    mn=limit
    
    for i in range(min1,max1+1,1):
        d=distancebetween(i,x1,x2,x3)
        mn=min(mn,d)
        
    return mn    
    
res=[]    
for _ in range(ii()):
    x1,x2,x3=mi()
    t=process(x1,x2,x3)
    res.append(t)

for e in res:
    print(e)    
    