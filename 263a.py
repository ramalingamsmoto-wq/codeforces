
mat=[]
mat.append([-1,-1,-1,-1,-1])
for i in range(1,6,1):
    a=list(map(int,input().strip().split()))
    a.insert(0,-1)
    mat.append(a)
ci=-1
cj=-1   
for i in range(1,6,1):
    for j in range(1,6,1):
        if mat[i][j]==1:
            ci=i
            cj=j
            break

#print(f" mat {mat}")
#print(f"ci {ci} cj {cj}")
ans=abs(ci-3)+abs(cj-3) 
print(ans)        