from tkinter import Tk

from tank import GAME_TITLE
from tank.TankGame import TankGame


class TankStart(Tk):
    def __init__(self):
        super().__init__()
        self.title('TankCraft')
        self.geometry('800x600')


if __name__ == '__main__':
    tank = Tk()
    tank.title(GAME_TITLE)
    tankGame = TankGame(master=tank)
    tankGame.mainloop()
