allowance = 20000
sf = 0.1
r = 0.5
lc = int(input("Enter Laptop Cost: "))
def months(lc):
    global savings
    savings = 0
    global count
    count = 1
    savings = allowance*sf
    while savings<=lc:
        savings += savings*r/100
        savings += allowance*sf
        count+=1
        
    print("Total months required : ",count)
    print("Total Savings: ", savings)
    print("Savings left after purchase of laptop : " , savings-lc)

months(lc)



