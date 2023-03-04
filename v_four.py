import pyttsx3 # offline voice support ,if will give two voices out 
import speech_recognition as sr # speech recognisition feature 
import datetime 
import wikipedia # accessing wiki
import webbrowser # for accessing webbrowser,opening google ,youtube etc.....
import os # for controlling operating system i.e desktop 
import pyjokes # jokes feature
import pywhatkit as kit # whatsApp feature 
import pyautogui 
import requests
import json

print("Initializing V-four")
# initilaizing microsoft software sapi for voice 
system = pyttsx3.init('sapi5')
voices = system.getProperty('voices')
system.setProperty('voice', voices[1].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    system.say(text)
    system.runAndWait()
# here it access date time library and wishes accordingly 
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("hi,good morning ")

    elif hour>=12 and hour<18:
        speak("hi,good afternoon")

    else:
        speak("hi,good Evening ")

    speak("i am your assistant v four")
    speak("how may i help you ?")

def takeCommand():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print("user said :",query)
        print('processing your request......')
        speak('processing your request ')
    except Exception:
        print('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

#main program 
if __name__ == '__main__':
    greet()
    while True:
        query = takeCommand()

        # features of voice assistant in infine while loop
        if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
            url = "https://youtube.com"
            webbrowser.register('youtube', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('youtube').open(url)

        elif 'open google' in query.lower():
            url='https://www.google.com'
            webbrowser.register('google', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('google').open(url)

        elif 'open code editor' in query.lower():
            codePath = "C:\\Users\\keert\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'joke' in query.lower():
            j=pyjokes.get_joke()
            speak("hope you like this joke master")
            print(j)
            speak(j)

        elif 'send whatsapp message' in query.lower():
                speak('On what number should I send the message ? Please enter in the console: ')
                number = input("Enter the number: ")
                speak("What is the message ?")
                message = takeCommand().lower()
                kit.sendwhatmsg_instantly(f"+91{number}", message)
                pyautogui.press('enter') # Sends the message
                speak("I've sent the message")

        elif 'how are you  v four' in query.lower() or 'how are you  'in query.lower() or'how are you doing  v four' in query.lower() or ' how are you doing ' in query.lower():
            speak(" i am fine thank you for asking ")
        
        elif 'who are you' in query.lower() or 'what can you do' in query.lower():
            speak('I am v four, 1 point O your personal assistant. I am programmed to  do minor tasks like'
                  'opening youtube,google chrome,search wikipedia and if bored tell you a joke' 
                  'or you can also ask me to send your whatsapp message too!')

        elif 'terminate' in query.lower() or 'quit' in query.lower():
            hour = datetime.datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night master, take care!")
                print("terminated")
            else:
                speak('Have a good day master!')
                print("terminated")
            exit()

