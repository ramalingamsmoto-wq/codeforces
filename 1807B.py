import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,a):
    es=0
    os=0
    for e in a:
        if e%2==0:
            es=es+e
        else:
            os=os+e
            
    if es> os:
        return "YES"   
    else:
        return "NO"             
res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    tans=process(n,a)
    res.append(tans)

for e in res:
    print(e)    