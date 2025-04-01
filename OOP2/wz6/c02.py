class Foo:
    def __new__(cls):
        print("Foo:__new__")
        instance=super().__new__(cls) # fizyczne utworzenie obiektu
        return instance

    def __init__(self):
        print("Foo:__init__")

class Bar:
    def __new__(cls):
        print("Bar:__new__")
        f=Foo()
        return f
    
    def __init__(self):
        print("Bar:__init__")

b=Bar()
print(isinstance(b,Foo))