import sys
from operator import itemgetter

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



def getArea(points):
    points.sort(key=itemgetter(0, 1))
    
    
    d=points[1][1]-points[0][1]
    a=d*d
    return a
    
    
    
res=[]
for _ in range(ii()):
    points=[]
    for _ in range(4):
        x,y=mi()
        point=[x,y]
        points.append(point)
    a1=getArea(points)  
    res.append(a1) 

for e in res:
    print(e)     