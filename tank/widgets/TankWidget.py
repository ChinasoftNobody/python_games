from kivy.factory import Factory
from kivy.uix.widget import Widget

from tank.widgets import BulletWidget


class TankWidget(Widget):

    def shot(self):
        # parent.add_widget(Factory.BulletWidget())
        bullet = Factory.BulletWidget()
        self.parent.add_widget(bullet)

        pass
