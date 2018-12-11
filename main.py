import kivy
import os
#: import main dog
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
#import image
#from PIL import *
import io
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty

import time

#from dog import *
imgSrc='german_shepherd.jpg'
imgArg1="pug.jpg"
imgArg='corgi.jpg'
class ScreenOne(Screen):
    pass

class SelectPhoto(Screen):
    pass

class Cam (Screen):
    def capture(self):
        # '''
        # Function to capture the images and give them the names
        # according to their captured time and date.
        # '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filename = "IMG_{}.png".format(timestr)
        camera.export_to_png("IMG_{}.png".format(timestr))
            #to get the image from the camera, pwedeng just select the image name agad. make filename global. Sa desktop it puts the images where your code is saved.

class ConfirmPhoto(Screen):
    pass

class ScreenTwo(Screen):

    imgSrc='headshot.jpg'

    def select_to(self,*args):

        try:
            imgArg=args[1][0]
            imgSrc=imgArg
            print (imgSrc)
            return imgSrc
            #iw= Image.open(args[1][0])
            #self.img.source= args[1][0]
            #self.img.source.reload()
        except:
            pass
    def set_path(self,*imgpath):
        global imgArg
        imgArg=imgpath
        #return imgArg

    #imgSrc=imgArg
class AlgoResult(Screen):
   #predict_breed(imgArg1)


    #obj2=ScreenTwo()
    #imgArg=obj2.imgSrc
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

    #obj1=ScreenTwo()
    #imgArg=obj1.select_to(imgArg)
    #print imgArg

  #  obj1=ScreenTwo()

   # imgArg=obj1.imgSrc
    #imgArg=imgArg1


    ar1 = StringProperty("")


    # imgArg1 = imgArg
    # print(imgArg1)
    #imgArg1 = "/home/invillanueva/Desktop/CS173/Pics/s4/husky_13.jpg"



    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name = "screen_one")) #home

        screen_manager.add_widget(SelectPhoto(name = "select_photo")) #Select Photo
        screen_manager.add_widget(Cam(name = "cam")) #Camera
        screen_manager.add_widget(ConfirmPhoto(name = "confirm_photo")) #Camera
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
