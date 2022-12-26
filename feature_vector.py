import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import tensorflow as tf
from keras.models import Model 
from keras.utils import img_to_array
import pickle

def get_model():
    mobile = tf.keras.applications.mobilenet.MobileNet(weights='imagenet')
    model = Model(inputs=mobile.inputs, outputs=mobile.get_layer('reshape_2').output)
    return model

def preprocessing(img):
    img = img.resize((224,224))
    img = img.convert('RGB')
    img = img_to_array(img)
    img = np.expand_dims(img,0)
    img = tf.keras.applications.mobilenet.preprocess_input(img)
    return img

def get_feature_vector(model, path):
    img = Image.open(path)
    ts = preprocessing(img)
    vector = model.predict(ts)[0]
    vector = vector/np.linalg.norm(vector)
    return vector

base_dir = '.'
vector_file = 'Database/feature.pkl'
path_file = 'Database/path.pkl'
db_dir = os.path.join(base_dir, 'images')
def train():
    vectors = []
    paths = []
    model = get_model()
    for i in os.listdir(db_dir):
        img_path = os.path.join(db_dir, i)
        vectors.append(get_feature_vector(model, img_path))
        paths.append(img_path)
    
    pickle.dump(vectors, open(vector_file, 'wb'))
    pickle.dump(paths, open(path_file, 'wb'))
