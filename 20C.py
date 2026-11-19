import sys
import heapq
from dataclasses import dataclass

# Fast I/O using buffered byte reading
input = sys.stdin.buffer.readline
mi = lambda: map(int, input().split())

n, m = mi()

nodes = []
limit = 2**70

@dataclass
class Node:
    __slots__ = ("cid", "df1", "prev", "nb", "nbd")
    cid: int
    df1: int
    prev: int
    nb: list
    nbd: list

    def __lt__(self, other):
        return self.df1 < other.df1

for i in range(n + 1):
    node = Node(i, limit, -2, [], [])
    nodes.append(node)

# Fixed: explicitly accessing index 1 of the nodes list
start_node = nodes[1]
start_node.df1 = 0
start_node.prev = -1

for _ in range(m):
    a, b, w = mi()
    nodes[a].nb.append(b)
    nodes[a].nbd.append(w)

    nodes[b].nb.append(a)
    nodes[b].nbd.append(w)

q = []
heapq.heappush(q, (0, 1))

while len(q) > 0:
    d, top = heapq.heappop(q)

    

    nbl = len(nodes[top].nb)
    for i in range(nbl):
        nid = nodes[top].nb[i]
        v1 = d + nodes[top].nbd[i]
        if v1 < nodes[nid].df1:
            nodes[nid].df1 = v1
            nodes[nid].prev = top
            heapq.heappush(q, (v1, nid))

if nodes[n].df1 == limit:
    sys.stdout.write("-1\n")
else:
    list1 = [n]
    while True:
        left = list1[-1]
        prev = nodes[left].prev
        if prev == -1:
            break
        list1.append(prev)

    list1.reverse()
    sys.stdout.write(" ".join(map(str, list1)) + "\n")
    