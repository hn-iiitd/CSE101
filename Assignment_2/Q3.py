def readfile(a,N):
    d = {}
    f = open(a,'r')
    i = 1
    for line in f:
        if (i-1)%(N)==0:
            q = line.split(":")
            d[q[0]]=0
        elif (i-1)%(N)!=0 :
            z = list(line.split(","))
            d[q[0]]+=int(z[1])
        else :
            pass
        i+=1
    f.close()
    return d
def counti(a):
    count = 0
    x = open(a,'r')
    for line in x:
        count+=1
    return count
a = 'Q3text.txt'
N = (counti(a))**0.5
d = readfile(a,N)
print(d)
print("Max Sign ")
x = 0
for i in d:
    if d[i] > x:
        x = d[i]
        y = i
for i in d:
    if d[i]==x:
        print(i,d[i])
print("\n")
print("Min Sign")
x = 100
for i in d:
    if d[i] < x:
        x = d[i]
        y = i
for i in d:
    if d[i]==x:
        print(i,d[i])