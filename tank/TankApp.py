# -*-coding:utf-8-*-

from kivy.app import App
from tank.TankGame import TankGame


class TankApp(App):

    def build(self):
        return TankGame()


if __name__ == '__main__':
    print('hello world')
    TankApp().run()
