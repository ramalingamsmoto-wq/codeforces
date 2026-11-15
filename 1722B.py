

def update(n,s,us):
    for c in s:
        if c=='B' or c=='G':
            us.append('T')
        else:
            us.append(c)    
    
def process(n,a,b):
    ma=[]
    mb=[]
    update(n,a,ma)
    update(n,b,mb)
    for i in range(n):
        if ma[i]!=mb[i]:
            return "NO"
    return "YES"        
res=[]
for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    tans=process(n,a,b)
    res.append(tans)

for e in res:
    print(e)    
    