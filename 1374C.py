

def process(n,s):
    stack = []
    cnt=0
    for c in s:
        if c=='(':
            stack.append(c)
        else:
            if len(stack) ==0:
                cnt=cnt+1   
            else:
                stack.pop()
                
    cnt=cnt+len(stack)      
    cnt=cnt//2
    return cnt      
                    
    

t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    s=input()
    tans=process(n,s)
    res.append(tans)
    
for e in res:
    print(e)    