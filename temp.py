import sys

from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings



from decimal import Decimal

num = Decimal("-0")
print(num.is_signed())  # True

pos_num = Decimal("0")
print(pos_num.is_signed())  # False



