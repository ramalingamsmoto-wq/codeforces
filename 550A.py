

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings




def process(s):
    #first way
    idx1=s.find("AB")
    if idx1!=-1:
        idx2=s.find("BA",idx1+2)
        if idx2!=-1:
            return "YES"
    
    #Sec way
    idx1=s.find("BA")
    if idx1!=-1:
        idx2=s.find("AB",idx1+2)
        if idx2!=-1:
            return "YES"
    
    return "NO"        
            
        
s=si()
t=process(s)
print(t)