class Player:
    def __init__(self,name,health=100):
        self.name=name
        self.health=health
        self.inventory=[]
        self.position=(0,0)
    def __str__(self):
        return  f"player from pubgmobile {self.name} and {self.position} "   
    def move(self,x,y):
        self.position=(x,y)
        print(f"{self.name} moved to position {self.position}") 
    
    def take_damage(self,damage):
        self.health-=damage
        if self.health<=0:
           print(f"{self.name} has been elementated!")
        else:
           print(f"{self.name} took {damage} damage , {self.health} health remaning")
           
    def pick_up_weapon(self,weapon):
        self.inventory.append(weapon) 
        print(f"{self.name} pickid up {weapon}")              
               

P1=Player("Magd")   
print (P1)   

P1.move(2,5) 

p2=Player("younes")      
print (p2)  

p2.move(6,-5)   