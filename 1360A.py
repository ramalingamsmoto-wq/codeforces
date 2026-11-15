


def process(a,b):
    
    
    area1=0
    area2=0
    #case1
    length=a+a
    breadth=b
    if length >=breadth:
        area1=length*length
    else:
        area1=breadth*breadth
        
    #print(f"area1 {area1}")    
    #case2
    length=b+b
    breadth=a
    if  length >= breadth:
        area2=length*length
           
    else:
        area2=breadth*breadth
        
   # print(f"area2 {area2}")     
        
    return min(area1,area2)    
        
    
    
res=[]
for _ in range(int(input())):
    a,b=map(int,input().strip().split())
    tans=process(a,b)
    res.append(tans)
for e in res:
    print(e)