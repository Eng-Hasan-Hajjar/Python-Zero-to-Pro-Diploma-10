##lesson15


student={"name":"kinda","name":"yasamin","name":"magd"}
print(student)


student={"name":"kinda","name2":"yasamin","name3":"magd"}
print(student)
print(type(student))

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


print(cars["brand"])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(len(thisdict))


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#dictionary

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

y = thisdict.get("model")
print(x,y)


x = thisdict.keys()
print(x)

car = {
     "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


car = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change




car = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")



thisdict = { "brand": "Ford",  "model": "Mustang", "year": 1964}
thisdict["year"] = 2018


thisdict = {  "brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})


thisdict = {"brand": "Ford", "model": "Mustang",  "year": 1964}
thisdict["color"] = "red"
print(thisdict)


thisdict = { "brand": "Ford","model": "Mustang","year": 1964}
thisdict.pop("model")
print(thisdict)

thisdict = {  "brand": "Ford", "model": "Mustang",  "year": 1964}
thisdict.popitem()
print(thisdict)

thisdict = { "brand": "Ford","model": "Mustang","year": 1964}
del thisdict["model"]
print(thisdict)



thisdict = { "brand": "Ford",  "model": "Mustang",  "year": 1964}
thisdict.clear()
print(thisdict)


thisdict = { "brand": "Ford",  "model": "Mustang",  "year": 1964}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])



for x in thisdict.values():
  print(x)


for x in thisdict.keys():
  print(x)


for x in thisdict.items():
  print(x)

for x, y in thisdict.items():
  print(x, y)

thisdict = { "brand": "Ford",  "model": "Mustang", "year": 1964}
yasmin_dict = thisdict.copy()
print(yasmin_dict)



thisdict = { "brand": "Ford",  "model": "Mustang","year": 1964}
mydict = dict(thisdict)
print(mydict)




myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



child1 = { "name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias", "year" : 2007}
child3 = {"name" : "Linus",  "year" : 2011}
myfamily = {"child1" : child1,"child2" : child2, "child3" : child3}


print(myfamily["child2"]["name"])
print(myfamily["child3"]["year"])

print(myfamily["child2"])





# قاموس يحتوي على بيانات الطلاب
students={
    "student_1":{
        "name":"Ali Mohammad",
        "grade":90,
        "scores":{ "math": 95 , "science":85 , "English": 90   }
        },
    "student_2":{
        "name":"Ali Mohammad2",
        "grade":90,
        "scores":{ "math": 95 , "science":85 , "English": 90   }
        },
    "student_3":{
        "name":"Ali Mohammad3",
        "grade":90,
        "scores":{ "math": 95 , "science":85 , "English": 90   }
        }
}

print(students["student_1"]["scores"]["science"])

## طباعة كل معلومات الطالب
for student_id,student_info in students.items() :
    print("student ID:", student_id )
    print("Name:", student_info["name"] )
    print("Grade:", student_info["grade"] )
    for subject,score in  student_info["scores"].items():
        print(subject,score)

##الوصول الى درجة معينة
mark_english2=students["student_2"]
print(mark_english2)

mark_english2=students["student_2"]["scores"]
print(mark_english2)

mark_english2=students["student_2"]["scores"]["English"]
print(mark_english2)
