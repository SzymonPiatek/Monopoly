import customtkinter as ctk
from tkinter import messagebox, colorchooser

from classes import Player, Tile
from settings import *


def change_frame(old_frame, new_frame):
    old_frame.destroy()
    new_frame()


def place_player_frame_widgets(name_label, money_title, money_label, country_title, country_label, color):
    name_label.place(relx=0.5, rely=0.04, anchor=ctk.CENTER, relwidth=1, relheight=0.08)
    money_title.place(relx=0.5, rely=0.14, anchor=ctk.CENTER, relwidth=1)
    money_label.place(relx=0.5, rely=0.19, anchor=ctk.CENTER)
    country_title.place(relx=0.5, rely=0.26, anchor=ctk.CENTER, relwidth=1)
    country_label.place(relx=0.5, rely=0.31, anchor=ctk.CENTER)

    # Configure
    name_label.configure(fg_color=color)


def place_tile_areas(tile_list: list):
    for tile in tile_list:
        tile.pack(fill=ctk.BOTH, expand=True)


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

    def game_view(self):
        # Fonts
        self.font_label_game_view = ctk.CTkFont(family=FONT_1, size=24)
        self.font_label_name_game_view = ctk.CTkFont(family=FONT_1, size=40, weight="bold")
        self.font_title_game_view = ctk.CTkFont(family=FONT_1, size=32, weight="bold")
        self.card_title_game_view = ctk.CTkFont(family=FONT_1, size=32, weight="bold")

        # Countries
        self.tile0 = Tile(tile_type="special", name="Start", value=self.start_value, location=0)
        self.tile1 = Tile(tile_type="country", name="Polska", value=300, location=1)
        self.tile2 = Tile(tile_type="country", name="Czechy", value=250, location=2)
        self.tile3 = Tile(tile_type="country", name="Słowacja", value=250, location=3)
        self.tile4 = Tile(tile_type="special", name="Pobierz kartę", value=0, location=4)
        self.tile5 = Tile(tile_type="country", name="Niemcy", value=450, location=5)
        self.tile6 = Tile(tile_type="country", name="Holandia", value=350, location=6)
        self.tile7 = Tile(tile_type="country", name="Luksemburg", value=450, location=7)
        self.tile8 = Tile(tile_type="special", name="Więzienie", value=1000, location=8)
        self.tile9 = Tile(tile_type="country", name="Belgia", value=300, location=9)
        self.tile10 = Tile(tile_type="country", name="Francja", value=500, location=10)
        self.tile11 = Tile(tile_type="country", name="Anglia", value=450, location=11)
        self.tile12 = Tile(tile_type="special", name="Pobierz kartę", value=0, location=12)
        self.tile13 = Tile(tile_type="country", name="Hiszpania", value=350, location=13)
        self.tile14 = Tile(tile_type="country", name="Portugalia", value=300, location=14)
        self.tile15 = Tile(tile_type="country", name="Włochy", value=400, location=15)
        self.tile16 = Tile(tile_type="special", name="Parking", value=self.parking_value, location=16)
        self.tile17 = Tile(tile_type="country", name="Litwa", value=250, location=17)
        self.tile18 = Tile(tile_type="country", name="Estonia", value=250, location=18)
        self.tile19 = Tile(tile_type="country", name="Łotwa", value=200, location=19)
        self.tile20 = Tile(tile_type="special", name="Pobierz kartę", value=0, location=20)
        self.tile21 = Tile(tile_type="country", name="Węgry", value=300, location=21)
        self.tile22 = Tile(tile_type="country", name="Rumunia", value=300, location=22)
        self.tile23 = Tile(tile_type="country", name="Mołdawia", value=200, location=23)
        self.tile24 = Tile(tile_type="special", name="Podatki", value=10, location=24)
        self.tile25 = Tile(tile_type="country", name="Bułgaria", value=300, location=25)
        self.tile26 = Tile(tile_type="country", name="Serbia", value=250, location=26)
        self.tile27 = Tile(tile_type="country", name="Chorwacja", value=300, location=27)
        self.tile28 = Tile(tile_type="special", name="Pobierz kartę", value=0, location=28)
        self.tile29 = Tile(tile_type="country", name="Grecja", value=250, location=29)
        self.tile30 = Tile(tile_type="country", name="Albania", value=250, location=30)
        self.tile31 = Tile(tile_type="country", name="Turcja", value=350, location=31)

        self.board = [self.tile0, self.tile1, self.tile2, self.tile3,
                      self.tile4, self.tile5, self.tile6, self.tile7,
                      self.tile8, self.tile9, self.tile10, self.tile11,
                      self.tile12, self.tile13, self.tile14, self.tile15,
                      self.tile16, self.tile17, self.tile18, self.tile19,
                      self.tile20, self.tile21, self.tile22, self.tile23,
                      self.tile24, self.tile25, self.tile26, self.tile27,
                      self.tile28, self.tile29, self.tile30, self.tile31]

        # Players
        self.player_one = Player(name=self.player_one_name,
                                 start_money=self.start_money,
                                 color=self.player_one_color)
        self.player_two = Player(name=self.player_two_name,
                                 start_money=self.start_money,
                                 color=self.player_two_color)

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

        # Players Widgets
        (self.player_one_name_label, self.player_one_money_title,
         self.player_one_money_label, self.player_one_country_title,
         self.player_one_country_label) = self.create_player_widgets(frame=self.player_one_frame,
                                                                     player=self.player_one)
        (self.player_two_name_label, self.player_two_money_title,
         self.player_two_money_label, self.player_two_country_title,
         self.player_two_country_label) = self.create_player_widgets(frame=self.player_two_frame,
                                                                     player=self.player_two)

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
        place_player_frame_widgets(name_label=self.player_one_name_label,
                                   money_title=self.player_one_money_title,
                                   money_label=self.player_one_money_label,
                                   country_title=self.player_one_country_title,
                                   country_label=self.player_one_country_label,
                                   color=self.player_one_color)

        # Player Two Layout
        place_player_frame_widgets(name_label=self.player_two_name_label,
                                   money_title=self.player_two_money_title,
                                   money_label=self.player_two_money_label,
                                   country_title=self.player_two_country_title,
                                   country_label=self.player_two_country_label,
                                   color=self.player_two_color)

        # Board Layout
        place_tile_areas(tile_list=[
            self.tile0_area, self.tile1_area, self.tile2_area, self.tile3_area,
            self.tile4_area, self.tile5_area, self.tile6_area, self.tile7_area,
            self.tile8_area, self.tile9_area, self.tile10_area, self.tile11_area,
            self.tile12_area, self.tile13_area, self.tile14_area, self.tile15_area,
            self.tile16_area, self.tile17_area, self.tile18_area, self.tile19_area,
            self.tile20_area, self.tile21_area, self.tile22_area, self.tile23_area,
            self.tile24_area, self.tile25_area, self.tile26_area, self.tile27_area,
            self.tile28_area, self.tile29_area, self.tile30_area, self.tile31_area
        ])

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

    def set_player_view(self):
        # Create Frame
        self.menu_frame = ctk.CTkFrame(master=self.master)

        # Fonts
        self.font_label_set_player_view = ctk.CTkFont(family=FONT_1, size=48, weight="bold")
        self.font_entry_set_player_view = ctk.CTkFont(family=FONT_1, size=32, weight="bold")
        self.font_button_set_player_view = self.font_button_main_menu

        # Players Widgets
        self.player_one_choose_color = ctk.CTkButton(master=self.menu_frame,
                                                     text="Wybierz kolor",
                                                     command=lambda: self.choose_color_button(
                                                         self.player_one_choose_color),
                                                     font=self.font_entry_set_player_view)
        self.player_two_choose_color = ctk.CTkButton(master=self.menu_frame,
                                                     text="Wybierz kolor",
                                                     command=lambda: self.choose_color_button(
                                                         self.player_two_choose_color),
                                                     font=self.font_entry_set_player_view)

        self.player_one_label, self.player_one_entry = self.create_set_player_view_widgets(
            label_text="Gracz 1",
            entry_text="Wybierz kolor")
        self.player_two_label, self.player_two_entry = self.create_set_player_view_widgets(
            label_text="Gracz 2",
            entry_text="Wybierz kolor")

        # Game settings Widgets
        self.start_money_label, self.start_money_entry = self.create_set_player_view_widgets(
            label_text="Stan konta na start",
            entry_text="Domyślnie 2000")
        self.start_value_label, self.start_value_entry = self.create_set_player_view_widgets(
            label_text="Bonus za pole Start",
            entry_text="Domyślnie 500")
        self.parking_value_label, self.parking_value_entry = self.create_set_player_view_widgets(
            label_text="Cena za parking",
            entry_text="Domyślnie 50")

        # Widgets
        self.start_game_button = ctk.CTkButton(master=self.menu_frame,
                                               text="Start",
                                               command=self.start_game_button_click,
                                               font=self.font_button_set_player_view,
                                               fg_color=BUTTON_COLOR_1,
                                               hover_color=HOVER_BUTTON_COLOR_1)

        # Layout
        # First row
        self.place_set_player_view_widgets(x=0, y=0, label=self.player_one_label,
                                           entry=self.player_one_entry, button=self.player_one_choose_color)
        self.place_set_player_view_widgets(x=0.5, y=0, label=self.player_two_label,
                                           entry=self.player_two_entry, button=self.player_two_choose_color)

        # Second row
        self.place_set_player_view_widgets(x=0, y=0.3, label=self.start_money_label,
                                           entry=self.start_money_entry, button=None)
        self.place_set_player_view_widgets(x=0.5, y=0.3, label=self.parking_value_label,
                                           entry=self.parking_value_entry, button=None)

        # Last row
        self.start_game_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER, relwidth=0.15, relheight=0.08)

        # Frame
        self.menu_frame.pack(fill=ctk.BOTH, expand=1)

    def choose_color_button(self, button):
        color = colorchooser.askcolor()[1]
        button.configure(fg_color=color)

    def create_set_player_view_widgets(self, label_text: str, entry_text: str):
        label = ctk.CTkLabel(master=self.menu_frame,
                             text=label_text,
                             font=self.font_label_set_player_view)
        entry = ctk.CTkEntry(master=self.menu_frame,
                             placeholder_text=entry_text,
                             font=self.font_entry_set_player_view)
        return label, entry

    def place_set_player_view_widgets(self, x: float, y: float, label, entry, button):
        label.place(relx=0.25 + x, rely=0.2 + y, anchor=ctk.CENTER)
        entry.place(relx=0.25 + x, rely=0.27 + y, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)
        if button:
            button.place(relx=0.25 + x, rely=0.34 + y, anchor=ctk.CENTER, relwidth=0.2, relheight=0.05)

    def create_player_widgets(self, frame, player):
        name_label = ctk.CTkLabel(master=frame,
                                  text=player.name.upper(),
                                  font=self.font_label_name_game_view)
        money_title = ctk.CTkLabel(master=frame,
                                   text="Saldo:",
                                   font=self.font_title_game_view)
        money_label = ctk.CTkLabel(master=frame,
                                   text=f"{player.money}$",
                                   font=self.font_label_game_view)
        country_title = ctk.CTkLabel(master=frame,
                                     text="Lista krajów:",
                                     font=self.font_title_game_view)
        country_label = ctk.CTkLabel(master=frame,
                                     text=player.country_list(),
                                     font=self.font_label_game_view)
        return name_label, money_title, money_label, country_title, country_label

    def start_game_button_click(self):
        # Set variables
        # Player settings
        self.player_one_name = self.player_one_entry.get()
        self.player_one_color = self.player_one_choose_color.cget("fg_color")
        self.player_two_name = self.player_two_entry.get()
        self.player_two_color = self.player_two_choose_color.cget("fg_color")
        # Game settings
        self.start_money = self.start_money_entry.get()
        self.start_value = self.start_value_entry.get()
        self.parking_value = self.parking_value_entry.get()
        # Change Frame
        change_frame(old_frame=self.menu_frame, new_frame=self.game_view)

    def show_tile_stats(self, status, frame, tile):
        # Delete Widgets
        for widget in frame.winfo_children():
            widget.destroy()

        # Create Child Frame For Frame
        card_frame = ctk.CTkFrame(master=frame, fg_color=CARD_COLOR_1)

        # Widgets For Frame
        name_label = ctk.CTkLabel(master=frame, text=tile.name)
        if status == "country":
            name_title = ctk.CTkLabel(master=frame, text="Kraj:")
            owner_title = ctk.CTkLabel(master=frame, text="Właściciel:")
            owner_label = ctk.CTkLabel(master=frame, text=tile.return_owner())
            buy_cost_title = ctk.CTkLabel(master=frame, text="Wartość kupna:")
            buy_cost_label = ctk.CTkLabel(master=frame, text=f"{tile.buy_cost}$")
            sell_cost_title = ctk.CTkLabel(master=frame, text="Wartość sprzedaży:")
            sell_cost_label = ctk.CTkLabel(master=frame, text=f"{tile.sell_cost}$")
            rent_title = ctk.CTkLabel(master=frame, text="Wartość czynszu:")
            rent_label = ctk.CTkLabel(master=frame, text=f"{tile.rent_cost}$")
        elif status == "start":
            value_label = ctk.CTkLabel(master=frame, text=f"Za wejśćie na to pole\ndostaniesz {tile.effect_value}$")
        elif status == "prison":
            value_label = ctk.CTkLabel(master=frame,
                                       text=f"Jeśli wejdziesz do więzienia\nstracisz {tile.effect_value}$.\nJeśli tyle nie masz\nto stracisz wszystkie pieniądze")
        elif status == "parking":
            value_label = ctk.CTkLabel(master=frame, text=f"Za postój na parkingu\nzapłacisz {tile.effect_value}$")
        elif status == "take_card":
            value_label = ctk.CTkLabel(master=frame,
                                       text="Na tym polu pobierasz kartę,\nktóra może mieć efekt\npozytywny albo negatywny")
        elif status == "tax":
            value_label = ctk.CTkLabel(master=frame,
                                       text=f"Jeśli wejdziesz na to pole\nbędziesz zapłacić podatek\nod posiadanych krajów\nw wysokości {tile.effect_value}%\nza każdy posiadany kraj")

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

    def create_dice_point_label(self, frame):
        return ctk.CTkLabel(master=frame, fg_color=DICE_POINT_COLOR_1,
                            text="", corner_radius=20)

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
        self.dice_frame = ctk.CTkFrame(master=self.mid_board_frame, fg_color="transparent")

        # Create Child Frames
        self.dice1_frame = ctk.CTkFrame(master=self.dice_frame, fg_color=DICE_COLOR_1)
        self.dice2_frame = ctk.CTkFrame(master=self.dice_frame, fg_color=DICE_COLOR_1)

        # Widgets
        self.dice_point_1 = self.create_dice_point_label(frame=self.dice1_frame)
        self.dice_point_2 = self.create_dice_point_label(frame=self.dice1_frame)
        self.dice_point_3 = self.create_dice_point_label(frame=self.dice1_frame)
        self.dice_point_4 = self.create_dice_point_label(frame=self.dice1_frame)
        self.dice_point_5 = self.create_dice_point_label(frame=self.dice1_frame)
        self.dice_point_6 = self.create_dice_point_label(frame=self.dice1_frame)
        self.dice_point_7 = self.create_dice_point_label(frame=self.dice2_frame)
        self.dice_point_8 = self.create_dice_point_label(frame=self.dice2_frame)
        self.dice_point_9 = self.create_dice_point_label(frame=self.dice2_frame)
        self.dice_point_10 = self.create_dice_point_label(frame=self.dice2_frame)
        self.dice_point_11 = self.create_dice_point_label(frame=self.dice2_frame)
        self.dice_point_12 = self.create_dice_point_label(frame=self.dice2_frame)

        self.dice_result_label = ctk.CTkLabel(master=self.dice_frame,
                                              text=self.dice["result"],
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
