import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

#return list of tuples (start,end,count) inclusive
def gs(n,k,s):
    segs=[]
    start=-1
    end=-1
    i=0
    started=False
    while True:
        
        if i>=n:
            if start != -1 and end !=-1:
            
                tup=(start,end,end-start+1) 
                segs.append(tup) 
                started=False
                start=-1
                end=-1
            break
            
        if s[i]  == 'B' and started==False:
            start=i
            started=True
            
        if started:
            if s[i] == 'B':
                end=i  
            else:
                tup=(start,end,end-start+1) 
                segs.append(tup) 
                started=False
                start=-1
                end=-1
        i=i+1          
    return segs    
    
    
def process(n,k,s):
    bsegs=gs(n,k,s)
    costs=[]
    left=0
    right=0
    
    cnt=0
    i=0
    # using 2 pointers costs contain all costs
    #getting min(costs)is the ans
    # using 2 pointers to get all the costs
    


for _ in range(ii()):
    n,k=mi()
    s=si()
    t=process(n,k,s)
    res.append(t)

for e in res:
    print(e)    
    