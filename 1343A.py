import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

powof2=[]
for i in range(70):
    v1=(2**i)
    powof2.append(v1)
    
aux=[powof2[0]]   
for i in range(1,70):
    v1=aux[i-1]+powof2[i]
    aux.append(v1)
    
def process(n):
    ans=-1
    for e in aux:
        if e!=1:
            if n%e==0:
                ans=(n//e)
                break
    return ans                

res=[]
for _ in range(ii()):
    n=ii()
    t=process(n)
    res.append(t)
    
for e in res:
    print(e)    