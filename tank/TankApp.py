# -*-coding:utf-8-*-

from kivy.app import App
from kivy.clock import Clock

from tank.TankGame import TankGame


class TankApp(App):

    def build(self):
        tank_game = TankGame()
        return tank_game


if __name__ == '__main__':
    print('hello world')
    TankApp().run()
