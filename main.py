import customtkinter as ctk
from tkinter import messagebox, colorchooser

from classes import Player, Country, SpecialTile
from settings import *


def change_frame(old_frame, new_frame):
    old_frame.destroy()
    new_frame()


def player_frame(name_label, money_title, money_label, country_title, country_label, color):
    name_label.place(relx=0.5, rely=0.04, anchor=ctk.CENTER, relwidth=1, relheight=0.08)
    money_title.place(relx=0.5, rely=0.14, anchor=ctk.CENTER, relwidth=1)
    money_label.place(relx=0.5, rely=0.19, anchor=ctk.CENTER)
    country_title.place(relx=0.5, rely=0.26, anchor=ctk.CENTER, relwidth=1)
    country_label.place(relx=0.5, rely=0.31, anchor=ctk.CENTER)

    # Configure
    name_label.configure(bg_color=color)


class GameApp:
    def __init__(self, master):
        # App settings
        self.master = master
        self.master.title("Monopoly")
        self.master.attributes("-fullscreen", True)

        # Screen size
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.screen_ratio = self.screen_width / self.screen_height

        # Fonts
        self.font_title_main_menu = ctk.CTkFont(family=FONT_1, size=128, weight="bold")
        self.font_button_main_menu = ctk.CTkFont(family=FONT_1, size=48, weight="bold")

        # Bind
        self.master.bind("<Escape>", self.confirm_exit)

        # Create Frame
        self.main_menu_frame = ctk.CTkFrame(master=self.master)

        # Widgets
        self.main_menu_label = ctk.CTkLabel(master=self.main_menu_frame,
                                            text="MONOPOLY", font=self.font_title_main_menu)
        self.main_menu_button = ctk.CTkButton(master=self.main_menu_frame,
                                              text="Graj",
                                              command=lambda: change_frame(old_frame=self.main_menu_frame,
                                                                           new_frame=self.set_player_view),
                                              font=self.font_button_main_menu,
                                              fg_color=BUTTON_COLOR_1,
                                              hover_color=HOVER_BUTTON_COLOR_1)

        # Layout
        self.main_menu_label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        self.main_menu_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER, relwidth=0.15, relheight=0.08)

        # Frame
        self.main_menu_frame.pack(fill=ctk.BOTH, expand=1)

    def choose_color_button(self, button):
        color = colorchooser.askcolor()[1]
        button.configure(fg_color=color)

    def set_player_view(self):
        # Create Frame
        self.menu_frame = ctk.CTkFrame(master=self.master)

        # Fonts
        self.font_label_set_player_view = ctk.CTkFont(family="Helvetica", size=48, weight="bold")
        self.font_entry_set_player_view = ctk.CTkFont(family="Helvetica", size=32, weight="bold")
        self.font_button_set_player_view = self.font_button_main_menu

        # Player One Widgets
        self.player_one_label = ctk.CTkLabel(master=self.menu_frame,
                                             text="Gracz 1",
                                             font=self.font_label_set_player_view)
        self.player_one_entry = ctk.CTkEntry(master=self.menu_frame,
                                             placeholder_text="Wpisz nazwę gracza",
                                             font=self.font_entry_set_player_view)
        self.player_one_choose_color = ctk.CTkButton(master=self.menu_frame,
                                                     text="Wybierz kolor",
                                                     command=lambda: self.choose_color_button(
                                                         self.player_one_choose_color),
                                                     font=self.font_entry_set_player_view)

        # Player Two Widgets
        self.player_two_label = ctk.CTkLabel(master=self.menu_frame,
                                             text="Gracz 2",
                                             font=self.font_label_set_player_view)
        self.player_two_entry = ctk.CTkEntry(master=self.menu_frame,
                                             placeholder_text="Wpisz nazwę gracza",
                                             font=self.font_entry_set_player_view)
        self.player_two_choose_color = ctk.CTkButton(master=self.menu_frame,
                                                     text="Wybierz kolor",
                                                     command=lambda: self.choose_color_button(
                                                         self.player_two_choose_color),
                                                     font=self.font_entry_set_player_view)

        # Game settings Widgets
        self.start_value_label = ctk.CTkLabel(master=self.menu_frame,
                                              text="Stan konta na start",
                                              font=self.font_label_set_player_view)
        self.start_value_entry = ctk.CTkEntry(master=self.menu_frame,
                                              placeholder_text="Domyślnie 2000",
                                              font=self.font_entry_set_player_view)

        # Widgets
        self.start_game_button = ctk.CTkButton(master=self.menu_frame,
                                               text="Start",
                                               command=self.start_game_button_click,
                                               font=self.font_button_set_player_view,
                                               fg_color=BUTTON_COLOR_1,
                                               hover_color=HOVER_BUTTON_COLOR_1)

        # Layout
        self.player_one_label.place(relx=0.25, rely=0.2, anchor=ctk.CENTER)
        self.player_one_entry.place(relx=0.25, rely=0.27, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)
        self.player_one_choose_color.place(relx=0.25, rely=0.34, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)

        self.player_two_label.place(relx=0.75, rely=0.2, anchor=ctk.CENTER)
        self.player_two_entry.place(relx=0.75, rely=0.27, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)
        self.player_two_choose_color.place(relx=0.75, rely=0.34, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)

        self.start_value_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.start_value_entry.place(relx=0.5, rely=0.57, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)

        self.start_game_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER, relwidth=0.15, relheight=0.08)

        # Frame
        self.menu_frame.pack(fill=ctk.BOTH, expand=1)

    def start_game_button_click(self):
        # Set variables
        self.player_one_name = self.player_one_entry.get()
        self.player_one_color = self.player_one_choose_color.cget("fg_color")
        self.player_two_name = self.player_two_entry.get()
        self.player_two_color = self.player_two_choose_color.cget("fg_color")
        self.start_value = self.start_value_entry.get()
        # Change Frame
        change_frame(old_frame=self.menu_frame, new_frame=self.game_view)

    def player_location_on_board(self, player):
        # Looking tile where player must be set
        for tile in self.board:
            if tile.location == player.location:
                print(player.location)

    def game_view(self):
        # Fonts
        self.font_label_game_view = ctk.CTkFont(family=FONT_1, size=24)
        self.font_label_name_game_view = ctk.CTkFont(family=FONT_1, size=40, weight="bold")
        self.font_title_game_view = ctk.CTkFont(family=FONT_1, size=32, weight="bold")
        self.card_title_game_view = ctk.CTkFont(family=FONT_1, size=32, weight="bold")

        # Countries
        self.tile0 = SpecialTile(name="Start", value=500, location_id=0)
        self.tile1 = Country(name="Polska", buy_cost=300, location_id=1)
        self.tile2 = Country(name="Czechy", buy_cost=250, location_id=2)
        self.tile3 = Country(name="Słowacja", buy_cost=250, location_id=3)
        self.tile4 = SpecialTile(name="Pobierz kartę", value=0, location_id=4)
        self.tile5 = Country(name="Niemcy", buy_cost=450, location_id=5)
        self.tile6 = Country(name="Holandia", buy_cost=350, location_id=6)
        self.tile7 = Country(name="Luksemburg", buy_cost=450, location_id=7)
        self.tile8 = SpecialTile(name="Więzienie", value=1000, location_id=8)
        self.tile9 = Country(name="Belgia", buy_cost=300, location_id=9)
        self.tile10 = Country(name="Francja", buy_cost=500, location_id=10)
        self.tile11 = Country(name="Anglia", buy_cost=450, location_id=11)
        self.tile12 = SpecialTile(name="Pobierz kartę", value=0, location_id=12)
        self.tile13 = Country(name="Hiszpania", buy_cost=350, location_id=13)
        self.tile14 = Country(name="Portugalia", buy_cost=300, location_id=14)
        self.tile15 = Country(name="Włochy", buy_cost=400, location_id=15)
        self.tile16 = SpecialTile(name="Parking", value=50, location_id=16)
        self.tile17 = Country(name="Litwa", buy_cost=250, location_id=17)
        self.tile18 = Country(name="Estonia", buy_cost=250, location_id=18)
        self.tile19 = Country(name="Łotwa", buy_cost=200, location_id=19)
        self.tile20 = SpecialTile(name="Pobierz kartę", value=0, location_id=20)
        self.tile21 = Country(name="Węgry", buy_cost=300, location_id=21)
        self.tile22 = Country(name="Rumunia", buy_cost=300, location_id=22)
        self.tile23 = Country(name="Mołdawia", buy_cost=200, location_id=23)
        self.tile24 = SpecialTile(name="Podatki", value=10, location_id=24)
        self.tile25 = Country(name="Bułgaria", buy_cost=300, location_id=25)
        self.tile26 = Country(name="Serbia", buy_cost=250, location_id=26)
        self.tile27 = Country(name="Chorwacja", buy_cost=3000, location_id=27)
        self.tile28 = SpecialTile(name="Pobierz kartę", value=0, location_id=28)
        self.tile29 = Country(name="Grecja", buy_cost=250, location_id=29)
        self.tile30 = Country(name="Albania", buy_cost=250, location_id=30)
        self.tile31 = Country(name="Turcja", buy_cost=350, location_id=31)

        self.board = [self.tile0, self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6,
                      self.tile7, self.tile8, self.tile9, self.tile10, self.tile11, self.tile12, self.tile13,
                      self.tile14, self.tile15, self.tile16, self.tile17, self.tile18, self.tile19, self.tile20,
                      self.tile21, self.tile22, self.tile23, self.tile24, self.tile25, self.tile26, self.tile27,
                      self.tile28, self.tile29, self.tile30, self.tile31]

        # Players
        self.player_one = Player(name=self.player_one_name, start_money=self.start_value, color=self.player_one_color)
        self.player_two = Player(name=self.player_two_name, start_money=self.start_value, color=self.player_two_color)

        # Create Main Frame
        self.game_frame = ctk.CTkFrame(master=self.master)

        # Create Child Frames For Main Frame
        self.player_one_frame = ctk.CTkFrame(master=self.game_frame)
        self.player_two_frame = ctk.CTkFrame(master=self.game_frame)
        self.board_frame = ctk.CTkFrame(master=self.game_frame)

        # Create Child Frames For Board Frame
        self.mid_board_frame = ctk.CTkFrame(master=self.board_frame)

        self.tile0_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile1_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile2_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile3_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile4_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile5_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile6_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile7_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile8_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile9_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile10_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile11_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile12_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile13_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile14_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile15_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile16_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile17_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile18_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile19_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile20_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile21_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile22_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile23_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile24_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile25_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile26_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile27_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile28_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile29_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile30_frame = ctk.CTkFrame(master=self.board_frame)
        self.tile31_frame = ctk.CTkFrame(master=self.board_frame)

        # Create Child Frame for Mid Board Frame
        self.tile_card_frame = ctk.CTkFrame(master=self.mid_board_frame, fg_color="transparent")

        # Player One Widgets
        self.player_one_name_label = ctk.CTkLabel(master=self.player_one_frame,
                                                  text=self.player_one.name.upper(),
                                                  font=self.font_label_name_game_view)

        self.player_one_money_title = ctk.CTkLabel(master=self.player_one_frame,
                                                   text="Saldo:",
                                                   font=self.font_title_game_view)
        self.player_one_money_label = ctk.CTkLabel(master=self.player_one_frame,
                                                   text=self.player_one.money,
                                                   font=self.font_label_game_view)

        self.player_one_country_title = ctk.CTkLabel(master=self.player_one_frame,
                                                     text="Lista krajów:",
                                                     font=self.font_title_game_view)
        self.player_one_country_label = ctk.CTkLabel(master=self.player_one_frame,
                                                     text=self.player_one.country_list(),
                                                     font=self.font_label_game_view)

        # Player Two Widgets
        self.player_two_name_label = ctk.CTkLabel(master=self.player_two_frame,
                                                  text=self.player_two.name.upper(),
                                                  font=self.font_label_name_game_view)

        self.player_two_money_title = ctk.CTkLabel(master=self.player_two_frame,
                                                   text="Saldo",
                                                   font=self.font_title_game_view)
        self.player_two_money_label = ctk.CTkLabel(master=self.player_two_frame,
                                                   text=self.player_two.money,
                                                   font=self.font_label_game_view)

        self.player_two_country_title = ctk.CTkLabel(master=self.player_two_frame,
                                                     text="Lista krajów",
                                                     font=self.font_title_game_view)
        self.player_two_country_label = ctk.CTkLabel(master=self.player_two_frame,
                                                     text=self.player_two.country_list(),
                                                     font=self.font_label_game_view)

        # Board Widgets
        self.tile0_area = ctk.CTkButton(master=self.tile0_frame,
                                        text=self.tile0.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="start",
                                                                             tile=self.tile0),
                                        fg_color=START_COLOR_1)
        self.tile1_area = ctk.CTkButton(master=self.tile1_frame,
                                        text=self.tile1.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile1),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile2_area = ctk.CTkButton(master=self.tile2_frame,
                                        text=self.tile2.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile2),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile3_area = ctk.CTkButton(master=self.tile3_frame,
                                        text=self.tile3.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile3),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile4_area = ctk.CTkButton(master=self.tile4_frame,
                                        text=self.tile4.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="take_card",
                                                                             tile=self.tile4),
                                        fg_color=TAKE_CARD_COLOR_1)
        self.tile5_area = ctk.CTkButton(master=self.tile5_frame,
                                        text=self.tile5.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile5),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile6_area = ctk.CTkButton(master=self.tile6_frame,
                                        text=self.tile6.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile6),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile7_area = ctk.CTkButton(master=self.tile7_frame,
                                        text=self.tile7.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile7),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile8_area = ctk.CTkButton(master=self.tile8_frame,
                                        text=self.tile8.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="prison",
                                                                             tile=self.tile8),
                                        fg_color=PRISON_COLOR_1)
        self.tile9_area = ctk.CTkButton(master=self.tile9_frame,
                                        text=self.tile9.name,
                                        command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                             status="country",
                                                                             tile=self.tile9),
                                        fg_color=COUNTRY_COLOR_1)
        self.tile10_area = ctk.CTkButton(master=self.tile10_frame,
                                         text=self.tile10.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile10),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile11_area = ctk.CTkButton(master=self.tile11_frame,
                                         text=self.tile11.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile11),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile12_area = ctk.CTkButton(master=self.tile12_frame,
                                         text=self.tile12.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="take_card",
                                                                              tile=self.tile12),
                                         fg_color=TAKE_CARD_COLOR_1)
        self.tile13_area = ctk.CTkButton(master=self.tile13_frame,
                                         text=self.tile13.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile13),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile14_area = ctk.CTkButton(master=self.tile14_frame,
                                         text=self.tile14.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile14),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile15_area = ctk.CTkButton(master=self.tile15_frame,
                                         text=self.tile15.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile15),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile16_area = ctk.CTkButton(master=self.tile16_frame,
                                         text=self.tile16.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="parking",
                                                                              tile=self.tile16),
                                         fg_color=PARKING_COLOR_1)
        self.tile17_area = ctk.CTkButton(master=self.tile17_frame,
                                         text=self.tile17.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile17),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile18_area = ctk.CTkButton(master=self.tile18_frame,
                                         text=self.tile18.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile18),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile19_area = ctk.CTkButton(master=self.tile19_frame,
                                         text=self.tile19.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile19),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile20_area = ctk.CTkButton(master=self.tile20_frame,
                                         text=self.tile20.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="take_card",
                                                                              tile=self.tile20),
                                         fg_color=TAKE_CARD_COLOR_1)
        self.tile21_area = ctk.CTkButton(master=self.tile21_frame,
                                         text=self.tile21.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile21),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile22_area = ctk.CTkButton(master=self.tile22_frame,
                                         text=self.tile22.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile22),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile23_area = ctk.CTkButton(master=self.tile23_frame,
                                         text=self.tile23.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile23),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile24_area = ctk.CTkButton(master=self.tile24_frame,
                                         text=self.tile24.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="tax",
                                                                              tile=self.tile24),
                                         fg_color=TAX_COLOR_1)
        self.tile25_area = ctk.CTkButton(master=self.tile25_frame,
                                         text=self.tile25.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile25),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile26_area = ctk.CTkButton(master=self.tile26_frame,
                                         text=self.tile26.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile26),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile27_area = ctk.CTkButton(master=self.tile27_frame,
                                         text=self.tile27.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile27),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile28_area = ctk.CTkButton(master=self.tile28_frame,
                                         text=self.tile28.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="take_card",
                                                                              tile=self.tile28),
                                         fg_color=TAKE_CARD_COLOR_1)
        self.tile29_area = ctk.CTkButton(master=self.tile29_frame,
                                         text=self.tile29.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile29),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile30_area = ctk.CTkButton(master=self.tile30_frame,
                                         text=self.tile30.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile30),
                                         fg_color=COUNTRY_COLOR_1)
        self.tile31_area = ctk.CTkButton(master=self.tile31_frame,
                                         text=self.tile31.name,
                                         command=lambda: self.show_tile_stats(frame=self.tile_card_frame,
                                                                              status="country",
                                                                              tile=self.tile31),
                                         fg_color=COUNTRY_COLOR_1)

        # Player One Layout
        player_frame(name_label=self.player_one_name_label,
                     money_title=self.player_one_money_title,
                     money_label=self.player_one_money_label,
                     country_title=self.player_one_country_title,
                     country_label=self.player_one_country_label,
                     color=self.player_one_color)

        # Player Two Layout
        player_frame(name_label=self.player_two_name_label,
                     money_title=self.player_two_money_title,
                     money_label=self.player_two_money_label,
                     country_title=self.player_two_country_title,
                     country_label=self.player_two_country_label,
                     color=self.player_two_color)

        # Board Layout
        self.tile0_area.pack(fill=ctk.BOTH, expand=1)
        self.tile1_area.pack(fill=ctk.BOTH, expand=1)
        self.tile2_area.pack(fill=ctk.BOTH, expand=1)
        self.tile3_area.pack(fill=ctk.BOTH, expand=1)
        self.tile4_area.pack(fill=ctk.BOTH, expand=1)
        self.tile5_area.pack(fill=ctk.BOTH, expand=1)
        self.tile6_area.pack(fill=ctk.BOTH, expand=1)
        self.tile7_area.pack(fill=ctk.BOTH, expand=1)
        self.tile8_area.pack(fill=ctk.BOTH, expand=1)
        self.tile9_area.pack(fill=ctk.BOTH, expand=1)
        self.tile10_area.pack(fill=ctk.BOTH, expand=1)
        self.tile11_area.pack(fill=ctk.BOTH, expand=1)
        self.tile12_area.pack(fill=ctk.BOTH, expand=1)
        self.tile13_area.pack(fill=ctk.BOTH, expand=1)
        self.tile14_area.pack(fill=ctk.BOTH, expand=1)
        self.tile15_area.pack(fill=ctk.BOTH, expand=1)
        self.tile16_area.pack(fill=ctk.BOTH, expand=1)
        self.tile17_area.pack(fill=ctk.BOTH, expand=1)
        self.tile18_area.pack(fill=ctk.BOTH, expand=1)
        self.tile19_area.pack(fill=ctk.BOTH, expand=1)
        self.tile20_area.pack(fill=ctk.BOTH, expand=1)
        self.tile21_area.pack(fill=ctk.BOTH, expand=1)
        self.tile22_area.pack(fill=ctk.BOTH, expand=1)
        self.tile23_area.pack(fill=ctk.BOTH, expand=1)
        self.tile24_area.pack(fill=ctk.BOTH, expand=1)
        self.tile25_area.pack(fill=ctk.BOTH, expand=1)
        self.tile26_area.pack(fill=ctk.BOTH, expand=1)
        self.tile27_area.pack(fill=ctk.BOTH, expand=1)
        self.tile28_area.pack(fill=ctk.BOTH, expand=1)
        self.tile29_area.pack(fill=ctk.BOTH, expand=1)
        self.tile30_area.pack(fill=ctk.BOTH, expand=1)
        self.tile31_area.pack(fill=ctk.BOTH, expand=1)

        # Child Frames For Board Frame
        y = 9
        x = y * 2
        gap = 0.02
        self.tile0_frame.place(relx=1 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile1_frame.place(relx=3 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile2_frame.place(relx=5 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile3_frame.place(relx=7 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile4_frame.place(relx=9 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile5_frame.place(relx=11 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile6_frame.place(relx=13 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile7_frame.place(relx=15 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile8_frame.place(relx=17 / x, rely=1 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile9_frame.place(relx=17 / x, rely=3 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile10_frame.place(relx=17 / x, rely=5 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile11_frame.place(relx=17 / x, rely=7 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile12_frame.place(relx=17 / x, rely=9 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile13_frame.place(relx=17 / x, rely=11 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile14_frame.place(relx=17 / x, rely=13 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile15_frame.place(relx=17 / x, rely=15 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile16_frame.place(relx=17 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile17_frame.place(relx=15 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile18_frame.place(relx=13 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile19_frame.place(relx=11 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile20_frame.place(relx=9 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile21_frame.place(relx=7 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile22_frame.place(relx=5 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile23_frame.place(relx=3 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile24_frame.place(relx=1 / x, rely=17 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile25_frame.place(relx=1 / x, rely=15 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile26_frame.place(relx=1 / x, rely=13 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile27_frame.place(relx=1 / x, rely=11 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile28_frame.place(relx=1 / x, rely=9 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile29_frame.place(relx=1 / x, rely=7 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile30_frame.place(relx=1 / x, rely=5 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile31_frame.place(relx=1 / x, rely=3 / x, anchor=ctk.CENTER,
                                relwidth=1 / y - gap, relheight=1 / y - gap)

        # Child Frames For Main Frame
        self.player_one_frame.place(relx=0.1, rely=0.5, anchor=ctk.CENTER, relwidth=0.18, relheight=0.98)
        self.board_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=0.6, relheight=0.98)
        self.player_two_frame.place(relx=0.9, rely=0.5, anchor=ctk.CENTER, relwidth=0.18, relheight=0.98)
        self.mid_board_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=0.76, relheight=0.76)

        # Main Frames
        self.game_frame.pack(fill=ctk.BOTH, expand=1)

        self.show_dice_result(self.player_one.throw_dice())

    def show_tile_stats(self, status, frame, tile):
        # Delete Widgets
        for widget in frame.winfo_children():
            widget.destroy()

        # Create Child Frame For Frame
        card_frame = ctk.CTkFrame(master=frame, fg_color=CARD_COLOR_1)

        # Widgets For Frame
        name_label = ctk.CTkLabel(master=frame, text=tile.name)
        if status == "country":
            name_title = ctk.CTkLabel(master=frame, text="Raj:")
            owner_title = ctk.CTkLabel(master=frame, text="Właściciel:")
            owner_label = ctk.CTkLabel(master=frame, text=tile.return_owner())
            buy_cost_title = ctk.CTkLabel(master=frame, text="Wartość kupna:")
            buy_cost_label = ctk.CTkLabel(master=frame, text=tile.buy_cost)
            sell_cost_title = ctk.CTkLabel(master=frame, text="Wartość sprzedaży:")
            sell_cost_label = ctk.CTkLabel(master=frame, text=tile.sell_cost)
            rent_title = ctk.CTkLabel(master=frame, text="Wartość czynszu:")
            rent_label = ctk.CTkLabel(master=frame, text=tile.rent)
        elif status == "start":
            value_label = ctk.CTkLabel(master=frame, text=f"Za wejśćie na to pole\ndostaniesz {tile.value}")
        elif status == "prison":
            value_label = ctk.CTkLabel(master=frame,
                                       text=f"Jeśli wejdziesz do więzienia\nstracisz {tile.value}.\nJeśli tyle nie masz\nto stracisz wszystkie pieniądze")
        elif status == "parking":
            value_label = ctk.CTkLabel(master=frame, text=f"Za postój na parkingu\nzapłacisz {tile.value}")
        elif status == "take_card":
            value_label = ctk.CTkLabel(master=frame,
                                       text="Na tym polu pobierasz kartę,\nktóra może mieć efekt\npozytywny albo negatywny")
        elif status == "tax":
            value_label = ctk.CTkLabel(master=frame,
                                       text=f"Jeśli wejdziesz na to pole\nbędziesz zapłacić podatek\nod posiadanych krajów\nw wysokości {tile.value}\nza każdy posiadany kraj")

        # Widgets For Card Frame
        color_banner = ctk.CTkLabel(master=card_frame, fg_color="#b50b49", text=tile.name, bg_color="#262626",
                                    font=self.card_title_game_view)

        # Layout For Frame
        card_frame.place(relx=0.25, rely=0.50, anchor=ctk.CENTER, relwidth=0.25, relheight=0.8)
        if status == "country":
            name_title.place(relx=4 / 6, rely=1 / 6, anchor=ctk.CENTER)
            name_label.place(relx=5 / 6, rely=1 / 6, anchor=ctk.CENTER)
            owner_title.place(relx=4 / 6, rely=2 / 6, anchor=ctk.CENTER)
            owner_label.place(relx=5 / 6, rely=2 / 6, anchor=ctk.CENTER)
            buy_cost_title.place(relx=4 / 6, rely=3 / 6, anchor=ctk.CENTER)
            buy_cost_label.place(relx=5 / 6, rely=3 / 6, anchor=ctk.CENTER)
            sell_cost_title.place(relx=4 / 6, rely=4 / 6, anchor=ctk.CENTER)
            sell_cost_label.place(relx=5 / 6, rely=4 / 6, anchor=ctk.CENTER)
            rent_title.place(relx=4 / 6, rely=5 / 6, anchor=ctk.CENTER)
            rent_label.place(relx=5 / 6, rely=5 / 6, anchor=ctk.CENTER)
        else:
            name_label.place(relx=0.75, rely=1 / 6, anchor=ctk.CENTER)
            value_label.place(relx=0.75, rely=3 / 6, anchor=ctk.CENTER)

        # Layout For Card Frame
        color_banner.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        # Frame
        frame.place(relx=0.5, rely=0.25, anchor=ctk.CENTER, relwidth=1, relheight=0.5)
        frame.configure(fg_color="transparent")

    def show_dice_result(self, dice):
        # Variables
        dice_point_relwidth = 0.2
        dice_point_relheight = 0.2
        self.dice = dice

        # Font
        self.dice_result_font = ctk.CTkFont(family=FONT_1, size=128, weight="bold")

        # Functions
        def place_dice_points(dice_result, dice1, dice2, dice3, dice4, dice5, dice6):
            if dice_result == 1:
                dice1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
            elif dice_result == 2:
                dice1.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice2.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
            elif dice_result == 3:
                dice1.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice2.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice3.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
            elif dice_result == 4:
                dice1.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice2.place(relx=0.25, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice3.place(relx=0.75, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice4.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
            elif dice_result == 5:
                dice1.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice2.place(relx=0.25, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice3.place(relx=0.75, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice4.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice5.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
            elif dice_result == 6:
                dice1.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice2.place(relx=0.75, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice3.place(relx=0.25, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice4.place(relx=0.75, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice5.place(relx=0.25, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)
                dice6.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                            relheight=dice_point_relheight)

        # Create Frame
        self.dice_frame = ctk.CTkFrame(master=self.mid_board_frame)

        # Create Child Frames
        self.dice1_frame = ctk.CTkFrame(master=self.dice_frame, fg_color=DICE_COLOR_1)
        self.dice2_frame = ctk.CTkFrame(master=self.dice_frame, fg_color=DICE_COLOR_1)

        # Widgets
        self.dice_point_1 = ctk.CTkLabel(master=self.dice1_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_2 = ctk.CTkLabel(master=self.dice1_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_3 = ctk.CTkLabel(master=self.dice1_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_4 = ctk.CTkLabel(master=self.dice1_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_5 = ctk.CTkLabel(master=self.dice1_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_6 = ctk.CTkLabel(master=self.dice1_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_7 = ctk.CTkLabel(master=self.dice2_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_8 = ctk.CTkLabel(master=self.dice2_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_9 = ctk.CTkLabel(master=self.dice2_frame, fg_color=DICE_POINT_COLOR_1,
                                         text="", corner_radius=20)
        self.dice_point_10 = ctk.CTkLabel(master=self.dice2_frame, fg_color=DICE_POINT_COLOR_1,
                                          text="", corner_radius=20)
        self.dice_point_11 = ctk.CTkLabel(master=self.dice2_frame, fg_color=DICE_POINT_COLOR_1,
                                          text="", corner_radius=20)
        self.dice_point_12 = ctk.CTkLabel(master=self.dice2_frame, fg_color=DICE_POINT_COLOR_1,
                                          text="", corner_radius=20)
        self.dice_result_label = ctk.CTkLabel(master=self.dice_frame, text=self.dice["result"],
                                              font=self.dice_result_font)

        # Layout
        place_dice_points(dice_result=self.dice["dice1"],
                          dice1=self.dice_point_1, dice2=self.dice_point_2,
                          dice3=self.dice_point_3, dice4=self.dice_point_4,
                          dice5=self.dice_point_5, dice6=self.dice_point_6)
        place_dice_points(dice_result=self.dice["dice2"],
                          dice1=self.dice_point_7, dice2=self.dice_point_8,
                          dice3=self.dice_point_9, dice4=self.dice_point_10,
                          dice5=self.dice_point_11, dice6=self.dice_point_12)
        self.dice_result_label.place(relx=0.75, rely=0.5, anchor=ctk.CENTER)

        # Child Frame
        self.dice1_frame.place(relx=1 / 6, rely=0.5, anchor=ctk.CENTER, relwidth=0.15, relheight=0.3)
        self.dice2_frame.place(relx=2 / 6, rely=0.5, anchor=ctk.CENTER, relwidth=0.15, relheight=0.3)

        # Frame
        self.dice_frame.place(relx=0.5, rely=0.75, anchor=ctk.CENTER, relwidth=1, relheight=0.5)

    def confirm_exit(self, event):
        result = messagebox.askquestion("Potwierdzenie", "Czy na pewno chcesz wyjść?")
        if result == "yes":
            self.master.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    app = GameApp(root)
    root.mainloop()
