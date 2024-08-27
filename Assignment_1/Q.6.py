n = int(input())
def pattern(n):
    star = "*"
    space = " "
    for i in range(1, n + 1):
        print(star*i + space*(2*n - 2*i) + star*i)

pattern(n)