
def getC(c,direction):
    LHK=[]
    LHK.append("qwert")
    LHK.append("asdfg")
    LHK.append("zxcvb")
    
    print(f"lhk {LHK}")
    
    for i in range(0,3):
        j=LHK[i].find(c)
        if  j!= -1:
            if direction=='R':
                return LHK[i][j-1]
            else:
                return LHK[i][j+1]    
        
    RHK=[]
    RHK.append("poiuy")
    RHK.append(";lkjh")
    RHK.append("/.,mn")
    
    print(f"rhk {RHK}")
    
    for i in range(0,3):
        j=RHK[i].find(c)
        if  j!= -1:
            if direction=='R':
                return RHK[i][j+1]
            else:
                return RHK[i][j-1]  
    
    
    
    
    
    

direction=input()
s=input()
rs=""

for c in s:
    us=getC(c,direction)
    rs=rs+us
    
print(rs)    