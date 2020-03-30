from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


class MainScreen(Screen, BoxLayout, ToggleButtonBehavior):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    allow_no_selection: False

    def getInfo(self):
        for w in ToggleButtonBehavior.get_widgets('size'):
            if w.state == 'down':
                self.manager.grid = w.text
        for w in ToggleButtonBehavior.get_widgets('level'):
            if w.state == 'down':
                self.manager.level = w.text

    def clk_setting(self, instance):
        status = instance.text
        if status == " Let's Play ":
            self.getInfo()
            print("PLAY :", self.manager.grid, "AT LEVEL ", self.manager.level)

        print("GAME MODE: ", status)

    def get_grid(self, instance):
        self.manager.grid = instance.text
        # print("GRID SIZE: ", select)

    def get_level(self, instance):
        self.manager.level = instance.text
        # print("LEVEL:", select)


class GameScreen(Screen, BoxLayout):
    pass


class HowToScreen(Screen):
    pass


class WindowManager(ScreenManager):
    grid = StringProperty(' 4 x 4 ')
    level = StringProperty(' EASY ')


class SudokuApp(App):

    def build(self):
        m = WindowManager()
        return m


if __name__ == '__main__':
    SudokuApp().run()
