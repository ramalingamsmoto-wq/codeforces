
import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


k=ii()
a=li()
a.sort(reverse=True)

i=0
s=0
cnt=0
found=False
l=len(a)
while True:
    
    if i>=l:
        break
        
    if s>=k:
        found=True
        break    
    
    s=s+a[i]
    cnt=cnt+1
    
    if s>=k:
        found=True
        break   
    
    
    i=i+1    
    
if found:
    print(cnt)  
else:
    print(-1)      