thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)



thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)



thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset.discard("banana")
print(thisset)



thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)



thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
myset = set1.union(set2, set3)
print(myset)




set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
myset = set1 | set2 | set3
print(myset)




set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)      

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple", "cherry"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z= x.symmetric_difference(y)
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z= x ^ y
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)


x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x <= y #z = x.issubset(y)
print(z)


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
