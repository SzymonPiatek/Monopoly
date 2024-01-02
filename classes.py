from random import randint


def throw_dice():
    return randint(1, 6) + randint(1, 6)


class Country:
    def __init__(self, name, buy_cost, tile_type, location_id):
        self.name = name
        self.tile_type = tile_type
        self.location = location_id
        self.buy_cost = buy_cost
        self.sell_cost = self.buy_cost * 0.8
        self.rent = 0.10 * self.buy_cost
        self.owner = None

    def __str__(self):
        return self.name

    def rent_pay(self, player):
        player.money -= self.rent

    def owner(self):
        return f"{self.owner}"


class Player:
    def __init__(self, name, start_money):
        self.name = name
        self.money = start_money
        self.location = 0

    def __str__(self):
        return self.name

    def buy_country(self, country):
        if self.money >= country.buy_cost:
            if country.owner is None:
                self.money -= country.buy_cost
                country.owner = self

    def sell_country(self, country):
        if country.owner == self:
            self.money += country.sell_cost
            country.owner = None

    def move(self):
        self.location = self.location + throw_dice()


