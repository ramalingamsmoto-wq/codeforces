

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(a):
    s=str(a)
    if len(s)<3:
        return "NO"
    fp=s[0]+s[1]
    fpi =int(fp)
    #print(f"fpin {fpi}")
    if fpi!=10:
        return "NO"
    else:
        sp=s[2:]    
        if sp[0]=='0':
            return "NO"
        else:
            spi=int(sp)    
            #print(f"spi {spi}")
            if spi>=2:
                return "YES"
                
    return "NO"            
                
res=[]
for _ in range(ii()):
    a=ii()
    t=process(a)
    res.append(t)
    
for e in res:
    print(e)    