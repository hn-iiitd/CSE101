x0 = 5
y0 = 5
x = 5
y = 5
z = 0
distance = ""
while distance!=0:
    distance = int(input("Enter value: "))
    if distance <= 0:
        break
    elif distance<=25 :
        y+=distance
    elif 25<distance<=50:
        y-=distance
    elif 50<distance<=75:
        x+=distance
    elif distance>=76:
        x-=distance
    z += distance
print("Final Coordinates: ","(",x,",",y,")")
print("Total Distance: ",z)
print("Displacement(Straight line distance): " ,((x - x0)**2 + (y-y0)**2)**0.5)

