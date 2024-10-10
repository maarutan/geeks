class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def moneyX(self):
        amount = float(input("Сколько денег хотите добавить? "))
        self.__balance += amount
        print(f"На вашем счету: {self.__balance}")

    def _kill(self):
        self.__balance = 0
        print("Баланс обнулен.")

    def __jackpot(self):
        self.__balance *= 10
        print(f"Ваш баланс после джекпота: {self.__balance}")

    def _combine_balance(self, other):
        self.__balance += other.__balance
        print(f"Общий баланс: {self.__balance}")
        
        
client1 = Bank("Марат", 1000)
client1.moneyX()
client1._kill()
client1._Bank__jackpot()

client2 = Bank("Камила", 500)
client1._combine_balance(client2)


