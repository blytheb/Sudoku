from kivy.app import App
from kivy.uix.label import Label

class SudokuApp(App):
    def build(self):
        return Label(text="Hello BABY")


SudokuApp().run()
