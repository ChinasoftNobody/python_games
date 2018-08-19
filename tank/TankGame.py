from kivy import logger
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout

from tank import CommonUtil
from tank.widgets import TankWidget


class TankGame(RelativeLayout):
    tank = ObjectProperty(None)
    _keyboard = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check = False
        self.register_keyboard_event()

    def register_keyboard_event(self):
        self._keyboard = Window.request_keyboard(self.keyboard_close, self, 'text')
        self._keyboard.bind(on_key_down=self.on_key_down_handle)
        self._keyboard.bind(on_key_up=self.on_key_up_handle)

    def keyboard_close(self):
        logger.Logger.info('keyboard closed')
        self._keyboard = None

    def on_key_down_handle(self, keyboard, keycode, text, modifiers):
        if CommonUtil.has_attr(self, 'on_key_down'):
            self.on_key_down(keyboard, keycode, text, modifiers)
        if self.children:
            for child in self.children:
                if CommonUtil.has_attr(child, 'on_key_down'):
                    child.on_key_down(keyboard, keycode, text, modifiers)
                    logger.Logger.debug(repr(child.__class__) + 'register event on_key_down')
        return True

    def on_key_up_handle(self, keyboard, keycode):
        if CommonUtil.has_attr(self,'on_key_up'):
            self.on_key_up(keyboard, keycode)
        if self.children:
            for child in self.children:
                if CommonUtil.has_attr(child,'on_key_up'):
                    child.on_key_up(keyboard, keycode)
                    logger.Logger.debug(repr(child.__class__) + 'register event on_key_up')
        return True

    def on_key_up(self, keyboard, keycode):
        if not self.check and keycode[1] == 'enter':
            print('touch me')
            self.clear_widgets()
            tank = Factory.TankWidget()
            self.tank = tank
            self.add_widget(tank)
            self.check = True
