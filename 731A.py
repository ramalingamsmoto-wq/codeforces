import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


alphab="abcdefghijklmnopqrstuvwxyz"
map=alphab+alphab+alphab
def gc(currc,tgtc):
    pos = map.index(currc, map.index(currc) + 1)
    
    fwdidx=map.index(tgtc,pos)
    fwdm=fwdidx-pos
    revidx=map.rfind(tgtc,0,pos)
    revm=pos-revidx
    ans=min(fwdm,revm)
    return ans
    
    
s=si()
n=len(s)
cnt=0
for i in range(n):
    if i==0:
        cnt+=gc('a',s[i])
    else:
        cnt+=gc(s[i-1],s[i])  
          
print(cnt)    