

import math

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def get_prime_divisors(n):
  divisors = set()  # Use a list [] if you want repeated factors

  # Extract all factors of 2
  while n % 2 == 0:
    divisors.add(2)
    n //= 2

  # Check odd numbers up to sqrt(n)
  for i in range(3, int(math.isqrt(n)) + 1, 2):
    while n % i == 0:
      divisors.add(i)
      n //= i

  # If n is still greater than 2, the remaining n is prime
  if n > 2:
    divisors.add(n)

  return sorted(divisors)


#print(get_prime_divisors(60))  # Output: [2, 3, 5]
#print(get_prime_divisors(315))  # Output: [3, 5, 7]


n=ii()
cnt=0
for i in range(1,n+1,1):
    a=get_prime_divisors(i)
    if len(a)==2:
        cnt=cnt+1
        
print(cnt)        