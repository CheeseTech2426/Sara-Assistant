from cmath import exp
from email.mime import application
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
#import random
import pyjokes
#import ctypes
import os

dirWeb = 'C:\\Sara\iBrowse.py'
#title = 'Sara'
#system("Sara " + ver)
#ctypes.windll.kernel32.SetConsoleTitleW(title)
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('Hello')
speak('I am Sara. Your virtual assistant')
speak('How may I help you?')

def take_command():
    try:
        with sr.Microphone() as source:
            speak('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sara' in command:
                command = command.replace('sara', '')
                print(command)
                

    except:
        pass
    return command

def run_sara():
    
    command = take_command()
    print(command)
    if 'hello' in command:
        speak('Hi')
        print('Hi')
    elif 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        speak('The current time is ' + time)
        print(time)
    elif 'date' in command:
        date=datetime.datetime.today().strftime('%Y-%m-%d')
        speak('The date is ' + date)
        print(date)
    elif 'what' in command:
        thingToSearchFromWikipedia = command.replace('what', '')
        info = wikipedia.summary(thingToSearchFromWikipedia, 4)
        speak(info)
        print(info)
    elif 'who' in command:
        thingToSearchFromWikipedia = command.replace('who', '')
        info = wikipedia.summary(thingToSearchFromWikipedia, 4)
        speak(info)
        print(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)
    elif 'quit' in command:
        speak('OK, bye.')
        exit()
    elif 'web' in command:
        speak('OK, opening iBrowse')
        os.startfile(dirWeb)
    else:
        speak('Sorry I did not regonize command ' + command + '.')

while True:
    run_sara()