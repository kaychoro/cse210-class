import time

class Wallet:
    class Transaction:
        def __init__(self, amount):
            self._amount = amount
            self._timestamp = time.time()
        
        def get_amount(self):
            return self._amount

    def __init__(self, initial_amount):
        self._transactions = []
        self._transactions.append(Wallet.Transaction(initial_amount))
    
    def add_transaction(self, tx_amount):
        self._transactions.append(Wallet.Transaction(tx_amount))

    def _sum_transactions(self):
        total = 0
        for tx in self._transactions:
            total += tx.get_amount()
        return total

    def get_balance(self):
        return self._sum_transactions()

    def __str__(self):
        return "Wallet: " + str(self._sum_transactions())

    def __repr__(self):
        return "W:" + str(self._sum_transactions())

wallets = []
wallets.append(Wallet(34))
wallets.append(Wallet(35))
print(wallets)
print(wallets[0])
wallet = Wallet(50)
wallet.add_transaction(-25)
print(wallet.get_balance())
print(str(wallet))