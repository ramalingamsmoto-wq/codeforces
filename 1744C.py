import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def process(n,c,s):
    map=s+s
    suf=[0]*n
    b=[]
    
    
    if s[n-1]=='g':
        suf[n-1]=0
    else:
        gidx=map.find('g',n-1)    
        tt=gidx-n+1
        suf[n-1]=tt
        
    
    for i in range(n-2,-1,-1):
        if s[i]=='g':
            suf[i]=0
        else:
            suf[i]=suf[i+1]+1
            
    mx=-1        
    for i in range(n):
        if s[i]==c:
            mx=max(mx,suf[i])
    return mx            
            
    
            
   # print(f" b {b}")        
    
        
res=[]
for _ in range(ii()):
    ns,c=ls()
    n=int(ns)
    s=si()
    tans=process(n,c,s)
    res.append(tans)
    
for e in res:
    print(e)    