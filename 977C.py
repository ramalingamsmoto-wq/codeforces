


import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def process(n,k,a):
    if n<k:
        return -1
    a.sort()    
    if k == 0:
        if a[0] > 1:
            return 1
        else:
            return -1
    v1=a[k-1]
    if k<n:
        if a[k]==a[k-1]:
            return -1
        else:
            return v1    
    elif k==n:
        return v1
    
        
n,k=mi()
a=li()
t=process(n,k,a)
print(t)
    