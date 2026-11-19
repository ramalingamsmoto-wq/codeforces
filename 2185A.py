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
    a=[]
    for i in range(1,n+1,1):
        a.append(i)
    res.append(a)   

for list1 in res:
    print(*list1)     
    