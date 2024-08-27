wts = [(10, 7.5), (25, 30), (10, 7.5), (50, 55)]
def grades(i):
    if 100>=i>=80:
        return("A")
    elif 80>i>=70:
        return("A-")
    elif 70>i>=60:
        return("B")
    elif 60>i>=50:
        return("B-")
    elif 50>i>=35:
        return("C")
    elif 30<=i<35:
        return("C-")
    elif i<30:
        return("F")
    elif i>100 :
        return("Wrong Marks Entered")
f = open("IPmarks.txt","r")
f2 = open("IPgrades.txt","w")
for line in f:
    s = 0
    l = list(line.split(","))
    for i in range(len(l[1:])):
        s+= round(int(l[i+1])*(wts[i][1]/wts[i][0]),2)
    f2.write(l[0])
    f2.write(" ")
    f2.write(str(s))
    f2.write(" ")
    f2.write(grades(s))
    f2.write("\n")
f.close()
f2.close()
