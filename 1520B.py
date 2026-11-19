import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


onos=[]
for l in range(1,11,1):
    for i in range(1,10,1):
        v1=str(i)*l
        onos.append(int(v1))
        
onos.sort()  
#print(len(onos))   
#print(*onos)    

l=len(onos)        
res=[]
for _ in range(ii()):
    n=ii()
    cnt=0
    for e in onos:
        if e<=n:
            cnt=cnt+1
        else:
            break    
    res.append(cnt)        
    
for e in res:
    print(e)    
    