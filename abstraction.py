from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete Class 1
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

# Concrete Class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")

    def stop_engine(self):
        print("Motorcycle engine stopped.")

# Instantiate the concrete classes
car = Car()
motorcycle = Motorcycle()

# Call the methods
car.start_engine()
car.stop_engine()

motorcycle.start_engine()
motorcycle.stop_engine()
