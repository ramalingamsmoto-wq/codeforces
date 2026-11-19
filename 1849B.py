import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


import heapq

def process(n,k,a):
    
    max_heap = []
    order=[]
    for idx, val in enumerate(a):
        
        v1=val%k
        if v1==0:
            v1=k
        heapq.heappush(max_heap, (-v1, idx+1))
    
    while True:
        
        if len(order)==n:
            break
        neg_val, sidx = heapq.heappop(max_heap)
        max_val = -neg_val
        
        nmax_val=max_val-k
        if nmax_val <=0:
            order.append(sidx)
        else:
            heapq.heappush(max_heap, (-nmax_val, sidx))
    return order            
        
    
    
    
    
    
    


res=[]
for _ in range(ii()):
    n,k=mi()
    a=li()
    t=process(n,k,a)
    res.append(t)

for list1 in res:
    print(*list1)    