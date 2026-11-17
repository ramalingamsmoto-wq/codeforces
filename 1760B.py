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
    s=input()
    mx=max(s)
    v1=ord(mx)-ord('a')+1
    res.append(v1)
    
for e in res:
    print(e)    