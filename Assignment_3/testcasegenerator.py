import random
a = "q6_data_in.txt"
f = open(a,'w')
n = 2022000
for i in range(1001):
    n+=1
    a_1 = random.randint(5,30)
    a_2 = random.randint(4,15)
    a_3 = random.randint(3,30)
    a_4 = random.randint(6,25)
    f.write(str(n))
    f.write(",")
    f.write(str(a_1))
    f.write(",")
    f.write(str(a_2))
    f.write(",")
    f.write(str(a_3))
    f.write(",")   
    f.write(str(a_4))
    f.write("\n")
f.close()
