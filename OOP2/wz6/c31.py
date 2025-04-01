class Foo:
    def __init__(self,name):
        self.name=name
        print(f"Foo({self.name}):__init__")

    def __del__(self):
        print(f"Foo({self.name}):__del__")

f=Foo("Aston")
g=Foo("Lukas")
del f
x=input("wpisz coś: ")

def something():
    ff=Foo("Krzysio")

something()
# zrób to w cpp i sprawdź jak działa