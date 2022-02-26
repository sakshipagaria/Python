# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:09:25 2022

@author: ADMIN
"""

import speech_recognition as sr
r=sr.Recognizer() #initialize the recognizer

AudioClip=('comethru2.wav')
#use audio as source

with sr.AudioFile(AudioClip) as source:
    audio=r.record(source)
#reads audio file

try:
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition fails to understand the audio.")
except sr.RequestError:
    print("Couldn't get the results")