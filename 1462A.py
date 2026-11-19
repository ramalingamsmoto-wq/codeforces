import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def process(n,b):
    left=0
    right=n-1
    a=[]
    while left <=right:
        if left==right:
            a.append(b[left])
            break
        else:
            a.append(b[left])  
            a.append(b[right]) 
        left=left+1
        right=right-1    
    return a    
 
res=[] 

for _ in range(ii()):
    n=ii()
    b=li()
    t=process(n,b)
    res.append(t)
    
for list1 in res:
    print(*list1)    