#STEP 1 IMPORT DATASETS
from sklearn.datasets import load_files
from keras.utils import np_utils
import numpy as np
from glob import glob
import cv2                
import matplotlib.pyplot as plt                        
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image                  
from tqdm import tqdm
from PIL import ImageFile    
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.callbacks import ModelCheckpoint 
from keras.applications.resnet50 import preprocess_input, decode_predictions
from extract_bottleneck_features import *
import os
from keras.optimizers import Adam, Adamax


def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)


face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

#STEP 3 DETECT DOGS
# define ResNet50 model
ResNet50_model = ResNet50(weights='imagenet')

dog_names = []

for i in os.listdir("Dog_Names"):
    dog_names.append(i)
    dog_names.sort()
#print len(dog_names)

bottleneck_features = np.load('bottleneck_features/DogResnet50Data.npz')
train_ResNet50 = bottleneck_features['train']
valid_ResNet50 = bottleneck_features['valid']
test_ResNet50 = bottleneck_features['test']


ResNet_model = Sequential()
ResNet_model.add(GlobalAveragePooling2D(input_shape=train_ResNet50.shape[1:]))
ResNet_model.add(Dense(133, activation='softmax'))
ResNet_model.compile(loss='categorical_crossentropy', optimizer=Adamax(lr=0.002), metrics=['accuracy'])

ResNet_model.load_weights('saved_models/weights.best.Resnet50.hdf5')


ResNet50_predictions = [np.argmax(ResNet_model.predict(np.expand_dims(feature, axis=0))) for feature in test_ResNet50]


# report test accuracy
#test_accuracy = 100.0*np.sum(np.array(ResNet50_predictions)==np.argmax(test_targets, axis=1))/len(ResNet50_predictions)
#print('Test accuracy: %.4f%%' % test_accuracy)




def ResNet50_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = np.expand_dims(np.expand_dims(extract_Resnet50(path_to_tensor(img_path)), axis=0), axis=0)
    # obtain predicted vector
    predicted_vector = ResNet_model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    breed = dog_names[np.argmax(predicted_vector)]
    if dog_detector(img_path) == True:
        print("Breed: {}".format(breed))
    else:
        print("If this person was a dog, that person would be a {}".format(breed))


def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151)) 

def face_detector(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0

def predict_breed(img_path):
    isDog = dog_detector(img_path)
    isPerson = face_detector(img_path)
    if isDog:
        print("Detected a dog")
        breed = ResNet50_predict_breed(img_path)
        return breed
    if isPerson:
        print("Detected a human face")
        breed = ResNet50_predict_breed(img_path)
        return breed
    else:
        print("No human face or dog detected")


#predict_breed('husky_104.jpg')
#predict_breed('Affenpinscher_00019.jpg')
#predict_breed('chihuahua_95.jpg')
#predict_breed('Akita_00244.jpg')
#predict_breed('corgi_95.jpg')
#predict_breed('german_shepherd_1.jpg')
'''

for img in os.listdir(direc):
    #f1=cv2.imread('sobra/'+img)
    print("Image name is %s" % img)
    predict_breed('sobra/'+img)'''

#STEP 6 WRITE DOG BREED CLASSIFIER ALGO


#STEP 7 TEST DOG BREED CLASSIFIER ALGO
