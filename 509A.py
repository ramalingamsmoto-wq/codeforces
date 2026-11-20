


import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def process(n):
    mx=-1
    rows, cols = n+1,n+1
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            if i==1 or j==1:
                grid[i][j]=1
                mx=max(mx,grid[i][j])
                
    #print(f"grid {grid}")
    
    for i in range(2,n+1,1):
        for j in range(2,n+1,1):
            grid[i][j]=grid[i-1][j]+grid[i][j-1]
            mx=max(mx,grid[i][j])

    #print(f"grid {grid}")
    return mx


n=ii()
t=process(n)
print(t)