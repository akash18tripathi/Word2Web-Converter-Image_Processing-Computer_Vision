import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt
from itertools import islice
from keras.callbacks import ModelCheckpoint
from keras.layers import Dense, Flatten, Conv2D
from keras.layers import MaxPooling2D, Dropout
from keras.models import Sequential
from keras.utils import print_summary, np_utils
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.models import load_model




#Data loading part
HEAD = 'head'
NAV = 'nav'
MAIN = 'main'
X = []
y = []
features = []

for filename in os.listdir(os.path.join(HEAD)):
   if filename.endswith('.jpg'):
       full_path = os.path.join(HEAD, filename)
       X.append(full_path)
       y.append(0)

for filename in os.listdir(os.path.join(NAV)):
    if filename.endswith('.jpg'):
        full_path = os.path.join(NAV, filename)
        X.append(full_path)
        y.append(1)

for filename in os.listdir(os.path.join(MAIN)):
   if filename.endswith('.jpg'):
       full_path = os.path.join(MAIN, filename)
       X.append(full_path)
       y.append(2)

for i in range(len(X)):
    img = plt.imread(X[i])
    resized_img = cv.resize(img, (100,100))
    features.append(resized_img)

features = np.array(features).astype('float32')
labels = np.array(y).astype('float32')


features, labels = shuffle(features, labels)
features = features / 255.
train_x, test_x, train_y, test_y = train_test_split(features, labels, random_state=0,test_size=0.1)
train_x = train_x.reshape(train_x.shape[0], 100, 100, 1)
test_x = test_x.reshape(test_x.shape[0], 100, 100, 1)

train_y = np_utils.to_categorical(train_y)
test_y = np_utils.to_categorical(test_y)

#CNN model
model = Sequential()
model.add(Conv2D(32, (5, 5), input_shape=(100, 100, 1), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
model.add(Conv2D(64, (5, 5), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(5, 5), padding='same'))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.6))
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.6))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_x, train_y, validation_data=(test_x, test_y), epochs=10, batch_size=32)



scores = model.evaluate(test_x, test_y, verbose=0)
print("CNN Error: %.2f%%" % (100 - scores[1] * 100))

model.save('model.h5')