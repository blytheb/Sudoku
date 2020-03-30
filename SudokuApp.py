from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


class MainScreen(Screen, BoxLayout, ToggleButtonBehavior):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    allow_no_selection: False

    def getInfo(self):
        for w in ToggleButtonBehavior.get_widgets('size'):
            if w.state == 'down':
                size = w.text
        for w in ToggleButtonBehavior.get_widgets('level'):
            if w.state == 'down':
                level = w.text
        return size, level

    def clk_setting(self, instance):
        status = instance.text
        if status == " Let's Play ":
            s, l = self.getInfo()
            print("PLAY :", s, "AT LEVEL ", l)

        print("GAME MODE: ", status)

    def get_size(self, instance):
        select = instance.text
        # print("GRID SIZE: ", select)

    def get_level(self, instance):
        select = instance.text
        # print("LEVEL:", select)


class GameScreen(Screen):
    pass

class HowToScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class SudokuApp(App):
    def build(self):
        m = WindowManager()
        return m


if __name__ == '__main__':
    SudokuApp().run()
