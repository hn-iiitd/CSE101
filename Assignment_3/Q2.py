def sorted(a,filemain):
    final = []
    finalm = []
    f = open(a,'r')
    for line in f.readlines()[1:]:
        l = list(line.split(","))
        e = l[3].strip()
        final.append(e)
        finalm.append(str(line))
    for i in final:
        if "\n" not in i:
            i = i + "\n"
    final.sort()
    file = open(filemain,'w')
    f.close()
    file.write("TA, Crossing, Gate number, Time")
    file.write("\n")
    for i in final:
        if len(finalm)>0:
            for j in finalm:
                k = list(j.split(","))
                if i==k[3].strip():
                    file.write(j)
                    finalm.remove(j)
                    break
                else:
                    pass
        else:
            break
    file.close()
def input1(a):
    f = open(a,'r')
    d = {}
    for line in f.readlines()[1:]:
        l = list(line.split(","))
        e = {"gate no. " : 0 , "crossing_type": "",'time': " " }
        e['gate no.'] = l[2].strip()
        e['crossing_type'] = l[1].strip()
        e['time'] = l[3].strip()
        if l[0] not in d.keys():
            d[l[0].strip()] = [e]
        elif l[0].strip() in d.keys():
            h = d[l[0].strip()][len(d[l[0]])-1]['crossing_type'] 
            if h==l[1].strip():
                if h=='ENTER':
                    pass
                elif h=="EXIT":
                    d[l[0].strip()].pop(len(d[l[0].strip()])-1)
                    d[l[0].strip()].append(e)
            elif h!=l[1].strip():
                d[l[0].strip()].append(e)
    f.close()
    return d
def timechk(t1,t2):
    t1 = t1.replace(":","")
    t2 = t2.replace(":","")
    t1 = t1.replace(":","")
    t2 = t2.replace(":","")
    t1 = int(t1)
    t2 = int(t2)
    if t1>=t2:
        return True
    elif t1<t2:
        return False
def query1(d,b):
    name = input("Enter Name : ")
    f = open(b,'w')
    try:
        for i in d[name]:
            f.write(str((i['crossing_type'],i['time'])))
            f.write(" ")
    except KeyError:
        print("Incorrect Name")
    f.close()
    try:
        t1 = input('Enter Current Time in Format HH:MM:SS :  ')
        for i in d[name]:
            if timechk(t1,i['time']):
                x = i['time']
                v = i
            else:
                break
    except KeyError:
        print("Time Format is wrong, please write time in HH:MM:SS  format")
    if v['crossing_type'] == 'ENTER' :
        print('Present in Campus')
    elif v['crossing_type'] == 'EXIT':
        print("Not in Campus")
    else:
        print(v)
def query2(a,e):
    t1 = input("ENTER STARTING TIME(HH:MM:SS):  ")
    t2 = input("ENTER STOP TIME(HH:MM:SS):  ")
    f = open(a,'r')
    f1 = open(e,'w')
    f1.write("TA, Crossing, Gate number, Time \n")
    for line in f.readlines()[1:]:
        l = list(line.split(", "))
        if t2>l[3]>t1:
            f1.write(line)
    f.close()
    f1.close() 
def query3(d):
    x = input("Enter gate no. : ")
    count_enter = 0
    count_exit = 0
    for i in d:
        for j in d[i]:
            if j['gate no.'] == x and j['crossing_type']=="ENTER":
                count_enter +=1
            if j['gate no.'] == x and j['crossing_type']=="EXIT":
                count_exit +=1
    return count_enter,count_exit

a = 'sorted_data.txt'
filemain = 'sorted_final.txt'
sorted(a,filemain)
b = 'output.txt'
d = input1(filemain)
e = 'Output2.txt'
while a!="":
    print("\n")
    print("Enter 1 for Student's Data")
    print("Enter 2 for no. of studenta in a given time")
    print("Enter 3 to know students from gate")
    print("\n")
    try:
        u = int(input("Enter Choice : "))
        if u!=1 and u!=2 and u!=3:
            break
        if u==1:
            query1(d,b)
        if u==2:
            query2(filemain,e)
        if u==3:
            o,p = query3(d)
            print("No. of Enteries = ",o,"and No. of Exits",p)
    except UnboundLocalError:
        print("Incorrect Time")
    except ValueError:
        break