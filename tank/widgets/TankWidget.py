from functools import partial

from kivy.clock import Clock
from kivy.factory import Factory
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from tank.widgets import BulletWidget


class TankWidget(Widget):
    moving = False
    move_clock_event = None
    speed = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bullet = None

    def shot(self):
        bullet = Factory.BulletWidget()
        self.parent.add_widget(bullet)
        self.bullet = bullet
        pass

    def move(self, x, y):
        for child in self.parent.children:
            if self is not child and self.collide_widget(child):
                return
        self.pos = Vector(x, y) + self.pos

    def on_key_down(self, keyboard, keycode, *args):
        move_keys = ['left', 'right', 'up', 'down']
        if keycode[1] not in move_keys:
            return
        if not self.moving:
            self.moving = True
            x, y = 0, 0
            if keycode[1] == move_keys[0]:
                x = -1
            elif keycode[1] == move_keys[1]:
                x = 1
            elif keycode[1] == move_keys[2]:
                y = 1
            elif keycode[1] == move_keys[3]:
                y = -1
            else:
                pass
            self.move_clock_event = Clock.schedule_interval(partial(self.move_update, x, y), self.speed)

    def on_key_up(self, keyboard, keycode):
        move_keys = ['left', 'right', 'up', 'down']
        if keycode[1] in move_keys:
            Clock.unschedule(self.move_clock_event)
            self.move_clock_event = None
            self.moving = False

    def move_update(self, value, key, dt):
        self.move(value, key)
        pass
