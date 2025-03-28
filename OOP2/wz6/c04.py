# Singleton

class Singleton:
    __ins=None # zawiera informacje o jedynej instancji którą stworzyliśmy

    def __new__(cls):
        if cls.__ins is None:
            print(" Creating instance")
            cls.__ins=super().__new__(cls)
        return cls.__ins

obj1=Singleton()
obj2=Singleton()
obj3=Singleton()

print(obj1)
print(obj2)
print(obj3)