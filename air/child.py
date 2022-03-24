from person import Person

class Child(Person):
    def __init__(self):
        super().__init__()
        self.__has_balloon = False
    

    def __str__(self):
        return super().__str__() + " (child)"

    def has_balloon(self) -> bool:
        return self.__has_balloon
    
    def speak(self):
        return super().speak() + "\nI WANT a ballon!!"

child = Child()
print(child.get_wallet())