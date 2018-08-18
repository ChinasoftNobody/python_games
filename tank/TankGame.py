from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from tank.widgets import TankWidget


class TankGame(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = False

    def on_touch_down(self, touch):
        if not self.check:
            print('touch me')
            self.clear_widgets()
            tank = Factory.TankWidget()
            self.add_widget(tank)
            tank.shot()
            self.check = True

        return True
