n=input()
s=input()

ac=0
dc=0

for i, c in enumerate(s):
    if c=='A':
        ac+=1
    else:
        dc+=1    
if ac < dc:
    print("Danik")
elif dc < ac:
    print("Anton")  
else:
    print("Friendship")          