

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def process(n,p):
    pre=[0]*n
    prei=[0]*n
    
    suf=[0]*n
    sufi=[0]*n
    
    pre[0]=p[0]
    prei[0]=0
    for i in range(1,n,1):
        pre[i]=min(pre[i-1],p[i])
        if pre[i]==p[i]:
            prei[i]=i
        else:
            prei[i]=prei[i-1]   
            
    suf[n-1]=p[n-1] 
    sufi[n-1]=n-1
    for i in range(n-2,-1,-1):
        suf[i]=min(suf[i+1],p[i])
        if suf[i]==p[i]:
            sufi[i]=i
        else:
            sufi[i]=sufi[i+1]    
    a=-1
    b=-1
    c=-1
    found=False        
    for i in range(1,n-1,1):
        if pre[i-1]<p[i]>suf[i+1]:
            a=prei[i-1] +1  
            b=i+1
            c=sufi[i+1] +1
            found=True 
            break
            
    if found:
        l1=["YES",a,b,c]    
        return l1
    else:
        l1=["NO"]   
        return l1     



res=[]
for _ in range(ii()):
    n=ii()
    p=li()
    t=process(n,p)
    res.append(t)
    
    
for list1 in res:
    print(list1[0])    
    if list1[0]=="YES":
        print(f"{list1[1]} {list1[2]} {list1[3]}")