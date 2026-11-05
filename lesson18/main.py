def get_name():
    print("kinda - interrupt enternet")
    
get_name()    


def get_name_student(name):
    print(f"{name} - interrupt enternet")
    
get_name_student("kinda")    



def get_full_name_student(fname,lname):
    print(f"{fname} ,{lname} - interrupt enternet")
    
get_full_name_student("kinda","Ahmad")    


def family(*members) :
    print("the family constst of :",members[0],members[2],members[3],members[1])

family("father","mother","shadi","eric")

def family2(child1,child2,child3):
    print(child1)
    
#family2(child1="younes") 
family2(child1="younes",child2="ahmad",child3="hasan") 

def skils(skill1,skill2) :
    print(skill1)  
    
skils(skill1="react",skill2="java script")    


def languages(lang1="Arabic"):
    print("i can speak:"+lang1)
    
languages("English")
languages()    


def clubs(names):
    for x in names:
        print(x)
        
clubs_list=["real madrid","catalonia","portugal"]
clubs(clubs_list)        


def add(x,y):
    return x + y

z=add(2,3)
print(z)
print(add(6,8))


def div(a,b):
    if b != 0:
        return a/b
    else:
        return "nan"
    
f=div(20,0)  
h=div(10,2)  
print(f,h)


def mul(a,b):
    return a*b

def sub(a,b):
    return a-b
def add(x,y):
    return x + y


def div(a,b):
    if b != 0:
        return a/b
    else:
        return "nan"

def menu():
    print("choose your choice:")
    print("1 add:")
    print("2 sub:")
    print("3 mul:")
    print("4 div:")
    print("5 exit.")
    
def main(choice,a,b):
       if choice == "1":
           print(add(a,b))
       elif choice == "2":
           print(sub(a,b))   
       elif choice == "3":
           print(mul(a,b)) 
       elif choice == "4":
           print(div(a,b)) 
       else :
           print("nothig")       
           
print("choose your operation:")   
menu()
choice=input("your choice:")
number1=int(input("number1:"))
number2=int(input("number2:"))
main(choice,number1,number2)    

