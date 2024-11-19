class Animal:
    def __init__(self , name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof !")
        

class Cat(Animal):
    def speak(self):
        print(f"{self.name} say meow!")
        
class Lion(Animal):
    pass
        
dog = Dog('Buddy')
cat = Cat('Whiskers')
lion = Lion("aaa")


dog.speak()
cat.speak()
print(lion.speak())