a=[1,2,3,4,5]
k=3
l=len(a)
for i in range(l-1,0,-1):
    print(f"i {i}",end='')
    j=i-1
    tgt=i-k
    v1=a[i]
    while j>=0 and j>=tgt:
        a[j]=a[j]+v1
        print(f" j {j}",end='')
        j=j-1
        
    print(f"a {a}")    
    print("\n\n")    
print(f"osum {sum(a)}")        