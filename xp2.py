'''Importing Necessary modules'''

#modules for ocr, web app and image processing

import easyocr 
import streamlit as st  
from PIL import Image 
import numpy as np  
import cv2
import time

# Heading and subheading

code = '''def Image_To_Text():
            print("Hello, User!")'''
st.code(code, language='python')

st.markdown('This is a Web page for Extraction of Text from an Image using **easyocr, opencv**')

img_file = st.file_uploader(label = "Upload the Image for text extraction",type=['png','jpg','jpeg'])  

@st.cache
def object_setup(): 
    reader = easyocr.Reader(['en', 'hi'],model_storage_directory='.')
    return reader 

def preprocessing(pic):
    img = cv2.resize(pic, None, fx=2, fy=2)#resizing the image for better string conversion
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#cvtColor method for channel conversion
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    img = cv2.GaussianBlur(img, (5, 5), 0)

    return img

with st.spinner("Please Wait, as I am not a Optimized Programmer 😅! "):
    reader = object_setup()

if img_file is not None:

    input_image = Image.open(img_file)
    st.image(input_image)

    my_bar = st.progress(0)

    for percent_complete in range(1):

        pic = np.array(input_image)
        pic = preprocessing(pic)
        result = reader.readtext(pic, decoder = 'beamsearch')# Return list of results
        result_text = []

        for text in result:
            result_text.append(text[1])

        st.write(result_text)

        my_bar.progress(percent_complete + 100)

    st.snow()
else:
    with st.spinner('👾👾👾👾👾👾👾👾'):
        time.sleep(5)
        st.write("👽👽👽👽")

st.caption("Created by @Anish521🐱")
