class LazySegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _push(self, node, start, end):
        # Push pending updates down to children
        if self.lazy[node] != 0:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            # Update children's values based on their segment lengths
            self.tree[left_child] += self.lazy[node] * (mid - start + 1)
            self.tree[right_child] += self.lazy[node] * (end - mid)

            # Pass the lazy value down
            self.lazy[left_child] += self.lazy[node]
            self.lazy[right_child] += self.lazy[node]

            # Clear current node's lazy value
            self.lazy[node] = 0

    def update_range(self, l, r, val):
        """Adds 'val' to all elements in range [l, r] (0-indexed, inclusive)."""
        self._update_range(1, 0, self.n - 1, l, r, val)

    def _update_range(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            self.tree[node] += val * (end - start + 1)
            self.lazy[node] += val
            return

        self._push(node, start, end)
        mid = (start + end) // 2
        self._update_range(2 * node, start, mid, l, r, val)
        self._update_range(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query_sum(self, l, r):
        """Returns the sum of elements in range [l, r] (0-indexed, inclusive)."""
        return self._query_sum(1, 0, self.n - 1, l, r)

    def _query_sum(self, node, start, end, l, r):
        if l > end or r < start:
            return 0
        if l <= start and end <= r:
            return self.tree[node]

        self._push(node, start, end)
        mid = (start + end) // 2
        left_sum = self._query_sum(2 * node, start, mid, l, r)
        right_sum = self._query_sum(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum

    def query_point(self, idx):
        """Returns the exact value at index 'idx'."""
        return self.query_sum(idx, idx)





t=int(input())
res=[]
for _ in range(t):
    n,k=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    st = LazySegmentTree(a)
    l=len(a)
    for i in range(l-1,0,-1):
        v1=st.query_point(i)
        st.update_range(max(0,i-k),i-1,v1)
    s=st.query_sum(0,l-1)
    if s%2 ==0:
        res.append("Bob")
    else:
        res.append("Alice")
        
for e in res:
    print(e)            
        
    
    
    

