from functools import partial

from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class BulletWidget(Widget):

    def __init__(self, tank, **kwargs):
        super().__init__(**kwargs)
        self.pos = tank.pos
        self.direction = tank.direction
        self.directionDict = tank.directionDict
        self.shoot_clock_event = Clock.schedule_interval(partial(self.move), tank.bullet_speed)

    def move(self, dt):
        x, y = 0, 0
        if self.direction == self.directionDict[0]:
            x = -1
        elif self.direction == self.directionDict[1]:
            x = 1
        elif self.direction == self.directionDict[2]:
            y = 1
        else:
            y = -1
        _pos = Vector(x, y) + self.pos
        if _pos[0] < 0 or _pos[0] > self.parent.size[0] or _pos[1] < 0 or _pos[1] > self.parent.size[1]:
            Clock.unschedule(self.shoot_clock_event)
            self.parent.remove_widget(self)
            del self
        else:
            self.pos = _pos
