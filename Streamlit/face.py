import cv2
import face_recognition
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('TkAgg',force=True)
import streamlit as st
import os

#Encode Faces
def encode_faces(path = "images/") -> dict:
    faces ={}
    for image in os.listdir(path):
        try:
            face = face_recognition.load_image_file(path+image) 
            encoding = face_recognition.face_encodings(face)[0]
            faces[image.split(".")[0]] = encoding
        except:
        
            pass
    return faces

#compare faces
def compare_faces(image):
    faces = encode_faces()
    face = face_recognition.load_image_file(image)
    try:
        encoding = face_recognition.face_encodings(face)[0] 
        results = face_recognition.compare_faces(list(faces.values()),encoding)
        return list(faces.keys())[results.index(True)]
    except:
        return "No Face Detected"
    



#Streamlit
st.title("Face Recognition")
st.header(":Hero Face Recognition:")
st.write("Upload an image and the app will tell you the name of the hero in the image")
#Upload Image
uploaded_file = st.file_uploader("Choose an image...")
if st.button("Click me..."):
    if uploaded_file is not None:
        image = uploaded_file.read()
        with open("images/guess/image.jpg","wb") as f:
            f.write(image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        st.write("Name: ",compare_faces("images/guess/image.jpg"))
    else:
        st.write("Please upload DUMB HEAD........")


    