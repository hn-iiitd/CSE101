import requests
n = int(input("Enter a number and know a fact \n"))
resp = requests.get("http://numbersapi.com/"+str(n))
print(resp.text)
print("")
k = input("Enter date in format DD/MM , to know a fact about it. \n")
resp = requests.get("http://numbersapi.com/"+str(k)+"/date")
print(resp.text)
print("")
k = input("Enter your pincode : ")
resp = requests.get('http://api.zippopotam.us/IN/' + str(k))
data = resp.json()
f = data["places"]
print("Places under this pincode are :")
for i in f:
    print(i["place name"])