class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance
     
    def deposti(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Środki zostały dodane do konta!")
        else:
            print("Blad kwoty, wplata nie moze byc mniejsza niz 0!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Niewystarczajace srodki na koncie!")
        elif amount < 0:
            print ("Bład kwoty")
        else:
            self.__balance = self.__balance - amount
            print(f"Wypłacono {amount} PLN.")

    def get_balance(self):
        return "Stan konta wynosi: " + str(self.__balance) +" PLN"


account = BankAccount("Jan Kowalski")

account.deposti(100) # 100
account.withdraw(40) # 60
account.deposti(200) # 260
account.deposti(100) # 360
account.withdraw(60) # 300
print(account.get_balance())
