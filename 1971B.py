
import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

res=[]
for _ in range(ii()):
    s=si()
    s=list(s)
    fc=s[0]
    l=len(s)
    idx=-1
    for i in range(1,l,1):
        if s[i]!=fc:
            idx=i
            break
    if idx==-1:
        tup=("NO",)    
        res.append(tup)
    else:
        
        s[0]=s[idx]
        s[idx]=fc
        s="".join(s)
        tup=("YES",s)
        res.append(tup)

for tup in res:
    print(tup[0])   
    if tup[0] =="YES":
        print(tup[1])