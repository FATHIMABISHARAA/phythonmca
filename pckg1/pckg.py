from mypckg import mod1
from mypckg import mod2
from mypckg import mod3

m=int(input("enter the first number"))
n=int(input("enter the second number"))
s=mod1.sum(m,n)
print("sum",s)
avg=mod2.avg(m,n)
print("average",avg)
p1=mod3.power(m)
p2=mod3.power(n)
print("power of",m,"is",p1)
print("power of",n,"is",p2)
