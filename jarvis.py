#Following libraries are used in this program.
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import json
import requests

#Set the voice using the 'pyttsx3' modeule
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)
#print(voices[1].id)

#Way to the browser from internet explorer to chrome.
file_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(file_path))

f = webbrowser.get('chrome')

#speak function to give audio output
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#This function is used to wish the user according to the timing
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning Sir')
    elif hour>=12 and hour<16:
        speak('Good afternoon Sir')
    else:
        speak('Good evening Sir')
    speak("I am jarvis ,please tell me how may I help you!")

#This function takes audio input from the user..
def takecommand():
    #it takes microphone input from user and returns the output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.5
        audio = r.listen(source)

#Exception handling...
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language="en-in")
        print(query)

    except Exception:
        #print(e)
        #print('Say that again please...')
        speak('sorry i did not get that , Say that again plaese')
        return 'None'
    return query

#This function is used tos send the email and this is done using the 'smtplib' module of python library
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('#####################','#########')
    server.sendmail('######################',to,content)
    server.close()

#Our main function where the required functions are called...
if __name__ == '__main__':
    wishme()
    while True:
    #if 1:
        query=takecommand().lower()
        #Logic for executing tasks based on query

        #condition to display and read the wikipedia of the required person or company as per demand of the user...
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=90000000)
            speak("According to wikipedia")
            print(results,'\n')
            speak(results)

        #condition to open the youtube as per demand of the user...
        elif 'youtube' in query:
            speak('opening youtube')
            f.open('youtube.com')
            exit()

        #Condition to open the hackerrank website...
        elif 'hackerrank' in query:
            speak("opening hackerrank")
            f.open("hackerrank.com")
            exit()

        #condition to play music using the default the music player..This is done using the 'OS' module
        elif 'play music' in query:
            speak('playing music')
            music_dir="D:\\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            exit()

        #tell the time on demand from the user..This is done using the 'datetime' module of the python library
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        #comdition to open the spotify...This is also done using the 'OS' module.
        elif 'spotify' in query:
            speak('Opening spotify')
            codePath="C:\\Users\\ALOK DUBEY\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
            exit()
        
        #condition to send the email...
        elif "send email" in query:

            #exception handling....
            try:
                speak("What should i say?")
                content=takecommand()
                speak('Enter your email')
                email=str(input('Please enter your email here: '))
                speak('sending')
                print('Sending...')
                to=email
                sendEmail(to,content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak('Sorry Alok,I am not able to send this email')

        #condition to stop the program...This is done using the exit() function...
        elif 'shut' in query:
            speak('good bye,have a nice day')
            exit()

        #condition to give the information about the programming language used,on demand from the user...
        elif 'programming language' in query:
            print('Python')
            speak('python programming language is used to make me')

        #this condition tells the name of the programmer who made this code,on demand from the user....
        elif 'invented' in query:
            speak('Alok made me')

        #condition to open the whatsapp using the 'OS' module...
        elif 'whatsapp' in query:
            speak('opening whatsapp')
            codePath="C:\\Users\\ALOK DUBEY\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
            exit()

        #condition to give the serach result in the chrome browser....
        elif 'search' in query:
            web=query.replace('search','')
            f.open(web)
            speak("Here are the results")
            exit()

        #condition to tell the weather condition of the demanded city...This is done using the weather API...
        elif "weather" in query:
            api_key="0b46db27d088bf2c9ba2e6116ec858f5"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takecommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                      
