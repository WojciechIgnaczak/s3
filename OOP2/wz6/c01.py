class Person:
    def __new__(cls,name,age):
        print("Creating a new Person object")
        instance=super().__new__(cls) # fizyczne utworzenie obiektu
        return instance

    def __init__(self,name,age):
        print("Initializing")
        self.name=name
        self.age=age

person=Person("John",30)
print(f"{person.name}, {person.age}")