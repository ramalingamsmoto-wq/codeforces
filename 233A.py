import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n=ii()
if n%2!=0:
    print(-1)
else:
    b=[]  
    i=1
    while True:  
        if len(b)==n:
            break
        b.append(i+1)
        b.append(i)
        i=i+2
    print(*b)    