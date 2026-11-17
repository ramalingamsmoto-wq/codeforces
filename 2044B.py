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
    s=si()
    rs=s[::-1]
    ans=""
    for c in rs:
        if c=='p':
            ans+='q'
        elif c=='q':
            ans+='p'  
        else:
            ans+=c    
    res.append(ans)
    
for e in res:
    print(e)    