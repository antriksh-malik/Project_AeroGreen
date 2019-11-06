import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import PySimpleGUI as sg

classifier.load("args.h5")

layout = [[sg.Text('Welcome to Project AeroGreen', justification='center', font='Helvetica 15')],
          [sg.Text("Please enter the street/area to be depolyed")],
          [sg.InputText(key='in1')],
          [sg.ReadButton('Begin Deployment')],
          [sg.Text("",key="streetname",size=(15,1)), sg.Text("is"),sg.Text("",key="predict",size(8,1))]]

street=' '

window = sg.Window('AeroGreen').Layout(layout)

# event loop
while True:
    button, values = window.Read()
    street=(values["in1"])
    if button is None:
        break
    elif button=="Begin Deployment":
        window.FindElement("streetname").Update(street)
        from keras.preprocessing import image
        test_image = image.load_img('C:/Users/user/Downloads/plastic_unsplash.jpg', target_size = (64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image,axis = 0)
        result = classifier.predict(test_image)
        training_set.class_indices
        prediction=""
        if result[0][0] >=0.5:
            prediction="unclean"
        else:
            prediction="clean"
        window.FindElement("predict").Update(prediction)
