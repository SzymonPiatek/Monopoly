import pytest

from classes import Player, Country


@pytest.fixture
def player():
    return Player(name="Szymon", start_money=2000)


@pytest.fixture
def poland():
    return Country(name="Poland", buy_cost=500, tile_type="Neutral", location_id=1)


@pytest.fixture
def germany():
    return Country(name="Germany", buy_cost=1000, tile_type="Neutral", location_id=2)


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


def test_player_can_move(player):
    player_location = player.location

    player.move()
    assert player.location != player_location
    assert player.location in range(player_location, player_location + 12)
