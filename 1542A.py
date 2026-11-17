import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    ec=0
    oc=0
    for e in a:
        if e%2==0:
            ec=ec+1
        else:
            oc=oc+1   
    if ec==oc:
        res.append("Yes")  
    else:
        res.append("No")   

for e in res:
    print(e)                