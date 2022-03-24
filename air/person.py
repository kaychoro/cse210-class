from wallet import Wallet


class Person:
    def __init__(self):
        self._wallet = Wallet(0)
    
    def __str__(self):
        return "(Person)"

    def get_wallet(self):
        return self._wallet

    def speak(self) -> str:
        return "Hi, my name is John."