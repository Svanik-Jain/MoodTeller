import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Listening...")                                                                                   
    audio = r.listen(source)   
try:
    saidText = r.recognize_google(audio)
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")

blob = TextBlob(saidText)
for sentence in blob.sentences:
    if(sentence.sentiment.polarity == 0.0):
        print("You are in a neutral mood.")
    elif(sentence.sentiment.polarity >= 0.05):
        print("You are in a good mood. I hope you have a nice day.")
    elif(sentence.sentiment.polarity <= 0.05):
        print("You are in a bad mood. I hope your problems are solved.")
    else:
        print("Unable to guess")
