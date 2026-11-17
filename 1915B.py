import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

list1=['A','B','C']
res=[]
for _ in range(ii()):
    ques=[]
    for i in range(3):
        q=si()
        q1 = [ord(char) - 64 if char.isalpha() else 0 for char in q]
        
        s=sum(q1)
        if s < 6:
            d=6-s
            ans=list1[d-1]
            res.append(ans)
            
for e in res:
    print(e)            
            

        