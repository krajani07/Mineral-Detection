#Importing the necessary packages
from numpy.lib.type_check import imag
import tensorflow 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import model_from_json
#image augmentation is performed
batch_size = 5 # no. of images allowed to algorithm
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1/255)
train_generator = train_datagen.flow_from_directory(r'C:\Users\HP\Desktop\mini\2ndtest\assets',  # This is the source directory for training images
        target_size=(200, 200),#images are resized to 200 x 200
        batch_size=batch_size,
        # mention the classes
        classes = ['calcite','diamond','dioptase','magnetite','quartz','ruby','sulfur'],
        # categorical mode because many classes
        class_mode='categorical')

#PHASE -1

#Building the CNN MODEL
model =tensorflow .keras.models.Sequential([
        # The first convolution & maxPooling
        # 32 and (3,3) means 32 feature detectors will be used and each filter will be 3rows- 3cols which will give rise to 32 feature maps 
    tensorflow.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(200, 200, 3)),
    tensorflow.keras.layers.MaxPooling2D(2, 2),
    # The second convolution & maxpooling
    tensorflow.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tensorflow.keras.layers.MaxPooling2D(2,2),
    # The third convolution & maxpooling
    tensorflow.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tensorflow.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution & Maxpooling
    tensorflow.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tensorflow.keras.layers.MaxPooling2D(2,2),
    # The fifth convolution & maxpooling
    tensorflow.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tensorflow.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into ann
    tensorflow.keras.layers.Flatten(),
    # 128 neuron in the fully-connected layer
    tensorflow.keras.layers.Dense(128, activation='relu'),
    # 7 output neurons for 7 classes with the softmax activation
    tensorflow.keras.layers.Dense(7, activation='softmax')
])


#PHASE -2

#Compiling the CNN Model
from tensorflow.keras.optimizers import RMSprop
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['acc'])
total_sample=train_generator.n # total images for training
n_epochs = 6 # 1 epoch means one complete dataset
# fit generator using training set
# define number of iterations per epoch
history = model.fit_generator(
        train_generator, 
        steps_per_epoch=int(total_sample/batch_size),  
        epochs=n_epochs,
        verbose=1)



#PHASE -3

#Test the built model with testing Image data set 

import numpy as np
import cv2
from tensorflow.keras.preprocessing import image

path = r'C:\Users\HP\Desktop\mini\2ndtest\test assets\test_set\diamond\diamond.43.jpg'
test_image = image.load_img(path, target_size = (200, 200))
# target size and input image size should be same
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
print()

print('**************')

if result[0][0] == 1:
    x="calcite"
    print('given mineral is' ,"calcite")

elif result[0][1] == 1:
    x="diamond"
    print('given mineral is' ,"diamond")

elif result[0][2] == 1:
    x="dioptase"
    print('given mineral is' ,"dioptase")

elif result[0][3] == 1:
    x="magnetite"
    print('given mineral is' ,'magnetite')

elif result[0][4] ==1:
    x="quartz"
    print('given mineral is' ,'quartz')

elif result[0][5] ==1:
    x="ruby"
    print('given mineral is' ,'ruby')

elif result[0][6] ==1:
    x="sulfur"
    print('given mineral is' ,'sulfur')

else:
    print("Can't detect a mineral!!!")
print('**************')

image = cv2.imread(path)
window_name = 'image'
cv2.putText(image,x,(500,750),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),5)
cv2.imshow(window_name, image)
cv2.waitKey(0) 
cv2.destroyAllWindows()