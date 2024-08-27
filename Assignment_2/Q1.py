menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print("           Menu")
print("Item No.","  Item","    Price")
for i in range(1,len(menu)+1):
    print("   ",i,"   ",menu[i-1][0],(9-len(menu[i-1][0]))*" ",menu[i-1][1])
x  = "a"
cost = 0
item = 0
l = []
print("-------------Please Order------------")
while(x!="\n"):
    print("Enter:")
    x = list(map(int,input().split()))
    if len(x)==0 or len(x)==1:
        print("Thanks For Ordering!")
        break
    else:
        cost+=menu[x[0]-1][1]*x[1]
        item+=x[1]
        l.append([menu[x[0]-1][0],",", x[1],', Rs',menu[x[0]-1][1]*x[1]])
print("your bill is given below")
for i in l:
    for j in i:
        print(j,end=" ")
    print(" ")
print("TOTAL, ",item,"items,","Rs",cost)