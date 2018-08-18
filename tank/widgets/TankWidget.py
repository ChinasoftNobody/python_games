from kivy.clock import Clock
from kivy.factory import Factory
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from tank.widgets import BulletWidget


class TankWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (100, 100)
        self.bullet = None

    def shot(self):
        # parent.add_widget(Factory.BulletWidget())
        bullet = Factory.BulletWidget()
        self.parent.add_widget(bullet)
        self.bullet = bullet

        pass

    def move(self, x, y):
        if self.collide_widget(self.bullet):
            Clock.unschedule(self.parent.clock_event)
            return
        self.pos = Vector(x, y) + self.pos

    def update(self, dt):
        # bounce off top and bottom
        _x = 0
        _y = 0
        if self.y > 0:
            _y = -1

        # bounce off left and right
        if self.x > 0:
            _x = -1
        self.move(_x, _y)
