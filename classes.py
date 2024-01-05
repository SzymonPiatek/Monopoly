from random import randint, choice, random
from settings import *


class SpecialTile:
    def __init__(self, name: str, value: int, location_id: int):
        self.name = name
        self.value = value
        self.location = location_id
        self.owner = 0

    def start_bonus(self, player):
        player.money += self.value

    def parking_pay(self, player):
        player.money -= self.value

    def tax_pay(self, player):
        player.money -= self.value

    def prison_pay(self, player):
        print("Trafiłeś do więzienia")
        if player.money >= 1000:
            player.money -= self.value
        if player.money < 1000:
            player.money = 0

    def card_random_effect(self, player):
        random_number = randint(-10, 10)
        random_number = random_number * 40

        player.money += random_number
        if random_number < 0:
            print(f"Zabrano ci {random_number}")
        elif random_number == 0:
            print("Nic się nie stało")
        elif random_number > 0:
            print(f"Dostałeś {random_number}")


class Country:
    def __init__(self, name, buy_cost, location_id):
        self.name = name
        self.location = location_id
        self.buy_cost = buy_cost
        self.sell_cost = self.buy_cost * 0.8
        self.rent = 0.10 * self.buy_cost
        self.owner = None

    def __str__(self):
        return self.name

    def rent_pay(self, player):
        player.money -= self.rent
        if player.money >= 0:
            print(f"Zapłacono {self.rent}")
        else:
            print("Bankructwo")

    def return_owner(self):
        if self.owner is not None:
            return f"{self.owner}"
        else:
            return "Kraj nie ma właściciela"


class Player:
    def __init__(self, name, start_money, color):
        self.name = choice(NAMES) if not name else name
        self.money = 2000 if not start_money else start_money
        self.location = 0
        self.countries = []
        self.color = color

    def country_list(self):
        if not self.countries:
            return "Brak krajów"
        elif len(self.countries) == 1:
            return self.countries
        elif len(self.countries) > 1:
            result = ""
            k = 0
            for i in self.countries:
                if not result:
                    result = f"{i},"
                    k += 1
                else:
                    if i == self.countries[-1]:
                        result = f"{result} {i}"
                    else:
                        if k % 2 != 0 and k < len(self.countries):
                            result = f"{result} {i},\n"
                        elif k % 2 == 0 and k < len(self.countries):
                            result = f"{result} {i},"
                    k += 1
            return result

    def buy_country(self, country):
        if self.money >= country.buy_cost:
            if country.owner is None:
                self.money -= country.buy_cost
                self.countries.append(country.name)
                country.owner = self

    def sell_country(self, country):
        if country.owner == self:
            self.money += country.sell_cost
            country.owner = None

    def throw_dice(self):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        result = dice1 + dice2

        return {
            "dice1": dice1,
            "dice2": dice2,
            "result": result
        }

    def move(self, dice, board):
        self.location = self.location + dice
        if self.location > len(board):
            self.location = self.location - (len(board)+1)
