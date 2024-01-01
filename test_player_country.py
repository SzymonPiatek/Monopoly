import pytest

from main import Player, Country


@pytest.fixture
def player():
    return Player(name="Szymon", start_money=2000)


@pytest.fixture
def poland():
    return Country(name="Poland", cost=500)


@pytest.fixture
def germany():
    return Country(name="Germany", cost=1000)


def test_player_buy_country(player, poland):
    player_money = player.money
    poland_cost = poland.cost

    player.buy_country(country=poland)
    assert player.money == player_money - poland_cost
    assert poland.owner == player


def test_player_cannot_buy_country_again(player, poland):
    player_money = player.money
    poland_cost = poland.cost

    player.buy_country(country=poland)
    player.buy_country(country=poland)
    assert player.money == player_money - poland_cost
    assert poland.owner == player
