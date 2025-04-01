class BaseClass:
    def __new__(cls):
        obj=super().__new__(cls)
        obj._from_base_class=type(obj)==BaseClass
        return obj
    
class Subclass(BaseClass):
    pass

base_instance=BaseClass()

sub_instance=Subclass()

print(base_instance._from_base_class)

print(sub_instance._from_base_class)