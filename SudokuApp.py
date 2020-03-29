from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainScreenLayout(BoxLayout):
    pass


class SudokuApp(App):
    def build(self):
        return MainScreenLayout()


if __name__ == '__main__':
    SudokuApp().run()
