import kivy
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
import image
import io
from kivy.core.image import Image as CoreImage

imgArg = ""

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class AlgoResult(Screen):
    try:
        global imgArg
    except:
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
    # def getMax(self):
    #     c = max(app.qscore, key=app.qscore.get)

    #     if c == "corgi":
    #         app.img_src = "corgi.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "corgi.jpg")
    #         app.breed_name = "Corgi"
    #     elif c == "pug":
    #         app.img_src = "pug.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pug.jpg")
    #         app.breed_name = "Pug"
    #     elif c == "husky":
    #         app.img_src = "husky.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "husky.jpg")
    #         app.breed_name = "Husky"
    #     elif c == "german_shepherd":
    #         app.img_src = "german_shepherd.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "german_shepherd.jpg")
    #         app.breed_name = "German Shepherd"
    #     elif c == "chihuahua":
    #         app.img_src = "chihuahua.jpg"
    #         #app.img_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chihuahua.jpg")
    #         app.breed_name = "Chihuahua"


class Corgi_Result(Screen):
    pass

class Pug_Result(Screen):
    pass

class Husky_Result(Screen):
    pass

class GS_Result(Screen):
    pass

class Chihuahua_Result(Screen):
    pass


class WYPupper(App):
    # scores
    qscore = {
        'corgi': 0,
        'pug': 0,
        'husky': 0,
        'german_shepherd': 0,
        'chihuahua': 0
    }

    # for quiz result
    breed_name = ''
    # global imgArg
    # imgArg=''
    # imgArg1 = imgArg
    # print(imgArg1)
    imgArg1 = ""
    def select_to(self,*args):
        try:
            global imgArg
            imgArg1 = args[1][0]
            imgArg = imgArg1
        except:
            pass

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

        # result pages
        screen_manager.add_widget(Corgi_Result(name = "corgi"))
        screen_manager.add_widget(Pug_Result(name = "pug"))
        screen_manager.add_widget(Husky_Result(name = "husky"))
        screen_manager.add_widget(GS_Result(name = "gs"))
        screen_manager.add_widget(Chihuahua_Result(name = "chihuahua"))

        return screen_manager


if __name__ == '__main__':
    app = WYPupper()
    app.run()
