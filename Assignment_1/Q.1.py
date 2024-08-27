def nump(n):
        d = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
        x = {10:"Ten",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred"}
        z = {11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:'Nineteen'}
        if (0<=n<=9):
                return d[n]
        elif(n%10==0):
                return x[n]
        elif(n//10 == 1):
                return z[n]
        else:
                f = (n//10)*10
                q = n-f
                return x[f] + ' ' + d[q]
def hund(n):
        return nump(n//100)+  ' Hundred ' + nump(n-(n//100)*100)
def thou(n):
        return nump(n//1000) + ' Thousand ' +hund(n- (n//1000)*1000 )
def lakh(n):
        return nump(n//100000) + ' Lakh ' +thou(n- (n//100000)*100000 )
def crore(n):
        return nump(n//10000000) + ' Crore ' + lakh(n- (n//10000000)*10000000 )

n = int(input())

if(0<=n<=99):
        x = nump(n)
if(100<=n<=999):
        x = hund(n)
if(1000<=n<=99999):
        x = thou(n)
if(100000<=n<=9999999):
        x = lakh(n)
if(1000000000>n>9999999):
        x = crore(n)
elif n>=1000000000:
       x =  "Number is out of range"
l = x.split(' ')
if(len(l)>2):  #for bonus questions
        i = 0
        while i < len(l)-1 :
                if l[i] == "Zero":
                        l.remove(l[i+1])
                        l.remove(l[i])
                else:
                        i = i+1
        if(l[len(l)-1] == "Zero"):
                l.remove(l[len(l)-1])
print(*l,sep = " ")