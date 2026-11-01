a = 2
b = 330
print("A") if a > b else print("B")

if a > b: print("a is greater than b")

"""

if a > b :
    print("A") 
else:
    print("B")
    
    
"""
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

if a>b:
    print("A")
elif a==b:
    print("=")
else :
    print("B")        

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 5
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
    print("new instrucion")    


eric=100
if eric>=50:
    print("good")
    if eric>=90:
        print("exellent")
    else:
        print("very good")    


a = b = 33
if b > a:
  pass




i = 1
while i < 6:
  print(i)
  i += 1

i = 10
while i < 6:
  print(i)
  i += 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")




fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)
  print("Mgd")



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):
  print(x)


for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

