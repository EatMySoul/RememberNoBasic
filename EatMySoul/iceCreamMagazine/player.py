class Player:

    def __init__(self):
        self.healf = 100
        self.dmg = 5
        self.cash = 44

    def pay(self, cash_to_pay):
        iceCreamMagazine.pay(cash_to_pay)

    def get_damage(self, dmg):
        self.healf -= dmg

    def attack(self):
        iceCreamMagazine.get_damage(self.dmg)
