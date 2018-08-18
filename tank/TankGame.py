from kivy.clock import Clock
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout

from tank.widgets import TankWidget


class TankGame(RelativeLayout):
    tank = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = False

    def on_touch_down(self, touch):
        if not self.check:
            print('touch me')
            self.clear_widgets()
            tank = Factory.TankWidget()
            self.tank = tank
            Clock.schedule_interval(self.tank.update, 1.0 / 60.0)
            self.add_widget(tank)
            tank.shot()
            self.check = True

        return True

