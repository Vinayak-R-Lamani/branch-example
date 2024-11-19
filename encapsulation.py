class Person:
    def __init__(self , name: str , age: int):
        self._name = name
        self._age = age
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age

        
class Main:
    @staticmethod
    def main():
        person = Person('name' ,12)
        print(person.get_name())
        print(person.get_age())
        print('hello world')
        
if __name__== "__main__":
    Main.main()