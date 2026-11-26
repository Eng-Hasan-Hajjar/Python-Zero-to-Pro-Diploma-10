class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def move(self):
        print(f"{self.name} is moving")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} says Woof!")
    def fetch(self):
        print(f"{self.name} is fetching the ball")



# إنشاء كائن من الفئة Dog
my_dog = Dog("Buddy", "Golden Retriever")
# استخدام الأساليب الموروثة والمخصصة
my_dog.move()    # Buddy is moving
my_dog.speak()   # Buddy says Woof!
my_dog.fetch()   # Buddy is fetching the ball
