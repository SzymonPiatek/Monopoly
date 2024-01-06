from random import randint, choice, random
from settings import *


class Tile:
    def __init__(self, tile_type: str, name: str, value: int, location: int):
        self.name = name
        self.location = location
        if tile_type == "country":
            self.buy_cost = value
            self.sell_cost = int(self.buy_cost * 0.8)
            self.rent_cost = int(self.buy_cost * 0.1)
            self.owner = None
        elif tile_type == "special":
            if name == "Start":
                self.effect_value = 500 if not value else value
            elif name == "Parking":
                self.effect_value = 50 if not value else value
            elif name == "Więzienie":
                self.effect_value = 1000 if not value else value
            else:
                self.effect_value = value

    def __str__(self):
        return self.name

    def start_bonus(self, player):
        player.money += self.effect_value

    def parking_pay(self, player):
        player.money -= self.effect_value

    def tax_pay(self, player):
        tax_result = 0
        if player.countries:
            for country in player.countries:
                tax_result += country.buy_cost * self.effect_value / 100
            player.money -= tax_result

    def prison_pay(self, player):
        if player.money > self.effect_value:
            player.money -= self.effect_value
        elif player.money <= self.effect_value:
            player.money = 0

    def card_random_effect(self, player):
        random_number = randint(-10, 10)
        random_number = random_number * 40
        player.money += random_number

    def rent_pay(self, player):
        player.money -= self.rent_cost

    def return_owner(self):
        if self.owner is not None:
            return f"{self.owner}"
        else:
            return "Brak"


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
                self.countries.append(country)
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
            self.location = self.location - (len(board) + 1)
