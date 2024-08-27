import random
import requests
def chkword(z): #check if string is valid
    Flag = False
    c = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + z
    resp = requests.get(c)
    if len(z)==5 and resp.status_code == 200  :
        Flag = True
    return Flag
def random_word(five): #generate random word
    j = random.randint(0,len(five))
    str = five[j]
    str = str.lower()
    return str
five  =['Alter','Apply','Argue','Arise','Avoid', 'Begin','Blame','Break','Bring','Build','Burst','Carry','Catch','Cause','Check','Claim','Clean','Clear','Climb','Close','Count','Cover','Cross','Dance','Doubt','Drink','Drive','Enjoy','Enter','Exist','Fight','Focus','Force','Guess','Imply','Issue','Judge','Laugh','Learn','Leave','Limit','Marry','Match','Occur','Offer','Order','Phone','Place','Point','Press','Prove','Raise','Reach','Refer','Relax','Serve','Shall','Share','Shift','Shoot','Sleep','Solve','Sound','Speak','Spend','Split','Stand','Start','State','Stick','Study','Teach','Thank','Think','Throw','Touch','Train','Treat','Trust','Visit','Voice','Waste','Watch','Worry','Would','Write']
str = random_word(five)
l = ["-","-","-","-","-"] #with -----
k = list(str)
i = 0
print("Guess the word","                ",6-i,"chances remaining ","\n")
print("Enter a Word with five letters")
print(*l,sep=" ")
while i<=6 or z!=str:
    if i==6:
        break
    q = []
    z = input("Enter Word: ")
    z.lower()
    flag = True
    if(chkword(z)):
        for w in range(5):
            y = ""
            if z[w] == str[w]:
                l[w] = z[w]
            elif (z[w] != str[w]) and (z[w] in str) and (z[w] != l[w]):
                q.append(z[w])
            for u in l:
                y= y+ u
            if y==str:
                flag = False
                break
        if(flag):
            i+=1
            q = list(set(q))
            print("Wrong guess ,Try again!","       ",6-i,"chances remaining ","\n")
            print("Guess the word \n",*l)
            print("letters present: ", *q,sep = " ")
            print("")
        if i==6:
            print("maximum chances exceeded")
            break
        if(not flag):
            print("Congratulations you have guessed the word right")
            break
    else:
        print("You have not entered a valid word, please try again!","       ",6-i,"chances remaining ","\n")
        print("Guess the word \n",*l)
print("The Word is",str)          