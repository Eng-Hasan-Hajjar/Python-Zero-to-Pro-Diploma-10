student=["Yasamin","Kinda","Younes"]
print(student)
absent_student=list(("magd","zahraa","eric"))
print(absent_student)
accounts_zoom=["kinda","kinda"]
print(accounts_zoom)
shoping_list=["glass","chiken","coffe","breed","eggs","tee","sugar","watermellon"]
print(len(shoping_list))
ages=[23,18,60,27,33]
print(ages)
puzzeles=[True,False,True]
print(puzzeles)
print(type(puzzeles))
shoping_list=["glass","chiken","coffe","breed","eggs","tee","sugar","watermellon"]
print(shoping_list[1])
print(shoping_list[3])
print(shoping_list[-1])
print(shoping_list[7])

print(shoping_list[1:3])
print(shoping_list[:3])
print(shoping_list[:])

print(shoping_list[-3:-1])

##x="glass"
#x="chiken"
#x="coffe"
for x in shoping_list:
    print(x)
    print("**")

football=["AlNaser","AlNaser","glatsrai"," ","AlAHli_Hala"]    
print(football[2])
football[2]="Trabsun"
print(football[2])
print(football)
football[3:]=["Ispain","Brazil"]
print(football)



vision_board = [
    ["Learn Python", 40],
    ["Speak German B1", 75],
    ["Travel to Japan", 20],
    ["Build my own website", 90]
]

for goal in vision_board:
    if goal[1] >= 80:
        print(goal[0], "🚀 Almost done!")
    elif goal[1] >= 50:
        print(goal[0], "🔥 Good progress")
    else:
        print(goal[0], "🌱 Keep going")
        
        
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)



thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.append("kiwi")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


tropical.extend(thislist)
print(tropical)


li1=[1,2,3]
li2=[4,5,6]  

li1.extend(li2)
print(li1)


li2.extend(li1)
print(li2)      