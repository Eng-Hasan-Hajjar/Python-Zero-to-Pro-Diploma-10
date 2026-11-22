class Weapon:
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage
    def __str__(self):
        return f"{self.name}"
    
akm=Weapon("AKM",49)
m416=Weapon("M4",36)
upm=Weapon("ump",20)

print(akm)    