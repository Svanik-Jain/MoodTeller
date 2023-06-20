import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr

sia = SentimentIntensityAnalyzer()

r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Listening...")                                                                                   
    audio = r.listen(source)   
saidText = r.recognize_google(audio)
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
   
scoreV = sia.polarity_scores(saidText)
ScoreC = scoreV['compound']

if(ScoreC == 0):
    print("You are in a neutral mood.")
elif(ScoreC >= 0.5):
    print("You are in a good mood. I hope you have a nice day.")
elif(ScoreC < 0.5):
    print("You are in a bad mood. I hope your problems are solved.")
