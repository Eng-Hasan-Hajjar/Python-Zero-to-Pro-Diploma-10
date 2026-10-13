
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
fruits=["apple","orange","kiwi"]
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
fruits=["apple","orange","kiwi","banana"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "Eric" for x in fruits]
print(newlist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23 , 1]
thislist.sort(key = myfunc,reverse=True)
print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry2"]
mylist = thislist.copy()
#mylist = thislist
print(mylist)

thislist = ["apple", "banana", "cherry26"]
print(mylist)



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
#for x in list2:
 # list1.append(x)
list1.append(list2) 
print(list1)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))
print(len(thistuple))

for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


thistuple = ["apple"]
print(type(thistuple))

thistuple = ("apple",)
print(type(thistuple))



tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thistuple)


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi")
print(thistuple[2:5])



thistuple = ("apple", "orange", "kiwi", "melon")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "kiwi")
print(thistuple[2:])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi")
print(thistuple[-4:-1])



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



x = ("apple", "banana", "cherry")


y = list(x)
y[1] = "kiwi"


x = tuple(y)

print(x)



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)




thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
