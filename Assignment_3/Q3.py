from random import randint as rd
n = int(input("Enter number of files : "))
output = open("file scores.txt","w")
for i in range(1,n+1):
    countsen = 0
    a = "FILE" + str(i) +".txt"
    rwords = []
    rdword = []
    f = open(a,'r')
    d = {}
    s = {}
    t = ["-",".",",",":",";",'..', '.,', '.:', '.;', ',.', ',,', ',:', ',;', ':.', ':,', '::', ':;', ';.', ';,', ';:', ';;',"\n","(",")"]
    for line in f.readlines():
        l = list(line.split(" "))
        for j in l:
            for k in t:
                while k in j:
                    j = j.replace(k,"")
            if j!="":
                j = j.lower()
                rwords.append(j)
                if j in d:
                    d[j]+=1
                elif j not in d:
                    d[j] = 1
    f.close()
    f = open(a,'r')
    sno = 0
    for line in f.readlines():
        p = list(line.split("."))
        for k in t :
            while k in p:
                p.remove(k)
        countsen+=len(p)
        for l1 in p:
            l1 = l1.strip()
            if l1!="":
                sno+=1
                l2 = l1.split(" ")
                s[sno] = len(l2)
    f.close()
    t = ['..', '.,', '.:', '.;', ',.', ',,', ',:', ',;', ':.', "--",':,', '::', ':;', ';.', ';,', ';:', ';;']
    f = open(a,'r')
    cons = 0
    for line in f.readlines():
        l = list(line.split(" "))
        for j in l:
            for k in t:
                if k in j:
                    cons+=1
                    break
    # print(cons)
    f.close()  
    twords = 0
    unique = len(d.keys())    #no.of.unique.words
    occ = []
    for i in d:
        twords+=d[i]
        occ.append(d[i])
    occ.sort()
    occ.reverse()
    occt = 0
    st = 0
    occcc = []
    if len(occ)>=5:
        occlen = 5
    else:
        occlen = len(occ)

    for i in range(occlen):
        occt+=occ[i]
        for j in d:
            if d[j] == occ[i] and j not in occcc:
                occcc.append(j)

    for i in s:
        if s[i]>35 or s[i]<5:
            st+=1
    try:
        for i in range(5):
            rtt = rd(0,twords-1)
            rdword.append(rwords[rtt])
    except ValueError:
        rdword.append("")
    # print(countsen)
    # print(st)
    try:
        F1 = unique/twords
        F2 = occt/twords
        F3 = st/countsen
        F4 = cons/twords
        if twords>750:
            F5 = 1
        elif twords<750:
            F5 = 0
        Tgrade = 4 + F1*6 + F2*6 -F3 - F4 - F5
        output.write(a+"\n")
        output.write('score: ' + str(Tgrade) +"\n")
        output.write("most used words : "+ str(occcc[:5]) + "\n")
        output.write("random words from submisson are: " + str(rdword) + "\n")  
        print("Report for",a,"generated successfully.")
    except ZeroDivisionError:
        print(a,"is Empty File")
        output.write(a+"\n")
        output.write('score: ' + str(0) +"\n")
        output.write("most used words : "+ str("Nil") + "\n")
        output.write("random words from submisson are: " + str("Nil") + "\n")  
print("\nReport for all Files saved successfully.")