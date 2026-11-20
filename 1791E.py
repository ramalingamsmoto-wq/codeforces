

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def update(n,a,start,end):
    ec=end-start+1
    if ec%2==0:
        for i in range(start,end+1,1):
            a[i]=-a[i]
    else:
        c=[]
        print(f"start {start} end{end}")
        for i in range(start,end+1,1):
            c.append(-a[i])
        print(f"c {c}")    
        mn=min(c)  
        flag=False  
        for i in range(start,end+1,1):
            if a[i]==-mn and flag==False:
                flag=True
            else:
                a[i]=-a[i]
        print(f"a {a}")        
        if start-1 >=0:
            if a[start]<0:
                if a[start-1]< -a[start]:
                    a[start-1] =-a[start-1]
                    a[start]=-a[start]
        if end+1<n:
            if a[end]<0:
                if a[end+1] < -a[end]:
                    a[end+1] =-a[end+1]
                    a[end]=-a[end]
        print(f"a {a}")                   
            
        


def process(n,a):
    
    i=0
    started=False
    start=-1
    end=-1
    while True:
        
        if i==n:
            started=False
            if start!=-1 and end!=-1:
                update(n,a,start,end)
                start=-1
                end=-1
            break
            
        
        if a[i]<0 and started==False:
            started=True
            start=i
            print(f"start in process {start}")
        if started:
            if a[i]  <=0:
                end=i  
                print(f" end in process {end}")
            if a[i]>0:
                started=False
                print(f"start,end in pro {start} {end}")
                update(n,a,start,end)
                start=-1
                end=-1
        i=i+1    
    s=sum(a)
    return s
    
                       
                    
                    

res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    t=process(n,a)
    res.append(t)
    
for e in res:
    print(e)    