import math
a = 10  
b = 1.05
c = 1
d = 1.06
p = 1.0
e = math.e
def demand(p):
    return e**(a- b*p)
def supply(p):
    return e**(c+ d*p)
flag = True
while flag:
    if demand(p) <= supply(p):
        break
    else:
        p +=p*5/100
        pass
print("Equilibrium price: ",p)
print("Demand: ",demand(p))
print("Supply: ",supply(p))



