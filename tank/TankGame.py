from tkinter import *

from tank import *


class TankGame(Frame):
    def __init__(self, master):
        super().__init__(master, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.pack(side=LEFT, padx=10)
        self.init_menu()

    def init_menu(self):
        """
        初始化菜单栏
        :return: None
        """
        menu_titles = {'start', 'pause', 'continue', 'next'}
        for menu_title in menu_titles:
            menu_button = Button(self, text=menu_title, width=10, height=5)
            menu_button.pack(side=LEFT,expand=NO,anchor=W, fill=BOTH)