import pytest

from classes import Player, Tile


@pytest.fixture
def player():
    return Player(name="Player 1", start_money=2000, color="#262626")


@pytest.fixture
def player2():
    return Player(name="Player 2", start_money=2000, color="#262626")


@pytest.fixture
def start():
    return Tile(tile_type="special", name="Start", value=500, location=0)


@pytest.fixture
def take_card1():
    return Tile(tile_type="special", name="Take card", value=0, location=5)


@pytest.fixture
def parking():
    return Tile(tile_type="special", name="Parking", value=50, location=6)


@pytest.fixture
def tax():
    return Tile(tile_type="special", name="Podatki", value=10, location=7)


@pytest.fixture
def prison():
    return Tile(tile_type="special", name="Więzienie", value=1000, location=8)


@pytest.fixture
def poland():
    return Tile(tile_type="country", name="Poland", value=400, location=1)


@pytest.fixture
def germany():
    return Tile(tile_type="country", name="Germany", value=500, location=2)


@pytest.fixture
def italy():
    return Tile(tile_type="country", name="Italy", value=450, location=3)


@pytest.fixture
def portugal():
    return Tile(tile_type="country", name="Portugal", value=350, location=4)


@pytest.fixture
def board(start, poland, germany, italy, take_card1, portugal, parking, tax, prison):
    return [start, poland, germany, italy, take_card1, portugal, parking, tax, prison]


def test_player_can_buy_country(player, poland):
    player_money = player.money

    player.buy_country(country=poland)
    assert player.money == player_money - poland.buy_cost
    assert poland.owner == player


def test_player_cannot_buy_country(player, poland):
    player_money = player.money - (player.money - poland.buy_cost + 1)
    player.money = player_money

    player.buy_country(country=poland)
    assert poland.owner is None
    assert player.money == player_money


def test_player_cannot_buy_country_again(player, poland):
    player_money = player.money

    player.buy_country(country=poland)
    player.buy_country(country=poland)
    assert player.money == player_money - poland.buy_cost
    assert poland.owner == player


def test_player_can_sell_country(player, poland):
    player_money = player.money

    player.buy_country(country=poland)
    assert poland.owner == player
    assert player.money == player_money - poland.buy_cost

    player.sell_country(country=poland)
    assert poland.owner is None
    assert player.money == player_money - (poland.buy_cost - poland.sell_cost)


def test_player_cannot_sell_country(player, poland):
    player_money = player.money

    player.sell_country(country=poland)
    assert player.money == player_money
    assert poland.owner is None


def test_player_pay_rent(player, poland):
    player_money = player.money
    poland.rent_pay(player=player)
    assert player.money == player_money - poland.rent_cost


def test_player_pay_tax(player, poland, tax):
    player.buy_country(country=poland)
    player_money = player.money

    tax.tax_pay(player=player)
    assert player.money == player_money - (poland.buy_cost * tax.effect_value / 100)


def test_player_pay_prison(player, prison):
    print("===="*5)
    player.money = prison.effect_value + 100
    player_money = player.money
    prison.prison_pay(player=player)
    assert player.money == player_money - prison.effect_value

    player.money = prison.effect_value
    prison.prison_pay(player=player)
    assert player.money == 0

    player.money = prison.effect_value - 100
    prison.prison_pay(player=player)
    assert player.money == 0


def test_player_can_move(player, board):
    for i in range(100):
        player_location = 0
        player.location = 0

        player.move(dice=player.throw_dice()['dice1'], board=board)
        assert player.location != player_location
        assert player.location in range(player_location + 1, player_location + 13)


def test_player_stand_at_start(player, start):
    player_money = player.money
    start_bonus = start.effect_value

    start.start_bonus(player=player)
    assert player.money == player_money + start_bonus


def test_player_stand_at_parking(player, parking):
    player_money = player.money
    parking_value = parking.effect_value

    parking.parking_pay(player=player)
    assert player.money == player_money - parking_value
