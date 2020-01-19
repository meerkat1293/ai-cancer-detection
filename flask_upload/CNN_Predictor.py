import keras
import tensorflow
import tensorflow_estimator
import tensorboard
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator

# load json and create model
json_file = open('/home/mmeer/flask_upload/model.json', 'r') # replace with local directory
loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/home/mmeer/flask_upload/model.h5") # replace with local directory

from keras.preprocessing.image import ImageDataGenerator
test_datagen = ImageDataGenerator(rescale = 1./255)
user_data = test_datagen.flow_from_directory('/home/mmeer/flask_upload/User-Data/test', # replace with local directory
                                            target_size = (64, 64),
                                            batch_size = 1,
                                            class_mode = 'binary')

# evaluate loaded model on user data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(user_data)
if score[1] == 0:
  diagnosis =  'The convolutional neural network predicts that this tumor is malignant!'
else:
  diagnosis = 'The convolutional neural network predicts that this tumor is benign.'

