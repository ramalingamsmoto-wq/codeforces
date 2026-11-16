


class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        # 1-based indexing requires an array of size n + 1
        self.tree = [0] * (self.n + 1)

    def add(self, index: int, delta: int) -> None:
        """Add 'delta' to the element at 1-based 'index' and propagate upwards."""
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)  # Add rightmost set bit

    def prefix_sum(self, index: int) -> int:
        """Return the sum of elements from index 1 to 'index' (inclusive)."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)  # Subtract rightmost set bit
        return total

    def range_sum(self, left: int, right: int) -> int:
        """Return the sum of elements in the range [left, right] (1-based indices)."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


res=[]
for _ in range(int(input())):
    n,q=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    os=sum(a)
    bit = FenwickTree(n)
    for i, val in enumerate(a, start=1):
        bit.add(i, val)
    for _ in range(q):
        l,r,k=map(int,input().strip().split())
        cnt=r-l+1
        cs=bit.range_sum(l, r)
        v1=cnt*k
        v2=os-cs+v1
        if v2%2!=0:
            res.append("YES")
        else:
            res.append("NO")  
            
for e in res:
    print(e)              