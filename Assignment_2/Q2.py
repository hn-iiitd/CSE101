def course_no(d):
    flag = True
    if(flag):
        if len(d[0]) != 6 :
            flag = False
    if(flag):
        A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        N = '1234567890'
        for i in range(5):
            if d[0][i].isalpha():
                if d[0][i] not in list(A):
                    flag = False
                    break
        if(flag):
            if d[0][0] not in list(A) or d[0][5] not in list(N):
                flag = False    
    return flag
def credit(d):
    flag = True
    l = d[1]
    if l!='2' and l!='4' and l!='1':
        flag = False
    return flag
d = " "
l ={}
a = 0
b = 0
c = 0
sgp={"A+":10 , "A":10, "A-":9, "B":8, "B-":7, "C":6, "C-":5, "D":4, "F":2}
while(d!=""):
    flag = True
    print("Enter Course Name, Credit, Grade")
    d = input().split()
    if len(d)==0:
        break
    if not course_no(d):
        print("Improper Course Number")
        flag = False
    if not credit(d):
        print("Incorrect Credit")
        flag = False
    if d[2] not in sgp.keys():
        print("Incorrect Grade")
        flag = False
    if(flag):
        l[d[0]] =   int(d[1]),d[2]
    if(not flag):
        print("Sorry, input ignored")
z = []
s = {}
for i in l.keys():
    z.append(i)
z.sort()
for i in z:
    s[i] = l[i]
for i in s:
    print(i,":",s[i][1])
for i in l:
    a+=l[i][0]*sgp[l[i][1]]
    b+=l[i][0]
print("SGPA: ",a/b)