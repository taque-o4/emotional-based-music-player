import mysql.connector
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
import tkinter.font as font
from tkinter import filedialog
import re

face_classifier = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
classifier =load_model(r'model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root!@#123",
                database="users_database"
            )

            # Execute a SELECT query to check if the user exists
            cursor = conn.cursor()
            query = "SELECT title, file_path FROM music_files WHERE category = %s"
            values = (label,)
            cursor.execute(query, values)
            tracks = cursor.fetchall()
            
            for track in tracks:
                def player():
                    # Initialize Pygame Mixer
                    pygame.mixer.init()
                    # Create a tkinter window
                    root = ctk.CTk()

                    # Create a Treeview widget
                    treeview = ttk.Treeview(root)

                    # Define our columns
                    treeview['columns'] = ('Title', 'Path')

                    # Loop thru the records and add them in the Treeview
                    treeview.insert('', 'end', values=track)

                    # Function to play song
                    def play_song(event):
                        # Get selected item on treeview
                        selected_item = treeview.selection()[0]
                        song = treeview.item(selected_item)['values'][1]

                        # Load and play song
                        pygame.mixer.music.load(song)
                        pygame.mixer.music.play()

                    # Bind select event to treeview
                    treeview.bind('<<TreeviewSelect>>', play_song)


                    # Pack the Treeview widget into the window
                    treeview.pack()
                    root.mainloop()
                player()
        else:
            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()