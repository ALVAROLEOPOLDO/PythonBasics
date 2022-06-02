numberList= list((1,2,3,4))
print(numberList)

r=list(range(1,10))
print(r)

colors=["red", "green"]
print("green" in colors)
colors[1]="yellow" 
print(colors)

colors.append("violet")
print(colors)

#colors.extend=(["blue","black"])
#print(colors)

colors.insert(1, "blue")
print(colors)

colors.pop()
print(colors)

colors.remove("blue")
print(colors)

colors.sort()