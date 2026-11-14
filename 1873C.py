sb =[[1,1,1,1,1,1,1,1,1,1],
     [1,2,2,2,2,2,2,2,2,1],
     [1,2,3,3,3,3,3,3,2,1],
     [1,2,3,4,4,4,4,3,2,1],
     [1,2,3,4,5,5,4,3,2,1],
     [1,2,3,4,5,5,4,3,2,1],
     [1,2,3,4,4,4,4,3,2,1],
     [1,2,3,3,3,3,3,3,2,1],
     [1,2,2,2,2,2,2,2,2,1],
     [1,1,1,1,1,1,1,1,1,1]]
 
def gs(chart):
    score=0
    for i in range(10):
        for j in range(10):
            if chart[i][j]=='X':
                score+=sb[i][j]
                
    return score
             
t=int(input()) 
res=[]
for i in range(t):
    chart=[]
    for j in range(10):
        temp=input()
        chart.append(temp)
    tans=gs(chart)
    res.append(tans)    
        
for j in range(t):
    print(res[j])   