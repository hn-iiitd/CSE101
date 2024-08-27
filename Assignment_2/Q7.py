def exit():  #exit
    return "\n Program ended successsfully \n"
def new(a):  #new
    n = input("Enter Name\n")
    z = {'address':"" ,'phone': "", 'email':"",}
    z['address'] = input("Enter Address\n")
    z['phone'] = input("Enter phone no.\n")
    z['email'] = input("Enter email id\n")
    x = open(a,'r')
    d = eval(x.readline())
    x.close()
    if n in d:
        if type(d[n]) == list:
            d[n].append(z)
        elif type(d[n])==dict:
            l = []
            ex = d[n]
            l.append(ex)
            l.append(z)
            d[n] = l
        y = open(a,'w')
        y.write(str(d))
        y.close()
    else:
        y = open(a,'w')
        d[n] = z
        y.write(str(d))
        y.close()
    return("New Name Added Successfully\n")
def partial(a,par): #search from partial
    flag = False
    x = open(a,"r")
    d = eval(x.readline())
    for i in d:
        if par in i: 
            print(i,d[i])
            flag = True
    if(not flag):
        print("No Name found\n") 
    x.close()
def find(a,emphn):  #search from phn no.
    flag = False
    x = open(a,"r")
    d = eval(x.readline())
    for i in d:
        if type(d[i]) == list:
            for j in d[i]:
                if j["email"] == emphn or j["phone"] == emphn:
                    flag = True
                    print(i,j) 
        elif type(d[i]) == dict:    
            if d[i]["email"] == emphn or d[i]["phone"] == emphn:
                flag = True
                print(i,d[i])
    if(not flag):
        print("No Entry found with this email or mobile")
    x.close()
def dele(a,nam):    #delete
    newD = {}
    l = []
    x = open(a,'r')
    d = eval(x.readline())
    for i in d:
        if i != nam:
            newD[i] = d[i]
    x.close()
    x = open(a,'w')
    x.write(str(newD))
    x.close()
    print("Done Successfully \n")
def fileempty(a):  #check if file is empty
    count = 0
    x = open(a,'r')
    for line in x:
        count+=1
    x.close()
    return count
def merge(a,nam): #bonus
    x = open(a,'r')
    y = open(nam,'r')
    d1 = eval(x.readline())
    d2 = eval(y.readline())
    x.close()
    y.close()
    for i in d2:
        flag = True
        if i in d1:
            if type(d1[i]) == list and type(d2[i])== list:
                for j in range(len(d1[i])):
                    for k in range(len(d2[i])):
                        if d1[i][j]['address'] == d2[i][k]['address'] and d1[i][j]['email'] == d2[i][k]['email'] and d1[i][j]['phone'] == d2[i][k]['phone']:
                            flag = False
            elif type(d1[i]) == list and type(d2[i]) == dict:
                for j in range(len(d1[i])):
                    if d1[i][j]['address'] == d2[i]['address'] and d1[i][j]['email'] == d2[i]['email'] and d1[i][j]['phone'] == d2[i]['phone']:
                        flag = False
            elif type(d1[i]) == dict and type(d2[i]) == list:
                for j in range(len(d2[i])):
                    if d2[i][j]['address'] == d1[i]['address'] and d2[i][j]['email'] == d1[i]['email'] and d2[i][j]['phone'] == d1[i]['phone']:
                        flag = False
            elif type(d1[i])==dict and type(d2[i]) == dict:
                if d1[i]['address'] == d2[i]['address'] and d1[i]['email'] == d2[i]['email'] and d1[i]['phone'] == d2[i]['phone']:
                    flag = False
            if(flag):
                if type(d1[i]) == list and type(d2[i])== list:
                    d1[i].extend(d2[i])
                elif type(d1[i]) == list and type(d2[i]) == dict:
                    d1[i].append(d2[i])
                elif type(d1[i]) == dict and type(d2[i]) == list:
                    d2[i].append(d1[i])
                    d1[i] = d2[i]
                elif type(d1[i])==dict and type(d2[i]) == dict:
                    l = []
                    ex = d1[i]
                    l.append(ex)
                    l.append(d2[i])
                    d1[i] = l
                y = open(a,'w')
                y.write(str(d1))
                y.close()
        else:
            y = open(a,'w')
            d1[i] = d2[i]
            y.write(str(d1))
            y.close()


a = 'addrbook.txt'
b = ""
while b!=0:  #loop
    print("0 - To exit")
    print("1 - To insert a new entry")
    print("2 - To find an entry with partial name")
    print("3 - To find an entry with email or phone no.")
    print("4 - To view the addressbook")
    print("5 - To delete an entry")
    print("6 - To merge the dictionary")
    b = int(input("Enter Value : "))
    if b==0:
        print(exit())
    if b==2:
        par =  input("input : ")
        partial(a,par)
    if b==1:
        if fileempty(a) ==0:
            x = open(a,'w')
            x.write('{}')
            x.close()
        print(new(a))
    if b==3:
        emphn = input("Enter : ")
        find(a,emphn)
    if b==4:
        x = open(a,"r")
        for line in x:
            print(line)
    if b==5:
        nam = input("Enter name of the entry : ")
        dele(a,nam)
    if b==6:
        nam = input("Enter file name : ")
        merge(a,nam)