import sys
from collections import Counter
import math


# --- Pure Bytes Input ---
rb = sys.stdin.buffer.readline
ii = lambda: int(rb())                        # Single integer
mi = lambda: map(int, rb().split())           # Multiple integers
li = lambda: list(map(int, rb().split()))     # List of integers
sb = lambda: rb().rstrip()                    # Raw bytes string (e.g., b'abc')
lb = lambda: rb().split()                     # List of raw bytes strings
ms = lambda: map(str, rb().split()) 

# --- Pure Bytes Output ---
out = bytearray()
pr = lambda x: out.extend(b'%d\n' % x)        # Append single integer as bytes
ps = lambda b: out.extend(b + b'\n')          # Append raw bytes line
pa = lambda a: out.extend(b' '.join(b'%d' % x for x in a) + b'\n') # Append int list
flush = lambda: sys.stdout.buffer.write(out)  # Write raw bytes in one syscall

def all_equal_all(lst):
    return all(x == lst[0] for x in lst) if lst else True
    

def process(n,a):
    tup=()
    if n==1:
        tup=("YES",a)
    if n>=2:
        if all_equal_all(a):
            tup=("NO",)
        else: 
            a.sort(reverse=True)
            #print(f"a12 {a}")
            
            flag=False
            s=a[0]
            for i in range(1,n,1):
                if s==a[i]:
                    flag=True
                    break
                s=s+a[i]    
            if flag:
                temp=a[0]
                a[0]=a[n-1]
                a[n-1]=temp
            #print(f"a123 {a}")    
                
            tup=("YES",a)
    return tup        

res=[]        
for _ in range(ii()):
    n=ii()
    a=li()
    tup=process(n,a)
    res.append(tup)
    
for tup in res:
    print(tup[0])    
    if (tup[0]== "YES"):
        print(*tup[1])
    
    