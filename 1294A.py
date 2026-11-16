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
    a,b,c,n=mi()
    list1=[a,b,c]
    list1.sort()
    mn=(list1[2]-list1[0])+ (list1[2]- list1[1])
    if n < mn:
        res.append("NO")
    else:
        rem=n-mn
        if rem%3==0:
            res.append("YES") 
        else:
            res.append("NO")  

for e in res:
    print(e)                 