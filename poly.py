class Animal:
    def __init__(self):
        self._property = "One"

    def get_property(self):
        return self._property
    
    def eat_food(self):
        #fixed
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def get_property(self):
        return "Two"
    

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self._property = "Three"


one:Animal = Animal()
two:Animal = Dog()
three:Animal = Cat()

print(one.get_property())
print(two.get_property())
print(three.get_property())