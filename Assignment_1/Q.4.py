import math
a = int(input("Enter starting time: "))
b = int(input("Enter ending time: "))
t = a 
s = 0
def fnc(t):
    ln = math.log(140000/(140000-2100*t))
    return 2000*ln - 9.8*t
while t<b :
    v = fnc(t)*0.25
    t+=0.25
    l = fnc(t)*0.25
    s = s+ (v+l)/2

print("distance is:",s)

    

