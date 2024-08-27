def pattern(a,b,n,x):
    if n//2 ==1:
        return a*(n//2) + b*(x-n) + a*(n//2)
    else:
        return a*(n//2) + b*(x-(n)) + a*(n//2) +"\n" + pattern(a,b,n-2,x)
def pattern2(a,b,n,x):
    if n==x:
        return a*(n//2) + b*(x-n) + a*(n//2)
    else:
        return a*(n//2) + b*(x-(n)) + a*(n//2) +"\n" + pattern2(a,b,n+2,x)
a = "* "
b = "  "
n = int(input("Enter n: "))
n = n*2 
x = n
print(pattern(a,b,n,x))
n = 4
print(pattern2(a,b,n,x))