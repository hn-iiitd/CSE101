x0 = float(input("Enter x0: "))
def value(x):
    global p
    p = x**3 - 10.5*x**2 + 34.5*x - 35
    return p
def root(value,x):
    for i in range(1,102):
        if -0.2<=value(x)<=0.2:
            return(x)
        elif i == 101 and value(x)!=0:
            return("No root found, please try again with different value")
        else:
            m = 3*x**2 - 21*x + 34.5
            x = (m*x-p)/m 

        
print("one of the root of the equation is : " , root(value,x0))