import calendar
import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
from googletrans import Translator
import keyboard
from PyDictionary import PyDictionary as pydict
import subprocess
import pyautogui
import requests


def weatherReport():
    api_key = "766e077d2f5b5caa4befcd3a860a55c6"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak('Tell me you Current Location ?')
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('waiting...')
        ad = r.listen(source)
        city = r.recognize_google(ad)
        print(city)
        # city='mumbai'
        url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url).json()

        print('temperature is' + str(response['main']['temp']))
        speak('temperature is' + str(response['main']['temp']))
        print('wind speed is' + str(response['wind']['speed']))
        speak('wind speed is' + str(response['wind']['speed']))
        print('and feels like ' + response['weather'][0]['main'])
        speak('and feels like ' + response['weather'][0]['main'])
def information():
    speak('sure...')
    person = text2.replace('information', '')
    info = wikipedia.summary(person, 1)
    print(info)
    speak('according to wikipedia' + info)
def dictionary():
    speak('dictionary is open')
    speak('Please tell me what you want now')
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listenning......')
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)
    if 'meaning' in text2:
        text2=text2.replace('meaning',"")
        text2=text2.replace('of',"")
        result=pydict.meaning(text2)
        speak(f'The meaning of {result}')

    elif 'synonym' in text2:
        text2=text2.replace('synonym',"")
        result=pydict.synonym(text2)
        speak(f'The meaning of {result}')

    elif 'antonym' in text2:
        text2=text2.replace('antonym',"")
        result=pydict.antonym(text2)
        speak(f'The meaning of {result}')
def screenshot():
    speak('okay,what name do you want give?')
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listenning......')
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)
    pathname=text2 +'.png'
    path='D:\\screenshot' + pathname
    ss=pyautogui.screenshot()
    ss.save(path)
    os.startfile('D:\\screenshot')
    speak('here is your screenshot')
def closeapp():
    speak('okay, wait a second..')

    if 'chrome' in text2:
        os.system("TASKILL /F /im chrome.exe")
    elif 'youtube' in text2:
        os.system("TASKILL /F /im chrome.exe")
    speak('done')

def TakeHindi():
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('listenning..')
            audio = r.listen(source)
            text2 = r.recognize_google(audio,language='hi')
            print('you said :' + text2)
    except Exception as Error:
        return 'none'
    return text2.lower()

def STranslator():
    speak('speak out the line which you want to translate')
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listenning......')
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)
    line=TakeHindi()
    traslator=Translator()
    result=traslator.translate(line)
    Txt=result.text
    speak('The translation for this line is :'+Txt)



r = sr.Recognizer()
try:
    engine = p.init() #information  the current driver

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(text):
        engine.say(text)
        engine.runAndWait()


     #it help us to retrieve audio from microphone

    speak("Hello . I'm your voice assistant. HOw are you?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listenning')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
    if "what" and "about" and "you" in text:
        speak("I am having a good day")
    speak("what  can i do for you?")
except:
    speak('can you speak again ?')
    pass


while True:
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('listenning......')
            audio = r.listen(source)
            text2 = r.recognize_google(audio)
            print(text2)

        if 'weather' in text2:
            weatherReport()


        if 'play' in text2:
            song = text2.replace('play','')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            if 'pause' in text2:
                keyboard.press('spacebar')
            elif 'full screen' in text2:
                keyboard.press('f')
            elif 'mute' in text2:
                keyboard.press('m')
            elif 'back' in text2:
                keyboard.press('j')
            elif 'start' in text2:
                keyboard.press('0')
            elif 'skip' in text2:
                keyboard.press('l')

        elif 'date' in text2:
            curr_date = datetime.date.today()
            speak('Today date is '+ str(curr_date))
            speak(' and Today is' + calendar.day_name[curr_date.weekday()])

        elif 'spotify' in text2:
            speak('Opening Spotify.....')
            program = r'C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe'
            subprocess.Popen([program])

        elif 'Notepad' in text2:
            speak('Okay....')
            os.system('Notepad')

        elif 'time' in text2:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'joke' in text2:
            speak('Sure,get ready for some chuckles')
            speak(pyjokes.get_joke())

        elif 'chrome' in text2:
            speak('Opening Chrome.....')
            program = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
            subprocess.Popen([program])



        elif 'who'in text2:
            information()

        elif 'what'in text2:
            information()

        elif 'how' in text2:
            information()


        elif 'search' in text2:
            speak('searching, have patience')
            text2=text2.replace("search","")
            content=pywhatkit.search(text2)
            speak('done')

        elif 'website' in text2:
            speak('okayji')
            text2=text2.replace("website","")
            web1=text2.replace("open","")
            web2='https://www.' +web1+'.com'
            webbrowser.open(web2)
            speak('done')

        elif 'screenshot' in text2:
            screenshot()

        elif 'dictionary' in text2:
            dictionary()

        elif "close" in text2:
            closeapp()

        elif "translate" in text2:
            STranslator()



        elif 'bye' in text2:
            speak('Thankyou!!')
            break




        else:
            speak('Please say the command again.')
    except:
        pass



