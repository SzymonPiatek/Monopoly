from random import randint


def throw_dice():
    return randint(1, 6) + randint(1, 6)


class SpecialTile:
    def __init__(self, name: str, value: int, location_id: int):
        self.name = name
        self.value = value
        self.location = location_id
        self.owner = 0
        self.buy_cost = None

    def start_bonus(self, player):
        player.money += self.value
        print(f"Start +{self.value}")
        print(player.money)

    def parking_pay(self, player):
        player.money -= self.value
        print(f"Zapłacono za parking {self.value}")
        print(player.money)

    def tax_pay(self, player):
        player.money -= self.value
        print(f"Opłacono podatki w wysokości {self.value}")
        print(player.money)

    def prison_pay(self, player):
        print("Trafiłeś do więzienia")
        if player.money >= 1000:
            player.money -= self.value
            print(f"Tracisz {self.value}")
        if player.money < 1000:
            player.money = 0
            print(f"Tracisz wszystkie pieniądze")

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
                print("Kupiłeś ten kraj")
        elif country.owner == self:
            print("Ten kraj już należy do ciebie")
        else:
            print("Nie możesz kupić tego kraju")

    def sell_country(self, country):
        if country.owner == self:
            self.money += country.sell_cost
            country.owner = None
            print("Sprzedałeś ten kraj")
        else:
            print("Ten kraj nie należy do ciebie")

    def move(self):
        dice = throw_dice()
        self.location = self.location + dice
        if self.location > 15:
            self.location = self.location - 16
        return dice
