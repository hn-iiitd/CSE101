N = int(input("Enter No. of top pages:-"))
u = 'pages.txt'
f = open(u,'r')
count = 0 #no. of urls in one line
q = []
d = {}
for line in f:               #creating a dictionary
      l = line.split(',')
      d[l[0]] = ["",0,"",""]
f.close()
f = open(u,'r')
for line in f:
  l = line.split(',')
  t = l[0]
  z = open(u,'r')
  for line in z:
    count = 0
    r = line.split(":")
    v = r[0].split(",")
    q = [v[0]]
    for j in d:
        if j in line and j not in q:   #counting no. of urls
              q.append(j)
              count+=1
        else:
              pass
    q.remove(v[0])
    d[v[0]][2] = q
    d[t][0] = l[1][:4]
    imp = float(v[1])/count     #importance of each link
    d[v[0]][3] = imp
    if t in r[1]:
      d[t][1] += round(imp,4)
  z.close()
f.close()
im = []
ur = []
for i in d:
      im.append(d[i][1])
      ur.append(i)
im.sort()
im.reverse()
count = 1
for j in im:
      for i in d:
            if d[i][1] == j and i in ur:
                  if(count<=N):
                        ur.remove(i)
                        print(count,":",i,d[i])
                        count+=1
                  elif count>N:
                        break