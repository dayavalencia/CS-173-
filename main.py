import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from  kivy.uix.filechooser import FileChooserIconView

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class Question2(Screen):
    pass

class WYPupper(App):

    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name = "screen_one")) #home
        screen_manager.add_widget(ScreenTwo(name = "screen_two")) #filechooser
        screen_manager.add_widget(ScreenThree(name = "screen_three")) #quizstart
        screen_manager.add_widget(Question2(name = "question_2")) #q2

        return screen_manager


if __name__ == '__main__':
    app = WYPupper()
    app.run()