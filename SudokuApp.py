from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MainScreenLayout(BoxLayout):
    status = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainScreenLayout, self).__init__(**kwargs)

    def clk_setting(self, instance):
        print(instance.text)


class SudokuApp(App):
    def build(self):
        return MainScreenLayout()


if __name__ == '__main__':
    SudokuApp().run()
