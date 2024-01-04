from classes import Player
from board import *

winner = None
start_money = 2000

player1_name = input("Nazwa pierwszego gracza: ")
player2_name = input("Nazwa drugiego gracza: ")

player1 = Player(name=player1_name, start_money=start_money)
player2 = Player(name=player2_name, start_money=start_money)


def choose_action(board, player, tile, owner):
    if not owner:
        if tile.owner is not None:
            pass
        elif tile.owner is None:
            choice = input('''
                Co chcesz zrobić?
                0 - Kupić kraj
                1 - Nic nie robić
                
                ''')

            if choice == '0':
                player.buy_country(country=tile)
            elif choice == '1':
                print("Pass")
            else:
                choose_action(board=board, player=player, tile=tile, owner=owner)
    if owner:
        choice = input('''
                    Co chcesz zrobić?
                    0 - Sprzedać kraj
                    1 - Nic nie robić

                    ''')

        if choice == '0':
            player.sell_country(country=tile)
        elif choice == '1':
            print("Pass")
        else:
            choose_action(board=board, player=player, tile=tile, owner=owner)


turn = 0
while winner is None:
    if turn == 0:
        player = player1
    elif turn == 1:
        player = player2

    dice = player.move()
    country = []
    for tile in board:
        if tile.owner == player:
            country.append(tile.name)

    print("=====" * 4)
    print(f"Gracz: {player.name}")
    print(f"Saldo: {player.money}")

    if not country:
        print("Brak krajów")
    else:
        print(f"Lista krajów: {country}")
    print("-----" * 4)
    print(f"Wyrzucił*ś: {dice}")
    for tile in board:
        if tile.location == player.location:
            print(f"Wylądował*ś na polu: {tile.name}")
            break

    for tile in board:
        if tile.location == player.location:
            this_tile = tile
            if this_tile.owner == player:
                pass
            elif this_tile.owner == 0:
                pass
            elif this_tile.owner is not None:
                print(f"{this_tile.owner} rząda od ciebie zapłaty czynszu!")
                print(f"Czynsz wynosi {this_tile.rent}")
                this_tile.rent_pay(player=player)

    if player.money < 0:
        if player == player1:
            print(f"Wygrał(a) {player2.name}")
        elif player == player2:
            print(f"Wygrał(a) {player1.name}")
        break

    tile = this_tile

    if tile.owner is None:
        print(f"Koszt zakupu: {tile.buy_cost}")

    if player.location == start.location:
        start.start_bonus(player=player)
    elif player.location == parking.location:
        parking.parking_pay(player=player)
    elif player.location == taxes.location:
        taxes.tax_pay(player=player)
    elif player.location == prison.location:
        prison.prison_pay(player)
    elif player.location == card_tile.location:
        card_tile.card_random_effect(player=player)
    elif player.location == card_tile2.location:
        card_tile2.card_random_effect(player=player)
    elif player.location == card_tile3.location:
        card_tile3.card_random_effect(player=player)
    elif player.location == card_tile4.location:
        card_tile4.card_random_effect(player=player)
    else:
        if tile.owner == player:
            choose_action(board=board, player=player, tile=tile, owner=True)
        else:
            choose_action(board=board, player=player, tile=tile, owner=False)

    turn = 1 if turn == 0 else 0
