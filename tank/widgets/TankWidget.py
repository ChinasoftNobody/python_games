from kivy.factory import Factory
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from tank.widgets import BulletWidget


class TankWidget(Widget):
    pos_x = NumericProperty(100)
    pos_y = NumericProperty(100)
    velocity = ReferenceListProperty(pos_x, pos_y)

    def shot(self):
        # parent.add_widget(Factory.BulletWidget())
        bullet = Factory.BulletWidget()
        self.parent.add_widget(bullet)

        pass

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def update(self, dt):
        self.move()

        # bounce off top and bottom
        if (self.y > 0):
            self.pos_y -= 1

        # bounce off left and right
        if (self.x > 0):
            self.pos_x -= 1