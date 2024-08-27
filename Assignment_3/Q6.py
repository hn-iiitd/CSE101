#assuming maxm by own as not mentioned in assignment
#assuming max marks for cutoff if two have the same difference.
#assuming marks b/w 78 and 82 does not include 78&82
#assuming max marks by own by hardcoding, for now it is same as weightage of respective assignments but can be changed by changing the list of maxm.

import time 
def app1(N,inn,out):
    class Course:
        def __init__(self,cname,credits,assessments,gp,maxm):
            self.cname = cname
            self.credits = credits
            self.assessment = assessments
            self.gp = gp
            self.maxmm = maxm
        def getd(self):
            d = {"course-name":c.cname,"credits":c.credits,"assessment":c.assessment,"grading policy":c.gp,"Final Cutoff":q.getcutoff(),"No. of students with grades ":q.gradecount()}
            return d
        def assessmentssep(self):
            self.assessmentsssep = {}
            for i in list(c.assessment):
                c.assessmentsssep.__dict__[i[0]] = i[1]
            return self.assessmentssep
        def __str__(self):
            pass
    class Student(Course):
        def __init__(self,inn,out):
            Course.__init__(self,cname=c.cname,credits=c.credits,assessments=c.assessment,gp=c.gp,maxm=c.maxmm)
            self.fin = inn
            self.out = out
        def stored(self):
            final = {}
            finn= open(self.fin,'r')
            for line in finn:
                q = list(line.split(","))
                self.rollno = q[0].strip()
                upd = {}
                for i in range(len(c.assessment)):
                    if i==len(c.assessment)-1:
                        if "\n" in q[i+1]:
                            q[i+1] = q[i+1].replace("\n","")
                    upd[c.assessment[i][0]] = q[i+1]
                final[q[0].strip()]  = upd
            finn.close()
            self.final = final
            return self.final
        def getcutoff(self):
            cut = []
            marks = []
            final = q.marksc()
            for i in final:
                marks.append(final[i]['Total Score'])
            marks.sort()
            marks.reverse()
            for i in c.gp:
                r = []
                for j in marks:
                    if i+2>j>i-2:
                        r.append(j)
                r.sort()
                diff = 0
                if len(r)<=1:
                    cut.append(i)
                elif len(r)>1:
                    for e in range(len(r)-1):
                        if r[e+1] - r[e] >=diff:
                            diff = r[e+1] - r[e]
                            ter1 = r[e+1]
                            ter2 = r[e]
                    cut.append((ter1+ter2)/2)
            return cut
        def grading(self,t):
            cut = q.getcutoff()
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
        def finalgrading(self):
            final = q.marksc()
            for j in final:
                final[j]['Grade'] = q.grading(final[j]['Total Score'])
            return final
        def gradecount(self):
            final  = q.finalgrading()
            d = {}
            for i in final:
                if final[i]["Grade"] not in d:
                    d[final[i]["Grade"]] = 1
                else:
                    d[final[i]["Grade"]]+=1
            return d
        def marksc(self):
            final = q.stored()
            for j in final:
                T = 0
                for i in range(len(c.assessment)):
                    bbb = float(final[j][c.assessment[i][0]])
                    T+=(bbb/c.maxmm[i])*c.assessment[i][1]
                final[j]['Total Score'] = T
            return final
        def upload(self):
            final = q.finalgrading()
            f = open(self.out,'w')
            for i in final:
                f.write(i)
                f.write(",")
                f.write(str(final[i]['Total Score']))
                f.write(",")
                f.write(str(final[i]['Grade']))
                f.write('\n')
            f.close()
            return "Task Successfull"
        def showm(self,roll):
            final = q.finalgrading()
            for i in final:
                if roll ==i:
                    return final[i]
                    break

    policy = [80, 65, 50, 40]
    assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
    maxm = [30,15,30,25]
    c = Course("IP",4,assessments,policy,maxm)

    q = Student(inn,out)


    while True:
        print('Enter 1 for summary')
        print('Enter 2 for uploading grade')
        print('Enter 3 for searching for a student')
        o = input("Enter Choice: ")
        if o== "" or o=="\n":
            break
        o = int(o)
        if o == 1:
            print(c.getd())
        if o == 2:
            start = time.time()
            for imp in range(N):
                print(q.upload())
            end = time.time()
            print("For grading",end-start)
        if o ==3:
            start = time.time()
            for n in range(2022001,2022060,1):
                print(n,q.showm(str(n)))
            end = time.time()
            print("For searching",end-start)
def app2(N,inn,out):
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
    while True:
        print('Enter 1 for summary')
        print('Enter 2 for grading')
        print('Enter 3 for searching for a student')
        o = input("Enter Choice: ")
        if o== "" or o=="\n":
            break
        o = int(o)
        if o == 1:
            print(getd(cname,credits,assessments,policy,finalcutoff,gradecount))
        if o == 2:
            start = time.time()
            for imppppp in range(N):
                print(upload(out,marksc,stored))
            end = time.time()
            print(end - start)
        if o ==3:
            start = time.time()
            for n in range(2022001,2022060):
                print(n,showm(str(n),marksc,stored))
            end = time.time()
            print(end - start)
N = 1
inn = "q6_data_in.txt"
out= "q6_student_data_out.txt"
while True:
    a = input("Enter Number:")
    if a=="\n" or "":
        break
    a = int(a)
    if a==1:
        app1(N,inn,out)
    if a==2:
        app2(N,inn,out)


