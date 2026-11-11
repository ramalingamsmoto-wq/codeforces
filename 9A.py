from fractions import Fraction

y,w=map(int,input().strip().split())
mx=max(y,w)
total=6
dot=total-mx+1

f=Fraction(dot,total)


if mx==1:
    print("1/1")
else:
    print(f)