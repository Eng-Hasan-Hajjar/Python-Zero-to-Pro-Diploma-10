#string  - str - سلسلة نصة
x = "awesome"

def myfunc():
  print("Python is " + x)
  
myfunc()


student="Eric"
def get_name():
    print("hello")
    print(student)
    
print("in main program") 

get_name()   



def welcome(name):
    print("Hello " + name)

welcome("Yunus")
welcome("Ahmad")
welcome("Hasan")


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)



#################################
x = "kida"
def myfunc():
  x = "Salma"
  print("Python is " + x)
  
myfunc()

print("Python is " + x)

myfunc()
print("Python is " + x)
####################################
x = "kida"
def myfunc():
  global x 
  x = "Salma"
  print("Python is " + x)
 
print("Python is " + x)  
myfunc()
print("Python is " + x)
##############################

x = "Hello World"
#display x:
print(x)
#display the data type of x:
print(type(x))
#####
x = 20
#display x:
print(x)
#display the data type of x:
print(type(x)) 

######

x = 20.5
#display x:
print(x)
#display the data type of x:
print(type(x))
#######

x = 2+1j
#display x:
print(x)
#display the data type of x:
print(type(x))


x = 1j
#display x:
print(x)
#display the data type of x:
print(type(x))

########
x = 2+1j        # مثالك
print(x)        # (2+1j)

a = 3+0j        # 3 حقيقي بس مكتوب كعقدي
b = 0+5j        # 5j تخيلي صافي
c = -2-3j       # سالب
d = 1.5+2.5j    # عشري عقدي

print(type(b))
print(type(c))
print(type(d))
print(type(a))  # <class 'complex'>

x = ["apple", "banana", "cherry"]
#display x:
print(x)
#display the data type of x:
print(type(x)) 
