import math

def fast_sieve(n=1_000_000):
    if n < 2:
        return []
    if n == 2:
        return [2]

    
    size = (n - 1) // 2
    sieve = bytearray([1]) * (size + 1)
    sieve[0] = 0  # 1 is not prime

    limit = int(math.isqrt(n))
    for i in range(1, (limit - 1) // 2 + 1):
        if sieve[i]:
            p = 2 * i + 1
            # Start marking from p*p; its index in the odd-only array is (p*p - 1) // 2
            start = (p * p - 1) // 2
            # Step by p in the odd-only array (which corresponds to 2*p in actual numbers)
            sieve[start::p] = bytearray((size - start) // p + 1)

    # Reconstruct the prime numbers
    return [2] + [2 * i + 1 for i, is_prime in enumerate(sieve) if is_prime]

# Example usage:
primes = fast_sieve(1_000_001)
#print(f"Found {len(primes)} primes. Largest: {primes[-1]}")
# Output: Found 78498 primes. Largest: 999983



n=int(input())

v1=-1
v2=-1

hs=set(primes) 
for i in range(2,n,1):
    if i not in hs:
        v1=i
        v2=n-v1
        if v2 not in hs:
            break
            
            
print(f"{v1} {v2}")        
