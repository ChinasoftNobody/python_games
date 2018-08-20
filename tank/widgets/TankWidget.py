from functools import partial

from kivy.clock import Clock
from kivy.factory import Factory
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from tank.widgets import BulletWidget


class TankWidget(Widget):
    moving = False
    shooting = False
    shoot_clock_event = None
    move_clock_event = None
    move_speed = .01
    bullet_speed = .001
    directionDict = ('left', 'right', 'up', 'down')
    direction = directionDict[2]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def shoot(self):
        bullet = Factory.BulletWidget(self)
        self.parent.add_widget(bullet)
        pass

    def move(self, x, y):
        for child in self.parent.children:
            if self is not child and self.collide_widget(child):
                return
        self.pos = Vector(x, y) + self.pos

    def on_key_down(self, keyboard, keycode, *args):
        print(keycode)
        move_keys = ['left', 'right', 'up', 'down']
        if keycode[1] in move_keys:
            if not self.moving:
                self.moving = True
                x, y = 0, 0
                if keycode[1] == move_keys[0]:
                    x = -1
                    self.direction = self.directionDict[0]
                elif keycode[1] == move_keys[1]:
                    x = 1
                    self.direction = self.directionDict[1]
                elif keycode[1] == move_keys[2]:
                    y = 1
                    self.direction = self.directionDict[2]
                elif keycode[1] == move_keys[3]:
                    y = -1
                    self.direction = self.directionDict[3]
                else:
                    pass
                self.move_clock_event = Clock.schedule_interval(partial(self.move_update, x, y), self.move_speed)
            return True
        elif keycode[1] == 'lctrl':
            if not self.shooting:
                self.shooting = True
                self.shoot()
            return True



    def on_key_up(self, keyboard, keycode):
        move_keys = ['left', 'right', 'up', 'down']
        if keycode[1] in move_keys:
            Clock.unschedule(self.move_clock_event)
            self.move_clock_event = None
            self.moving = False
            return True
        elif keycode[1] == 'lctrl':
            self.shooting = False

    def move_update(self, value, key, dt):
        self.move(value, key)
        pass
