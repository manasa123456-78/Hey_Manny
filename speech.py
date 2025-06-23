import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1.2
        audio = r.listen(source, phrase_time_limit=8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except Exception:
        speak("Sorry, could not understand. Please say again.")
        return "None"
