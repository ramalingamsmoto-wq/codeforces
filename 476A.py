import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n,m=mi()
minl=-1
maxl=-1

if n%2==0:
    q=n//2
    minl=q
    maxl=n
else:
    q=n//2
    minl=q+1
    maxl=n
    
ans=-1 
for i in range(minl,maxl+1,1):
    if i%m==0:
        ans=i
        break
        
print(ans)        
    