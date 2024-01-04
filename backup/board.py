from classes import Country, SpecialTile

start = SpecialTile(name="Start", value=500, location_id=0)
card_tile = SpecialTile(name="Pobierz kartę", value=0, location_id=4)
card_tile2 = SpecialTile(name="Pobierz kartę", value=0, location_id=12)
card_tile3 = SpecialTile(name="Pobierz kartę", value=0, location_id=20)
card_tile4 = SpecialTile(name="Pobierz kartę", value=0, location_id=28)

prison = SpecialTile(name="Więzienie", value=1000, location_id=8)
parking = SpecialTile(name="Parking", value=50, location_id=16)
taxes = SpecialTile(name="Podatki", value=300, location_id=24)

country1 = Country(name="Ukraina", buy_cost=200, location_id=1)
country2 = Country(name="Polska", buy_cost=400, location_id=2)
country3 = Country(name="Czechy", buy_cost=500, location_id=3)
country4 = Country(name="Niemcy", buy_cost=600, location_id=5)
country5 = Country(name="Austria", buy_cost=500, location_id=6)
country6 = Country(name="Francja", buy_cost=650, location_id=7)
country7 = Country(name="Hiszpania", buy_cost=450, location_id=9)
country8 = Country(name="Włochy", buy_cost=600, location_id=10)
country9 = Country(name="Portugalia", buy_cost=450, location_id=11)
country10 = Country(name="Grecja", buy_cost=350, location_id=13)
country11 = Country(name="Cypr", buy_cost=250, location_id=14)
country12 = Country(name="Malta", buy_cost=300, location_id=15)
country13 = Country(name="Łotwa", buy_cost=450, location_id=17)
country14 = Country(name="Litwa", buy_cost=600, location_id=18)
country15 = Country(name="Estonia", buy_cost=450, location_id=19)
country16 = Country(name="Brazylia", buy_cost=350, location_id=21)
country17 = Country(name="Argentyna", buy_cost=250, location_id=22)
country18 = Country(name="Urugwaj", buy_cost=300, location_id=23)
country19 = Country(name="Stany Zjednoczone", buy_cost=450, location_id=25)
country20 = Country(name="Kanada", buy_cost=600, location_id=26)
country21 = Country(name="Meksyk", buy_cost=450, location_id=27)
country22 = Country(name="Australia", buy_cost=350, location_id=29)
country23 = Country(name="Grenlandia", buy_cost=250, location_id=30)
country24 = Country(name="Madagaskar", buy_cost=300, location_id=31)

board = [
    start,
    country1, country2, country3,
    card_tile,
    country4, country5, country6,
    prison,
    country7, country8, country9,
    card_tile2,
    country10, country11, country12,
    parking,
    country13, country14, country15,
    card_tile3,
    country16, country17, country18,
    taxes,
    country19, country20, country21,
    card_tile4,
    country22, country23, country24
]