#bonus Question
#education loan repayment duration calculator.
a = int(input("Total Fees for Program : "))
d = float(input("Annual Interest Rate : "))
f = int(input("Total duration of program,max = 4 : "))

print("The fees is payable semester wise or yearly?")
print("enter 'y' for yearly"," 's' for semesterly")
m = input()
if m == 's':
    each_sem_fees = c = a/(2*f)
    e= 0
    for i in range(1,12*f + 1):
        if i==1 or i==7 or i==13 or i==19 or i==25 or i==31 or i==37 or i==43:
            e+= c
        e = e + e*d/1200
    print("Amount of loan pending: ",e)
elif m == 'y':
    each_year_fees = c = a/(f)
    e= 0
    for i in range(1,12*f + 1):
        if i==1 or i==13 or i==25 or i==37:
            e+= c
        e = e + e*d/1200
    print("Amount of loan pending: ",e)

#calculating months to repay the loan
base = int(input("Enter In hand salary per month "))
expenses = int(input("Expenses /month: "))
savings = base - expenses

#assuming max years to repay loan is 15 years (SBI) after graduating
flag = True
for y in range(1,16):
    for i in range(1,13):
        e = e - savings
        if e <= 0 :
            print("Loan will be paid in",y,"years and" , i, "months.")
            break
        e = e + e*d/1200
    if e<= 0 :
        flag = False
        break
if(flag):
    print("Sorry, you will not be able to pay the loan on time.")