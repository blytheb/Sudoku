from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen, BoxLayout, ToggleButtonBehavior):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    allow_no_selection: False

    def clk_setting(self, instance):
        status = instance.text
        if status == " Let's Play ":
            print("PLAY :", self.manager.grid_size, "AT LEVEL ", self.manager.level)

        print("GAME MODE: ", status)


class GameScreen(Screen, BoxLayout):
    pass


class HowToScreen(Screen):
    pass


class WindowManager(ScreenManager):
    grid_size = NumericProperty(4)
    level = StringProperty('easy')


class SudokuApp(App):

    def build(self):
        m = WindowManager()
        return m


if __name__ == '__main__':
    SudokuApp().run()
