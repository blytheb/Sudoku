from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import Clock
from kivy.uix.widget import Widget


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
#     def __init__(self, **kwargs):
#       super(GameScreen, self).__init__(**kwargs)

    def drawGrid(self):
        for i in range(self.manager.grid_size * self.manager.grid_size):
            if self.manager.grid_size == 9:
                self.ids.board.add_widget(TextInput(text="", multiline=False, cursor_blink=False, size_hint_x=None, size_hint_y=None, height=45, width=45))
            if self.manager.grid_size == 4:
                self.ids.board.add_widget(TextInput(text="", multiline=False, cursor_blink=False, size_hint_x=None, size_hint_y=None, height=65, width=65))



class HowToScreen(Screen):
    pass


class WindowManager(ScreenManager):
    grid_size = NumericProperty(4)
    level = StringProperty('easy')




class SudokuApp(App):

    def build(self):
        m = WindowManager()
#        m.add_widget(Screen(name='main'))
 #       m.add_widget(Screen(name='game'))
        return m


if __name__ == '__main__':
    SudokuApp().run()
