import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

n,m=mi()
cnt=n
while True:
    q=n//m
    r=n%m
    
    if q==0:
        break
    cnt=cnt+q
    n=n//m   
    n=n+r
    
print(cnt)     