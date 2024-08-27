fm = []
matrix = m =  []
N = int(input("N: ")) #no. or rows
for i in range(N):
    print("Enter x,y")
    l = []
    l = list(map(int,input().split(",")))
    m.append(tuple(l))
print("Tuples: ",m)
for i in m:
    l = []
    for j in i:
        l.append(j)
    l.append(1)
    fm.append(l)
print("order of matrix formed is :",N,"X",3)
print("matrix is")
for i in fm:
    print(i)
print("2nd Matrix is: ")
B = [["cx", 0, 0],  
     [0, "cy", 0],  
     [0, 0, 1]] 
for i in B:
    print(i)
cx = int(input("cx: "))
cy = int(input("cy: "))  
B = [[cx, 0, 0],  
     [0, cy, 0],  
     [0, 0, 1]] 
multi = []
print("The final shape is:\n ",)
for i in range(N):
    l = []
    for j in range(3):
        l.append(0)
    multi.append(l) 
for i in range(len(fm)):    
   for j in range(len(B[0])):    
          for k in range(len(B)):    
               multi[i][j] += (fm[i][k])*(B[k][j])
for i in multi:
    print(i[0:2])