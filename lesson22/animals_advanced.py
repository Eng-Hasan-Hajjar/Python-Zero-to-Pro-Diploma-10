class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def move(self):
        print(f"{self.name} is moving")


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
    def describe(self):
        print(f"{self.name} is a mammal with {self.fur_color} fur")

class Dog(Mammal):
    def __init__(self, name, breed, fur_color):
        super().__init__(name, fur_color)
        self.breed = breed
    def speak(self):
        print(f"{self.name} says Woof!")
    def fetch(self):
        print(f"{self.name} is fetching the ball")


# إنشاء كائن من الفئة Dog
my_dog = Dog("Buddy", "Golden Retriever", "golden")
# استخدام الأساليب الموروثة والمخصصة
my_dog.move()       # Buddy is moving
my_dog.describe()   # Buddy is a mammal with golden fur
my_dog.speak()      # Buddy says Woof!
my_dog.fetch()      # Buddy is fetching the ball
