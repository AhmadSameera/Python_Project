import calendar
import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import time
import datetime
import winsound
import wikipedia
from ecapture import ecapture as ec
import pyjokes
import webbrowser
import os
import subprocess
import pyautogui
import requests
from Speak import speak,listen
from objectmain1 import *


try:

    def time():
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)

    def date():
        curr_date = datetime.date.today()
        speak('Today date is ' + str(curr_date))
        speak(' and Today is' + calendar.day_name[curr_date.weekday()])

    def screenshot():
        speak('okay,what name do you want give?')

        pathname=listen()+'.png'
        path='D:\\screenshot\\' + pathname
        ss=pyautogui.screenshot()
        ss.save(path)
        os.startfile('D:\\screenshot\\')
        speak('here is your screenshot')


    def note():
        speak("What should i write?")
        note = listen()
        file = open('jarvis.txt', 'w')
        speak(" Should i include date and time")
        snfm = listen()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            file.write(strTime)
            file.write(" :- ")
            file.write(note,os.path.join( "image","text.txt"))
        else:
            file.write(note,os.path.join( "image","text.txt"))


    def alarm(Timing):
        altime=str(datetime.datetime.now().strptime(Timing,"%I:%M:%p"))
        altime=altime[11:-3]
        Horeal=altime[:2]
        Horeal=int(Horeal)
        Mireal=altime[3:5]
        Mireal=int(Mireal)
        print(f"Done, alarm is set for {Timing}")

        while True:
            if Horeal==datetime.datetime.now().hour:
                if Mireal==datetime.datetime.now().minute:
                    print("alarm is running")
                    winsound.PlaySound('abc',winsound.SND_LOOP)

                elif Mireal<datetime.datetime.now().minute:
                    break




    def function(query):
        query=str(query)
        if "time" in query:
            time()
        if "date" in query:
            date()
        if "screenshot" in query:
            screenshot()
        if "jokes" in query:
            speak('Sure,get ready for some chuckles')
            speak(pyjokes.get_joke())
        if "notepad" in query:
            speak('Okay....')
            os.system('Notepad')
        if 'spotify' in query:
            speak('Opening Spotify.....')
            program = r'C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe'
            subprocess.Popen([program])
        if 'note' in query:
            note()



    def functionInput(tag,query):

        if "information" in tag:
            person = str(query).replace('what is', '').replace('who is', '').replace(
                'get information', '').replace('find', '')
            info = wikipedia.summary(person,sentence=3)
            speak('According to wikipedia' + info)

        if "google" in tag:
            query=str(query).replace('search', '')
            query=str(query).replace('about', '').replace('google','')
            pywhatkit.search(query)
            if "close Google" is tag:
                os.startfile("TASKKILL /F /im chrome.exe ")

        if "weatherReports" in tag:
                api_key = "766e077d2f5b5caa4befcd3a860a55c6"  # Enter the API key you got from the OpenWeatherMap website
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                speak('Tell me you Current Location ?')
                r = sr.Recognizer()
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

        if "play"in tag:
            song = str(query).replace('play song', '')
            song = str(query).replace('play something', '')
            song = str(query).replace('i want to listen ', '')
            pywhatkit.playonyt(song)
            speak('playing ' + song)

        if "website" in tag:
            speak("okay")
            command=query.replace("Amica","")
            command=query.replace("website","")
            web1=query.replace("open","")
            web2='https://www.'+ web1+ '.com'
            webbrowser.open(web2)
            speak("Done..")

        if 'open gmail' in tag:
            webbrowser.open_new_tab("mail.google.com")
            speak("Google Mail open now")

        if 'open chrome' in tag:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")

        if 'news' in tag:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
            speak('Here are some headlines from the Times of India, Happy reading')



        if "camera" in tag :
            speak('camera is opening')

            speak('Tell me would you like to take picture or detect the object?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print('waiting...')
                ad = r.listen(source)
                pic = r.recognize_google(ad)
                if "detect object" in pic or "object detect" in pic:
                    print(pic)
                    main()
                else:
                    speak("give name to your picture")
                    pathname1 = listen() + '.png'
                    ec.capture(0, "Camera",os.path.join( "D:\\screenshot\\",pathname1))

        if "alarm" in tag:
            speak("please tell me the time for alarm. example set alarm to 5:30 am :")
            tt = listen()
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            alarm(tt)

except:
    pass