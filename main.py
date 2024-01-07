import customtkinter as ctk
from tkinter import messagebox, colorchooser

from classes import Player, Tile
from settings import *


def change_frame(old_frame, new_frame):
    clear_frame(frame=old_frame)
    new_frame()


def place_player_frame_widgets(name_label, money_title, money_label, country_title,
                               country_label, location_title, location_label, turn_label , color):
    name_label.place(relx=0.5, rely=0.04, anchor=ctk.CENTER, relwidth=1, relheight=0.08)
    money_title.place(relx=0.5, rely=0.14, anchor=ctk.CENTER)
    money_label.place(relx=0.5, rely=0.19, anchor=ctk.CENTER)
    location_title.place(relx=0.5, rely=0.24, anchor=ctk.CENTER)
    location_label.place(relx=0.5, rely=0.29, anchor=ctk.CENTER)
    country_title.place(relx=0.5, rely=0.34, anchor=ctk.N)
    country_label.place(relx=0.5, rely=0.39, anchor=ctk.N)
    turn_label.place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

    # Configure
    name_label.configure(fg_color=color)


def place_tile_areas(tile_list: list):
    for tile in tile_list:
        tile.pack(fill=ctk.BOTH, expand=True)


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def check_set_player_value_type(value):
    if value:
        return int(value)
    else:
        return value


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
        # Start Main Menu
        self.font_title_main_menu = self.set_font(size=128)
        self.font_button_main_menu = self.set_font(size=48)
        # Set Player Menu
        self.font_label_set_player_view = self.set_font(size=48)
        self.font_entry_set_player_view = self.set_font(size=32)
        self.font_button_set_player_view = self.set_font(size=48)
        # Game Board
        self.font_label_game_view = self.set_font(size=24)
        self.font_label_name_game_view = self.set_font(size=40)
        self.font_title_game_view = self.set_font(size=32)
        self.card_title_game_view = self.set_font(size=32)
        self.dice_result_font = self.set_font(size=128)

        # Bind
        self.master.bind("<Escape>", self.confirm_exit)

        # Main Menu
        self.start_game_menu_view()

    def set_font(self, size: int):
        return ctk.CTkFont(family=FONT_1, size=size, weight="bold")

    def start_game_menu_view(self):
        # Create Frame
        self.main_menu_frame = ctk.CTkFrame(master=self.master)

        # Create Widgets
        self.main_menu_label = ctk.CTkLabel(master=self.main_menu_frame,
                                            text="MONOPOLY", font=self.font_title_main_menu)
        self.main_menu_button = ctk.CTkButton(master=self.main_menu_frame,
                                              text="Graj",
                                              command=lambda: change_frame(old_frame=self.master,
                                                                           new_frame=self.set_player_view),
                                              font=self.font_button_main_menu,
                                              fg_color=BUTTON_COLOR_1,
                                              hover_color=HOVER_BUTTON_COLOR_1)

        # Place Widgets
        self.main_menu_label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        self.main_menu_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER, relwidth=0.15, relheight=0.08)

        # Place Frame
        self.main_menu_frame.pack(fill=ctk.BOTH, expand=1)

    def set_player_view(self):
        # Create Frame
        self.menu_frame = ctk.CTkFrame(master=self.master)

        # Create Widgets
        # Player 1
        self.player_one_choose_color = ctk.CTkButton(
            master=self.menu_frame,
            text="Wybierz kolor",
            command=lambda: self.choose_color_button(self.player_one_choose_color),
            font=self.font_entry_set_player_view)
        self.player_one_label, self.player_one_entry = self.create_set_player_view_widgets(
            label_text="Gracz 1",
            entry_text="Wybierz kolor")

        # Player 2
        self.player_two_choose_color = ctk.CTkButton(
            master=self.menu_frame,
            text="Wybierz kolor",
            command=lambda: self.choose_color_button(self.player_two_choose_color),
            font=self.font_entry_set_player_view)
        self.player_two_label, self.player_two_entry = self.create_set_player_view_widgets(
            label_text="Gracz 2",
            entry_text="Wybierz kolor")

        # Game Settings
        self.start_money_label, self.start_money_entry = self.create_set_player_view_widgets(
            label_text="Saldo początkowe",
            entry_text="Domyślnie 2000")
        self.start_value_label, self.start_value_entry = self.create_set_player_view_widgets(
            label_text="Bonus za pole Start",
            entry_text="Domyślnie 500")
        self.parking_value_label, self.parking_value_entry = self.create_set_player_view_widgets(
            label_text="Cena za parking",
            entry_text="Domyślnie 50")
        self.tax_value_label, self.tax_value_entry = self.create_set_player_view_widgets(
            label_text="Procent podatku",
            entry_text="Domyślnie 10")

        # Start Game Button
        self.start_game_button = ctk.CTkButton(master=self.menu_frame,
                                               text="Start",
                                               command=self.start_game_button_on_click,
                                               font=self.font_button_set_player_view,
                                               fg_color=BUTTON_COLOR_1,
                                               hover_color=HOVER_BUTTON_COLOR_1)

        # Place Widgets
        # First Row
        self.place_set_player_view_widgets(x=0, y=0, label=self.player_one_label,
                                           entry=self.player_one_entry, button=self.player_one_choose_color)
        self.place_set_player_view_widgets(x=0.25, y=0, label=self.start_money_label,
                                           entry=self.start_money_entry, button=None)
        self.place_set_player_view_widgets(x=0.5, y=0, label=self.player_two_label,
                                           entry=self.player_two_entry, button=self.player_two_choose_color)

        # Second Row
        self.place_set_player_view_widgets(x=0, y=0.3, label=self.start_value_label,
                                           entry=self.start_value_entry, button=None)
        self.place_set_player_view_widgets(x=0.25, y=0.3, label=self.parking_value_label,
                                           entry=self.parking_value_entry, button=None)
        self.place_set_player_view_widgets(x=0.5, y=0.3, label=self.tax_value_label,
                                           entry=self.tax_value_entry, button=None)

        # Last Row
        self.start_game_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER, relwidth=0.15, relheight=0.08)

        # Place Frame
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

    def start_game_button_on_click(self):
        # Set Variables
        # Player settings
        self.player_one_name = self.player_one_entry.get()
        self.player_one_color = self.player_one_choose_color.cget("fg_color")
        self.player_two_name = self.player_two_entry.get()
        self.player_two_color = self.player_two_choose_color.cget("fg_color")
        # Game settings
        self.start_money = check_set_player_value_type(self.start_money_entry.get())
        self.start_value = check_set_player_value_type(self.start_value_entry.get())
        self.parking_value = check_set_player_value_type(self.parking_value_entry.get())
        self.tax_value = check_set_player_value_type(self.tax_value_entry.get())
        # Change Frame
        change_frame(old_frame=self.master, new_frame=self.game_view)

    def game_view(self):
        # Create Countries
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
        self.tile24 = Tile(tile_type="special", name="Podatki", value=self.tax_value, location=24)
        self.tile25 = Tile(tile_type="country", name="Bułgaria", value=300, location=25)
        self.tile26 = Tile(tile_type="country", name="Serbia", value=250, location=26)
        self.tile27 = Tile(tile_type="country", name="Chorwacja", value=300, location=27)
        self.tile28 = Tile(tile_type="special", name="Pobierz kartę", value=0, location=28)
        self.tile29 = Tile(tile_type="country", name="Grecja", value=250, location=29)
        self.tile30 = Tile(tile_type="country", name="Albania", value=250, location=30)
        self.tile31 = Tile(tile_type="country", name="Turcja", value=350, location=31)

        # Create Board
        self.board = [self.tile0, self.tile1, self.tile2, self.tile3,
                      self.tile4, self.tile5, self.tile6, self.tile7,
                      self.tile8, self.tile9, self.tile10, self.tile11,
                      self.tile12, self.tile13, self.tile14, self.tile15,
                      self.tile16, self.tile17, self.tile18, self.tile19,
                      self.tile20, self.tile21, self.tile22, self.tile23,
                      self.tile24, self.tile25, self.tile26, self.tile27,
                      self.tile28, self.tile29, self.tile30, self.tile31]

        # Create Players
        self.player_one = Player(name=self.player_one_name,
                                 start_money=self.start_money,
                                 color=self.player_one_color)

        self.player_two = Player(name=self.player_two_name,
                                 start_money=self.start_money,
                                 color=self.player_two_color)

        # Create Frames
        # Main Frames
        self.player_one_frame = ctk.CTkFrame(master=self.master)
        self.player_two_frame = ctk.CTkFrame(master=self.master)
        self.board_frame = ctk.CTkFrame(master=self.master)

        # Child Frames
        self.mid_board_frame = ctk.CTkFrame(master=self.board_frame, fg_color="transparent")
        self.up_mid_board_frame = ctk.CTkFrame(master=self.mid_board_frame, fg_color="transparent")
        self.down_mid_board_frame = ctk.CTkFrame(master=self.mid_board_frame, fg_color="transparent")
        self.left_down_mid_board_frame = ctk.CTkFrame(master=self.down_mid_board_frame, fg_color="transparent")
        self.right_down_mid_board_frame = ctk.CTkFrame(master=self.down_mid_board_frame, fg_color="transparent")

        # Create Widgets
        # Player Widgets
        (self.player_one_name_label,
         self.player_one_money_title,
         self.player_one_money_label,
         self.player_one_country_title,
         self.player_one_country_label,
         self.player_one_location_title,
         self.player_one_location_label,
         self.player_one_turn_label) = self.create_player_widgets(frame=self.player_one_frame,
                                                                  player=self.player_one)
        (self.player_two_name_label,
         self.player_two_money_title,
         self.player_two_money_label,
         self.player_two_country_title,
         self.player_two_country_label,
         self.player_two_location_title,
         self.player_two_location_label,
         self.player_two_turn_label) = self.create_player_widgets(frame=self.player_two_frame,
                                                                  player=self.player_two)

        # Tile Widgets
        self.tile0_area = self.create_tile_button(tile=self.tile0, status="start")
        self.tile1_area = self.create_tile_button(tile=self.tile1, status="country")
        self.tile2_area = self.create_tile_button(tile=self.tile2, status="country")
        self.tile3_area = self.create_tile_button(tile=self.tile3, status="country")
        self.tile4_area = self.create_tile_button(tile=self.tile4, status="take_card")
        self.tile5_area = self.create_tile_button(tile=self.tile5, status="country")
        self.tile6_area = self.create_tile_button(tile=self.tile6, status="country")
        self.tile7_area = self.create_tile_button(tile=self.tile7, status="country")
        self.tile8_area = self.create_tile_button(tile=self.tile8, status="prison")
        self.tile9_area = self.create_tile_button(tile=self.tile9, status="country")
        self.tile10_area = self.create_tile_button(tile=self.tile10, status="country")
        self.tile11_area = self.create_tile_button(tile=self.tile11, status="country")
        self.tile12_area = self.create_tile_button(tile=self.tile12, status="take_card")
        self.tile13_area = self.create_tile_button(tile=self.tile13, status="country")
        self.tile14_area = self.create_tile_button(tile=self.tile14, status="country")
        self.tile15_area = self.create_tile_button(tile=self.tile15, status="country")
        self.tile16_area = self.create_tile_button(tile=self.tile16, status="parking")
        self.tile17_area = self.create_tile_button(tile=self.tile17, status="country")
        self.tile18_area = self.create_tile_button(tile=self.tile18, status="country")
        self.tile19_area = self.create_tile_button(tile=self.tile19, status="country")
        self.tile20_area = self.create_tile_button(tile=self.tile20, status="take_card")
        self.tile21_area = self.create_tile_button(tile=self.tile21, status="country")
        self.tile22_area = self.create_tile_button(tile=self.tile22, status="country")
        self.tile23_area = self.create_tile_button(tile=self.tile23, status="country")
        self.tile24_area = self.create_tile_button(tile=self.tile24, status="tax")
        self.tile25_area = self.create_tile_button(tile=self.tile25, status="country")
        self.tile26_area = self.create_tile_button(tile=self.tile26, status="country")
        self.tile27_area = self.create_tile_button(tile=self.tile27, status="country")
        self.tile28_area = self.create_tile_button(tile=self.tile28, status="take_card")
        self.tile29_area = self.create_tile_button(tile=self.tile29, status="country")
        self.tile30_area = self.create_tile_button(tile=self.tile30, status="country")
        self.tile31_area = self.create_tile_button(tile=self.tile31, status="country")

        self.board_widgets = [
            self.tile0_area, self.tile1_area, self.tile2_area, self.tile3_area,
            self.tile4_area, self.tile5_area, self.tile6_area, self.tile7_area,
            self.tile8_area, self.tile9_area, self.tile10_area, self.tile11_area,
            self.tile12_area, self.tile13_area, self.tile14_area, self.tile15_area,
            self.tile16_area, self.tile17_area, self.tile18_area, self.tile19_area,
            self.tile20_area, self.tile21_area, self.tile22_area, self.tile23_area,
            self.tile24_area, self.tile25_area, self.tile26_area, self.tile27_area,
            self.tile28_area, self.tile29_area, self.tile30_area, self.tile31_area
        ]

        # Configure Widgets
        # Tile Button
        for widget in self.board_widgets:
            self.change_button_state(widget)

        # Player Action Widget
        self.start_game_button = ctk.CTkButton(master=self.mid_board_frame,
                                               text="Zaczynamy!",
                                               command=self.start_game_button_func)

        # Place Widgets
        # Player Widgets
        place_player_frame_widgets(name_label=self.player_one_name_label,
                                   money_title=self.player_one_money_title,
                                   money_label=self.player_one_money_label,
                                   country_title=self.player_one_country_title,
                                   country_label=self.player_one_country_label,
                                   location_title=self.player_one_location_title,
                                   location_label=self.player_one_location_label,
                                   turn_label=self.player_one_turn_label,
                                   color=self.player_one_color)
        place_player_frame_widgets(name_label=self.player_two_name_label,
                                   money_title=self.player_two_money_title,
                                   money_label=self.player_two_money_label,
                                   country_title=self.player_two_country_title,
                                   country_label=self.player_two_country_label,
                                   location_title=self.player_two_location_title,
                                   location_label=self.player_two_location_label,
                                   turn_label=self.player_two_turn_label,
                                   color=self.player_two_color)

        # Board Widgets
        y = 9
        x = y * 2
        gap = 0.02
        self.tile0_area.place(relx=1 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile1_area.place(relx=3 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile2_area.place(relx=5 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile3_area.place(relx=7 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile4_area.place(relx=9 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile5_area.place(relx=11 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile6_area.place(relx=13 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile7_area.place(relx=15 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile8_area.place(relx=17 / x, rely=1 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile9_area.place(relx=17 / x, rely=3 / x, anchor=ctk.CENTER,
                              relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile10_area.place(relx=17 / x, rely=5 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile11_area.place(relx=17 / x, rely=7 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile12_area.place(relx=17 / x, rely=9 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile13_area.place(relx=17 / x, rely=11 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile14_area.place(relx=17 / x, rely=13 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile15_area.place(relx=17 / x, rely=15 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile16_area.place(relx=17 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile17_area.place(relx=15 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile18_area.place(relx=13 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile19_area.place(relx=11 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile20_area.place(relx=9 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile21_area.place(relx=7 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile22_area.place(relx=5 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile23_area.place(relx=3 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile24_area.place(relx=1 / x, rely=17 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile25_area.place(relx=1 / x, rely=15 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile26_area.place(relx=1 / x, rely=13 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile27_area.place(relx=1 / x, rely=11 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile28_area.place(relx=1 / x, rely=9 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile29_area.place(relx=1 / x, rely=7 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile30_area.place(relx=1 / x, rely=5 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)
        self.tile31_area.place(relx=1 / x, rely=3 / x, anchor=ctk.CENTER,
                               relwidth=1 / y - gap, relheight=1 / y - gap)

        # Player Action Widget
        self.start_game_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=0.4, relheight=0.4)

        # Place Frames
        # Child Frame
        self.mid_board_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=0.76, relheight=0.76)
        self.up_mid_board_frame.place(relx=0.5, rely=0.25, anchor=ctk.CENTER, relwidth=1, relheight=0.5)
        self.down_mid_board_frame.place(relx=0.5, rely=0.75, anchor=ctk.CENTER, relwidth=1, relheight=0.5)
        self.left_down_mid_board_frame.place(relx=0.25, rely=0.5, anchor=ctk.CENTER, relwidth=0.5, relheight=1)
        self.right_down_mid_board_frame.place(relx=0.75, rely=0.5, anchor=ctk.CENTER, relwidth=0.5, relheight=1)

        # Main Frames
        self.player_one_frame.place(relx=0.1, rely=0.5, anchor=ctk.CENTER, relwidth=0.18, relheight=0.98)
        self.board_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=0.6, relheight=0.98)
        self.player_two_frame.place(relx=0.9, rely=0.5, anchor=ctk.CENTER, relwidth=0.18, relheight=0.98)

    def start_game_button_func(self):
        self.start_game_button.destroy()
        for widget in self.board_widgets:
            self.change_button_state(widget)
        self.play_game(self.player_one)

    def change_button_state(self, button):
        if button.cget("state") == "normal":
            button.configure(state="disabled")
        else:
            button.configure(state="normal")

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
        location_title = ctk.CTkLabel(master=frame,
                                      text="Lokalizacja:",
                                      font=self.font_title_game_view)
        location_label = ctk.CTkLabel(master=frame,
                                      text=self.get_location_name(player=player),
                                      font=self.font_label_game_view)
        turn_label = ctk.CTkLabel(master=frame,
                                  text="",
                                  font=self.font_label_game_view)
        return (name_label, money_title, money_label, country_title,
                country_label, location_title, location_label, turn_label)

    def get_location_name(self, player):
        for tile in self.board:
            if tile.location == player.location:
                return tile.name

    def create_tile_button(self, tile, status: str):
        return ctk.CTkButton(master=self.board_frame,
                             text=tile.name,
                             command=lambda: self.show_tile_stats(tile=tile))

    def show_tile_stats(self, tile):
        # Delete Widgets
        clear_frame(frame=self.up_mid_board_frame)

        # Create Child Frame For Frame
        card_frame = ctk.CTkFrame(master=self.up_mid_board_frame, fg_color=CARD_COLOR_1)

        # Widgets For Frame
        name_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=tile.name)
        if tile.tile_type == "country":
            name_title = ctk.CTkLabel(master=self.up_mid_board_frame, text="Kraj:")
            owner_title = ctk.CTkLabel(master=self.up_mid_board_frame, text="Właściciel:")
            owner_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=tile.return_owner())
            buy_cost_title = ctk.CTkLabel(master=self.up_mid_board_frame, text="Wartość kupna:")
            buy_cost_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=f"{tile.buy_cost}$")
            sell_cost_title = ctk.CTkLabel(master=self.up_mid_board_frame, text="Wartość sprzedaży:")
            sell_cost_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=f"{tile.sell_cost}$")
            rent_title = ctk.CTkLabel(master=self.up_mid_board_frame, text="Wartość czynszu:")
            rent_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=f"{tile.rent_cost}$")
        elif tile.tile_type == "special":
            if tile.name == "Start":
                value_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=f"Za wejśćie na to pole\ndostaniesz {tile.effect_value}$")
            elif tile.name == "Więzienie":
                value_label = ctk.CTkLabel(master=self.up_mid_board_frame,
                                           text=f"Jeśli trafisz do więzienia\nstracisz {tile.effect_value}$.\nJeśli tyle nie masz,\n stracisz wszystkie swoje pieniądze")
            elif tile.name == "Parking":
                value_label = ctk.CTkLabel(master=self.up_mid_board_frame, text=f"Za postój na parkingu\nzapłacisz {tile.effect_value}$")
            elif tile.name == "Pobierz kartę":
                value_label = ctk.CTkLabel(master=self.up_mid_board_frame,
                                           text="Na tym polu pobierasz kartę,\nktóra może mieć efekt\npozytywny albo negatywny")
            elif tile.name == "Podatki":
                value_label = ctk.CTkLabel(master=self.up_mid_board_frame,
                                           text=f"Jeśli wejdziesz na to pole\nbędziesz zapłacić podatek\nod posiadanych krajów\nw wysokości {tile.effect_value}%\nza każdy posiadany kraj")

        # Widgets For Card Frame
        color_banner = ctk.CTkLabel(master=card_frame, fg_color=CARD_BANNER_1, text=tile.name, bg_color="#262626",
                                    font=self.card_title_game_view)

        # Layout For Frame
        card_frame.place(relx=0.25, rely=0.50, anchor=ctk.CENTER, relwidth=0.3, relheight=0.9)
        if tile.tile_type == "country":
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

    def play_game(self, player):
        # Clear Frame
        clear_frame(frame=self.up_mid_board_frame)
        clear_frame(frame=self.left_down_mid_board_frame)
        clear_frame(frame=self.right_down_mid_board_frame)

        # Create Widgets
        self.throw_dice_button = ctk.CTkButton(master=self.right_down_mid_board_frame,
                                               text="Rzuć kośćmi",
                                               command=lambda: self.player_throw_dice(player))

        if player.name == self.player_one.name:
            self.player_one_turn_label.configure(text="Twoja kolej!")
            self.player_two_turn_label.configure(text="")
        elif player.name == self.player_two.name:
            self.player_two_turn_label.configure(text="Twoja kolej!")
            self.player_one_turn_label.configure(text="")

        # Place Widgets
        self.throw_dice_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)

    def player_throw_dice(self, player):
        # Clear Frame
        clear_frame(frame=self.left_down_mid_board_frame)
        clear_frame(frame=self.right_down_mid_board_frame)

        # Throw Dice
        dice1, dice2, dice_result = player.throw_dice()
        self.show_dice_result(dice1, dice2, dice_result)

        # Player move
        self.player_move(player=player, dice=dice_result)

    def player_move(self, player, dice):
        # Change Player Location
        player.move(dice=dice, board=self.board)
        self.update_player_stats(player=player)

        # Change Player Location On A Board

        # Show Tile Stats
        for tile in self.board:
            if tile.location == player.location:
                self.show_tile_stats(tile)
                tile = tile
                break

        # Create Widgets
        self.player_can_buy_button = ctk.CTkButton(master=self.right_down_mid_board_frame,
                                                   text="Kup ten kraj",
                                                   command=lambda: self.player_buy_country(player=player,
                                                                                           tile=tile))
        self.player_can_sell_button = ctk.CTkButton(master=self.right_down_mid_board_frame,
                                                    text="Sprzedaj ten kraj",
                                                    command=lambda: self.player_sell_country(player=player,
                                                                                             tile=tile))
        if player.name == self.player_one.name:
            self.player_do_nothing_button = ctk.CTkButton(master=self.right_down_mid_board_frame,
                                                          text="Nic nie rób",
                                                          command=lambda: self.play_game(self.player_two))
        elif player.name == self.player_two.name:
            self.player_do_nothing_button = ctk.CTkButton(master=self.right_down_mid_board_frame,
                                                          text="Nic nie rób",
                                                          command=lambda: self.play_game(self.player_one))
        # Show Player Action
        if tile.tile_type == "country":
            if player != tile.owner and not tile.owner:
                if tile.buy_cost <= player.money:
                    self.player_can_buy_button.place(relx=0.5, rely=1/3, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)
                self.player_do_nothing_button.place(relx=0.5, rely=2/3, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)
            elif player == tile.owner:
                self.player_can_sell_button.place(relx=0.5, rely=1 / 3, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)
                self.player_do_nothing_button.place(relx=0.5, rely=2 / 3, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)
            elif player != tile.owner and tile.owner:
                tile.rent_pay(player=player)
                self.check_player_money(player=player)
                self.player_do_nothing_button.place(relx=0.5, rely=2 / 3, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)

        elif tile.tile_type == "special":
            if tile.name == "Start":
                tile.start_bonus(player=player)
            elif tile.name == "Pobierz kartę":
                tile.card_random_effect(player=player)
            elif tile.name == "Więzienie":
                tile.prison_pay(player=player)
            elif tile.name == "Parking":
                tile.parking_pay(player=player)
            elif tile.name == "Podatki":
                tile.tax_pay(player=player)
            self.update_player_stats(player=player)
            self.check_player_money(player=player)
            self.player_do_nothing_button.place(relx=0.5, rely=2 / 3, anchor=ctk.CENTER, relwidth=0.4, relheight=0.2)

    def check_player_money(self, player):
        if player.money < 0:
            if player.name == self.player_one.name:
                self.player_one_turn_label.configure(text="Przegrałeś")
                self.player_two_turn_label.configure(text="Wygrałeś")
            elif player.name == self.player_two.name:
                self.player_one_turn_label.configure(text="Wygrałeś")
                self.player_two_turn_label.configure(text="Przegrałeś")
            self.player_do_nothing_button.configure(text="Koniec gry",
                                                    command=lambda: self.master.destroy())

    def player_buy_country(self, player, tile):
        player.buy_country(tile)
        self.update_player_stats(player=player)
        if player.name == self.player_one.name:
            self.play_game(self.player_two)
        elif player.name == self.player_two.name:
            self.play_game(self.player_one)

    def player_sell_country(self, player, tile):
        player.sell_country(tile)
        self.update_player_stats(player=player)
        if player.name == self.player_one.name:
            self.play_game(self.player_two)
        elif player.name == self.player_two.name:
            self.play_game(self.player_one)

    def update_player_stats(self, player):
        if player.name == self.player_one.name:
            self.player_one_money_label.configure(text=f"{player.money}$")
            self.player_one_country_label.configure(text=player.country_list())
            self.player_one_location_label.configure(text=self.get_location_name(player=player))
        elif player.name == self.player_two.name:
            self.player_two_money_label.configure(text=f"{player.money}$")
            self.player_two_country_label.configure(text=player.country_list())
            self.player_two_location_label.configure(text=self.get_location_name(player=player))

    def show_dice_result(self, dice1, dice2, dice_result):
        # Variables
        dice_point_relwidth = 0.2
        dice_point_relheight = 0.2

        # Functions
        def place_dice_points(dice_score, dice_one, dice_two, dice_three, dice_four, dice_five, dice_six):
            if dice_score == 1:
                dice_one.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
            elif dice_score == 2:
                dice_one.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_two.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
            elif dice_score == 3:
                dice_one.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_two.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_three.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                 relheight=dice_point_relheight)
            elif dice_score == 4:
                dice_one.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_two.place(relx=0.25, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_three.place(relx=0.75, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                 relheight=dice_point_relheight)
                dice_four.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                relheight=dice_point_relheight)
            elif dice_score == 5:
                dice_one.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_two.place(relx=0.25, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_three.place(relx=0.75, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                 relheight=dice_point_relheight)
                dice_four.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                relheight=dice_point_relheight)
                dice_five.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                relheight=dice_point_relheight)
            elif dice_score == 6:
                dice_one.place(relx=0.25, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_two.place(relx=0.75, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)
                dice_three.place(relx=0.25, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                 relheight=dice_point_relheight)
                dice_four.place(relx=0.75, rely=0.25, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                relheight=dice_point_relheight)
                dice_five.place(relx=0.25, rely=0.5, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                                relheight=dice_point_relheight)
                dice_six.place(relx=0.75, rely=0.75, anchor=ctk.CENTER, relwidth=dice_point_relwidth,
                               relheight=dice_point_relheight)

        # Create Child Frames
        self.dice1_frame = ctk.CTkFrame(master=self.left_down_mid_board_frame, fg_color=DICE_COLOR_1)
        self.dice2_frame = ctk.CTkFrame(master=self.left_down_mid_board_frame, fg_color=DICE_COLOR_1)

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

        self.dice_result_label = ctk.CTkLabel(master=self.left_down_mid_board_frame,
                                              text=dice_result,
                                              font=self.dice_result_font)

        # Layout
        place_dice_points(dice_score=dice1,
                          dice_one=self.dice_point_1, dice_two=self.dice_point_2,
                          dice_three=self.dice_point_3, dice_four=self.dice_point_4,
                          dice_five=self.dice_point_5, dice_six=self.dice_point_6)
        place_dice_points(dice_score=dice2,
                          dice_one=self.dice_point_7, dice_two=self.dice_point_8,
                          dice_three=self.dice_point_9, dice_four=self.dice_point_10,
                          dice_five=self.dice_point_11, dice_six=self.dice_point_12)
        self.dice_result_label.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

        # Child Frame
        self.dice1_frame.place(relx=2 / 6, rely=0.3, anchor=ctk.CENTER, relwidth=0.3, relheight=0.3)
        self.dice2_frame.place(relx=4 / 6, rely=0.3, anchor=ctk.CENTER, relwidth=0.3, relheight=0.3)

    def create_dice_point_label(self, frame):
        return ctk.CTkLabel(master=frame, fg_color=DICE_POINT_COLOR_1,
                            text="", corner_radius=20)

    def confirm_exit(self, event):
        result = messagebox.askquestion("Potwierdzenie", "Czy na pewno chcesz wyjść?")
        if result == "yes":
            self.master.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    app = GameApp(root)
    root.mainloop()
