import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget


# class HelloKivyApp(App):
#
#     def build(self):
#         return Label()
#
# hk = HelloKivyApp()
# hk.run()

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()


customWidget = CustomWidgetApp()
customWidget.run()


