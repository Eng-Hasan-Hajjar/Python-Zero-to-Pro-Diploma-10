##inherentance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname,id):
        Person.__init__(self, fname, lname)
        self.id=id

class Employee(Person):
    def __init__(self, fname, lname,salary):
       Person.__init__(self, fname, lname)
       self.salary=salary
    def printname(self):
       print(self.firstname, self.lastname,self.salary)
   
S = Student("Mike", "Olsen",3)
S.printname()

E = Employee("Mike emp", "Olsen",500)
E.printname()





##polymorphism   
x="hello classes"
print(len(x))
y=("kinda","yasmin","magd")
print(len(y))
y=["kinda","yasmin","magd"]
print(len(y))
y={"kinda","yasmin","magd"}
print(len(y))

##ex:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


