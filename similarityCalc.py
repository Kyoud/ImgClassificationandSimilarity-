import numpy as np
import tensorflow as tf
from scipy.spatial.distance import cityblock
from tensorflow import keras
from keras.models import Model
import requests
import PIL
from PIL import Image
from io import BytesIO
import pathlib
import os


def createOrLoadDatabase(model):  # creating a database of vectors to compare against
    database = []  # array including vector and path
    if not os.path.isfile('similarityDatabase.npy'):  # only create database if does not already exist
        data_dir = pathlib.Path("carBrands")
        pathOfImages = list(data_dir.glob('*/*.jpg'))  # all image paths from dataset
        for path in pathOfImages:
            img = PIL.Image.open(path)
            img = img.resize((180, 180))
            img = keras.preprocessing.image.img_to_array(img)
            imgArrayBadge = tf.expand_dims(img, 0)
            database.append([model.predict(imgArrayBadge), path])
        np.save("similarityDatabase", database, allow_pickle=True)  # saving database to disc
    else:
        database = np.load("similarityDatabase.npy", allow_pickle=True)  # loading database when already on disc
    return database


model = keras.models.load_model('carClassifierModel/')  # loading model from disc
model.summary()
layer_name = 'dense'  # chose last layer

featureVectorModel = Model(inputs=model.input, outputs=model.get_layer(layer_name).output)  # cut of the last layer
featureVectorModel.summary()

database = createOrLoadDatabase(featureVectorModel)  # loading or creating the database with the new model

response = requests.get("https://source.unsplash.com/random/?car ,audi")  # get sample image
if response.status_code == 200:  # when image is loadable show it and format for model
    img = PIL.Image.open(BytesIO(response.content))
    img.show()
    img = img.resize((180, 180))
    img = keras.preprocessing.image.img_to_array(img)
    imgArrayBadge = tf.expand_dims(img, 0)  # Create a batch
else:
    raise Exception("Problem with request, Status code: " + str(response.status_code))

intermediate_output = featureVectorModel.predict(imgArrayBadge)
smallest = []  # store the image with the smallest Manhattan distance
for vector, path in database:
    if not smallest:
        smallest = [cityblock(intermediate_output, vector), path]  # fist image
    else:
        distance = cityblock(intermediate_output, vector)  # calculate Manhattan distance
        if smallest[0] > distance:
            smallest = [distance, path]

print("The closest image is: ")
img = PIL.Image.open(smallest[1])
img.show()  # show image with the most similarity
