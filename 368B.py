import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n,m=mi()
a=li()
suf=[0]*n

hs=set()

for i in range(n-1,-1,-1):
    hs.add(a[i])
    l=len(hs)
    suf[i]=l


res=[]
for i in range(m):
    qidx=ii()
    res.append(suf[qidx-1])
    
for e in res:
    print(e)    
    