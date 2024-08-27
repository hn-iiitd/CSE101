def tan(x):
    x = (3.14/180)*x
    return(x + (x**3)/3 + 2*(x**5)/15 + 17*(x**7)/315 )
angle = float(input("Enter value of angle in degrees: "))
if 0<=angle<90:
    b = float(input("Enter distance to the base of the pole: "))
    h = b*tan(angle)
    print("height of pole is : ",h)
    print("distance to top of the poll : ", (h**2 + b**2)**0.5)
else:
    print("Invalid Input")
