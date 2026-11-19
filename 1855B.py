import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def process(n):
    cnt=0
    for i in range(1,n+1,1):
        if n%i==0:
            cnt=cnt+1
        else:
            break
    return cnt
                
r=[]
for _ in range(ii()):
    n=ii()
    t=process(n)
    r.append(t)
    
for e in r:
    print(e)    