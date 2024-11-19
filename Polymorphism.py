class Bird:
    def fly(self):
        print("bird is flying ")
        
class Airplane:
    def fly(self):
        print("Airplane  is flying ")
        
def make_it_fly(flyable):
    flyable.fly()
    
bird = Bird()
plane = Airplane()

make_it_fly(bird)
make_it_fly(plane)
'''
in the Polymorphism there are two 
    1 : is compile time polymorphism the "the method overloading"
    2: is run time polymorphism the "the method overriding"
'''