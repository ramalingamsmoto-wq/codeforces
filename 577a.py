import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n,x=mi()

cnt=0
for i in range(1,n+1,1):
    if x%i==0 :
        q=x//i
        if q<=n:
            cnt=cnt+1
print(cnt)        