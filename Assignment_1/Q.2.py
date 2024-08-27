M = int(input("M: "))

#assembly
x1 = assembly_labhrs_tab = 8
y1 = assembly_labhrs_chair = 2
z1 = assembly_max_labhrs = 400
#Finishing
x2 = finishing_labhrs_tab = 2
y2 = finishing_labhrs_chair = 1
z2 = finishing_max_labhrs = 120

p = max_profit = 0
for chair in range(1,41):
    for tab in range(1,41):
        if (tab*x1 + chair*y1 <= z1) and (tab*x2 + chair*y2 <= z2):
            if tab<M:
                profit_tab = tab*90
            elif tab>=M:
                profit_tab = M*90 + (tab-M)*100
            if chair<M:
                profit_chair = chair*25
            elif chair>= M:
                profit_chair = M*25 + (chair-M)*30
            z = profit_chair + profit_tab
            if z>p:
                treq = tab
                creq = chair
                p = z
print(treq ," tables are required and ",creq , " chairs are required for maximum profit of ","$",z)

            

    






