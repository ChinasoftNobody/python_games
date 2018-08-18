from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class BulletWidget(Widget):
    pos_x = NumericProperty(0)
    pos_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.pos_x = 100
        # self.pos_y = 100
