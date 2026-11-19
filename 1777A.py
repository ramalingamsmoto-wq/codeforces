import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,a):
    cnt=0
    i=0
    while True:
        l=len(a)
        if i>=l:
            break
        if i+1<l:
            fe=a[i]    
            se=a[i+1]
            
            fep=fe&1
            sep=se&1
            
            if fep==sep:
                a.pop(i+1)
                a.pop(i)
                a.insert(i,(fe*se))
                i=max(0,i-1)
                cnt=cnt+1
            else:
                i=i+1    
        else:
            break    
    return cnt
        
res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    tans=process(n,a)
    res.append(tans)
    
for e in res:
    print(e)    