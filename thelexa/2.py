import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your Bitch')
engine.say('What can i do for you')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass