#assuming maxm by own as not mentioned in assignment
#assuming max marks for cutoff if two have the same difference.
#assuming marks b/w 78 and 82 does not include 78&82
#assuming max marks by own by hardcoding, for now it is same as weightage of respective assignments but can be changed by changing the list of maxm.
def getd(cname,credits,assessments,policy,finalcutoff,gradecount):
    d = {"course-name":cname,"credits":credits,"assessment":assessments,"grading":policy,"Final Cutoff":finalcutoff(marksc,stored,inn,policy),"No. of students with grades ":gradecount(marksc,finalgrading,stored)}
    return d
def assessmentssep(assessments):
    assessmentsssep = {}
    for i in list(assessments):
        assessmentsssep[i[0]] = i[1]
    return assessmentssep
def stored(inn):
    final = {}
    finn= open(inn,'r')
    for line in finn:
        q = list(line.split(","))
        upd = {}
        for i in range(len(assessments)):
            if i==len(assessments)-1:
                if "\n" in q[i+1]:
                    q[i+1] = q[i+1].replace("\n","")
            upd[assessments[i][0]] = q[i+1]
        final[q[0].strip()]  = upd
    finn.close()
    return final
def finalcutoff(marksc,stored,inn,policy):
    cut = []
    marks = []
    final = marksc(stored,inn)
    for i in final:
        marks.append(final[i]['Total Score'])
    marks.sort()
    for i in policy:
        r = []
        for j in marks:
            if i+2>j>i-2:
                r.append(j)
        r.sort()
        diff = 0
        if len(r)<=1:
            cut.append(i)
        else:
            for e in range(len(r)-1):
                if r[e+1] - r[e] >=diff:
                    diff = r[e+1] - r[e]
                    ter1 = r[e+1]
                    ter2 = r[e]
            cut.append((ter1+ter2)/2)
    return cut
def grading(t,finalcutoff,marksc,stored,inn,policy):
    cut = finalcutoff(marksc,stored,inn,policy)
    if t>=cut[0]:
        grade = "A"
    if cut[1]<=t<cut[0]:
        grade = "B"
    if cut[2]<=t<cut[1]:
        grade = "C"
    if cut[3]<=t<cut[2]:
        grade = "D"
    if t<cut[3]:
        grade = "F"
    return grade
def finalgrading(marksc,stored):
    final = marksc(stored,inn)
    for j in final:
        final[j]['Grade'] = grading(final[j]['Total Score'],finalcutoff,marksc,stored,inn,policy)
    return final
def gradecount(marksc,finalgrading,stored):
    final  = finalgrading(marksc,stored)
    d = {}
    for i in final:
        if final[i]["Grade"] not in d:
            d[final[i]["Grade"]] = 1
        else:
            d[final[i]["Grade"]]+=1 
    return d
def marksc(stored,inn):
    final = stored(inn)
    for j in final:
        T = 0
        for i in range(len(assessments)):
            bbb = float(final[j][assessments[i][0]])
            T+=(bbb/maxm[i])*assessments[i][1]
        final[j]['Total Score'] = T
    return final
def upload(out,marksc,stored):
    final = finalgrading(marksc,stored)
    f = open(out,'w')
    for i in final:
        f.write(i)
        f.write(",")
        f.write(str(final[i]['Total Score']))
        f.write(",")
        f.write(str(final[i]['Grade']))
        f.write('\n')
    f.close()
    return "Task Successfull"
def showm(roll,marksc,stored):
    final = finalgrading(marksc,stored)
    for i in final:
        if roll ==i:
            return final[i]
            break
cname = "IP"
credits=4
policy = [80, 65, 50, 40]
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
maxm = [30,15,30,25]
inn = "student_data_in.txt"
out= "student_data_out2.txt"
while True:
    print('Enter 1 for summary')
    print('Enter 2 for uploading grade')
    print('Enter 3 for searching for a student')
    o = input("Enter Choice: ")
    if o== "" or o=="\n":
        break
    o = int(o)
    if o == 1:
        print(getd(cname,credits,assessments,policy,finalcutoff,gradecount))
    if o == 2:
        print(upload(out,marksc,stored))
    if o ==3:
        n = input("Enter Roll no : ")
        print(showm(n,marksc,stored))
    