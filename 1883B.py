
from collections import Counter

def isPalindrome(counts):
    even_count = sum(1 for v in counts.values() if v % 2 == 0)
    odd_count = sum(1 for v in counts.values() if v % 2 != 0)
    
    l=len(counts.values())
    if l==even_count or (even_count==l-1 and odd_count==1):
        return "YES"
    else:
        return "NO"    

    

def process(n,k,s):
    counts=Counter(s)
    odd_count = sum(1 for v in counts.values() if v % 2 != 0)
    if k==odd_count-1 or k==odd_count:
        return "YES"
    elif k>=odd_count-1:   
        nk1=k-odd_count+1
        nk2=k-odd_count
        
        if nk1%2==0 or nk2%2==0:
            return "YES"
         
    return "NO"    
        
    
    
    
    



res=[]
for _ in range(int(input())):
    n,k=map(int,input().strip().split())
    s=input()
    tans=process(n,k,s)
    res.append(tans)
    
for e in res:
    print(e)    