order=[
      1,11,111,1111,
      2,22,222,2222,
      3,33,333,3333,
      4,44,444,4444,
      5,55,555,5555,
      6,66,666,6666,
      7,77,777,7777,
      8,88,888,8888,
      9,99,999,9999]
res=[]      
for _ in range(int(input())):
    x=int(input())
    ol=0
    for e in order:
        cl=len(str(e))
        ol=ol+cl
        if e==x:
            break 
    res.append(ol)  
for e in res:
    print(e)               