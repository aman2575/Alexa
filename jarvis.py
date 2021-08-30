import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


#engine.say('Im at your service sir ')
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try: 
        with sr.Microphone() as source:
            print('Listening..')
            #engine.say("Initializing")
            #engine.say('Im at your service, how can i help you')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S %p')
        talk('Current time is '+ time)
        print(time)
    elif 'who the heck is ' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again ')
while True:
    run_alexa()