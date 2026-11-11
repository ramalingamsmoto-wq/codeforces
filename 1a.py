import math


n,m,a=map(int,input().strip().split())
rc=n/a
rc=math.ceil(rc)

cc=m/a
cc=math.ceil(cc)

ans=rc*cc
print(ans)
