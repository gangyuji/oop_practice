class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("The animal speaks.")
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("Meow!")