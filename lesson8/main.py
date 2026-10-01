## bool 
## true   false       python
## 1      0           c++

print(20>3)
print(20<3)
print(20==3)

##avg2=input("enter your grade!")
avg=60
if avg>65:
    print("congratulations for IT!")
    print("congratulations for siencs!")
else:
    print("we are sorry! ")    


print(bool("lesson8"))
print(bool(50))
print(bool(""))
print(bool(0))
print(bool(" "))
print(bool("0"))

print(["hasan","hassan","hosien"])
print(bool(["hasan","hassan","hosien"]))

print(bool([]))

print(bool(()))
print(bool({}))


def getmark():
    avg=input("enter your rate: ")
    avg=int(avg)
    if avg>65:
        return True
    else:
        return False
    
print(getmark())    