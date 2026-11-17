import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

ml=[8,4,2,6]
n=ii()
if n==0:
    print(1)
else:
    mv=n%4
    mv=mv-1
    print(ml[mv])    