import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


# class HelloKivyApp(App):
#
#     def build(self):
#         return Label()
#
# hk = HelloKivyApp()
# hk.run()

# class CustomWidget(Widget):
#     pass

class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class TutorialApp(App):

    def build(self):
        return CalcGridLayout()

tutApp = TutorialApp()
tutApp.run()


