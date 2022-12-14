import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voices', voices[1].id)


# Function to convert text into speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Function to take user voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

 
# Function to wish the user
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am an advance jarvis created by shivam and team for science Exhibition.Sir Please tell me how can I help you.")
 
 
if __name__ == "__main__":
    wish()
    takeCommand()
    
