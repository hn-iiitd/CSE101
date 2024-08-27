def popul(i,r,t):
    while t!=0:
        i= i + i*(r/100)
        t = t-1
        r = r-0.1
    return i
pop = [50, 1450, 1400, 1700, 1500, 600, 1200] #given
d = sum(pop)
print("Current population of world: ",d,"Million")
for years in range(0,40):
    e = 0
    r = 2.5
    for i in pop:
        z=popul(i,r,years)
        e+=z
        r = r-0.4
    if e>=d:
        d = e
        y = years 
    else:
        break
    
print("Max population is: ",d,"Million")
print("Years needed to reach max population is: ",y)