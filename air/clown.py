from person import Person
from balloon import Balloon
from air_tank import AirTank
from seller import Seller
from wallet import Wallet

class Clown(Person, Seller):
    def __init__(self):
        super().__init__()
        self.__tank = AirTank("Helium")

    def sell_item(self, cost:float):
        return self.buy_balloon(cost)
    
    def buy_balloon(self, cost) -> Balloon:
        balloon = Balloon("Red")
        balloon.fill(self.__tank.release_air(500))
        self._wallet.add_transaction(cost)
        return balloon
    
    def __str__(self) -> str:
        return f"Clown ($ {self._wallet.get_balance():.2f})"
    
    def speak(self):
        return super().find() + "\nWould anyone like to buy a ballon?"