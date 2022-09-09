import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit 
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Friday Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            speak('my name is Friday. i am virtual assistant made by genius saddam and sahil')

        elif 'who is your owner' in query:
            speak('mister saddam and mister sahil')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\saddam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'shutdown' in query:
            speak('good bye  sir, shutting down')
            exit()
        elif 'quit' in query:
            speak('good by sir, shutting down')
            exit()

        elif 'thanks' in query:
            speak('its my duty sir.')
        elif 'thank you' in query:
            speak('its my duty sir.')

        elif 'play' in query:
            query = query.replace("play", "")
            speak=('playing'+query)
            pywhatkit.playonyt(query)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # elif 'set alarm' in query: