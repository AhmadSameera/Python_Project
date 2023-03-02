import pyttsx3 as p
import speech_recognition as sr
import datetime


def speak(text):
    engine = p.init("sapi5")  # information  the current driver

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    print(" ")
    print(f"Voice Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
    print("  ")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)

        print('listenning')
        audio = r.listen(source,0,4)
        try:
            print("Recogninzing..")
            query = r.recognize_google(audio)
            print(f"You said:{query}")
        except:
            # return ""
            pass

        query=str(query)
        return  query.lower()