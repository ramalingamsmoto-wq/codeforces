

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n):
    sl=2*n
    rows, cols = sl,sl
    grid = [['n' for _ in range(cols)] for _ in range(rows)]
    #print(f"{grid}")
    
    cnt=0
    for i in range(0,2*n,2):
        if cnt%2==0:
            start='#'
            sec='.'
        else:
            start='.'    
            sec='#'
        startrow=i
        add_row=i+1   
        
        for j in range(0,n,1):
            k=j*2
            if j%2==0:
                grid[startrow][k]=start
                grid[startrow][k+1]=start
                grid[add_row][k]=start
                grid[add_row][k+1]=start
            else:
                grid[startrow][k]=sec
                grid[startrow][k+1]=sec
                grid[add_row][k]=sec
                grid[add_row][k+1]=sec
        cnt=cnt+1            
                
    result = ["".join(row) for row in grid]  
    for row in result:
        print(row)        
    
       
            
        

    

for _ in range(ii()):
    n=ii()
    process(n)
    