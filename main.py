import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView

import io
from kivy.core.image import Image as CoreImage


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class AlgoResult(Screen):
    pass
# quiz -------------------------------
class ScreenThree(Screen):
    pass


class Question2(Screen):
    pass

class Question3(Screen):
    pass

class Question4(Screen):
    pass

class Question5(Screen):
    pass

class Question6(Screen):
    pass

class Question7(Screen):
    pass

class Question8(Screen):
    pass

class Question9(Screen):
    pass

class Question10(Screen):
    pass

class ResultScreen(Screen):
    def giveMax():
        

class WYPupper(App):
    # scores
    qscore = {
        'corgi': 0,
        'pug': 0,
        'husky': 0,
        'german_shepherd': 0,
        'chihuahua': 0
    }

    # doggo data
    corgi_data = ('corgi.jpg', 'Corgi', '')
    pug_data = ('pug.jpg', 'Pug', '')
    husky_data = ('husky.jpg', 'Husky', '')
    german_shepherd_data = ('german_shepherd.jpg', 'Corgi', '')
    chihuahua_data = ('chihuahua.jpg', 'Chihuahua', '')
    

    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name = "screen_one")) #home
        screen_manager.add_widget(ScreenTwo(name = "screen_two")) #filechooser
        screen_manager.add_widget(AlgoResult(name = "result")) #algo results screen
        screen_manager.add_widget(ScreenThree(name = "screen_three")) #quizstart
        screen_manager.add_widget(Question2(name = "question_2")) #q2
        screen_manager.add_widget(Question3(name = "question_3")) #q3
        screen_manager.add_widget(Question4(name = "question_4")) #q4
        screen_manager.add_widget(Question5(name = "question_5")) #q5
        screen_manager.add_widget(Question6(name = "question_6")) #q6
        screen_manager.add_widget(Question7(name = "question_7")) #q7
        screen_manager.add_widget(Question8(name = "question_8")) #q8
        screen_manager.add_widget(Question9(name = "question_9")) #q9
        screen_manager.add_widget(Question10(name = "question_10")) #q10
        screen_manager.add_widget(QuizResult(name = "quiz_result")) #q10

        return screen_manager


if __name__ == '__main__':
    app = WYPupper()
    app.run()
