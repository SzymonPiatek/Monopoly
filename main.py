class Country:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.rent = 0.10 * self.cost
        self.owner = None

    def __str__(self):
        return self.name

    def rent_pay(self, player):
        player.money -= self.rent


class Player:
    def __init__(self, name, start_money):
        self.name = name
        self.money = start_money

    def __str__(self):
        return self.name

    def buy_country(self, country):
        if self.money >= country.cost:
            if country.owner is None:
                self.money -= country.cost
                country.owner = self
