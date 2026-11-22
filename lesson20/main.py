

class student:
    def __init__(self,name_new,age_new,avg_new):
        self.name=name_new
        self.age=age_new
        self.avg=avg_new
    def __str__(self):
        return f"{self.name}:{self.age}"
    def get_avg(self):
        return self.avg
    
class person:
    def __init__(self,name,nationality):
        self.name=name
        self.nationality=nationality
        
    
student1=student("magd",22,90)
student2=student("Kinda",16,92)
p1=person("Jamila","Syria")

print(student1.name,student1.age,student1.avg)
print(student2.name,student2.age,student2.avg)
print(p1.name,p1.nationality)
print(type(p1))   
print(type(5)) 
print(student1)
x=student1.get_avg()
print(x)

del student1.avg
    