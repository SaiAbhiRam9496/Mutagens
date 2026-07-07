# voice.py
# Speech-to-text input and text-to-speech output

import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen():
    """Listens via microphone and returns recognized text, or None if failed."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return None

def speak(text):
    """Speaks the given text out loud."""
    tts_engine.say(text)
    tts_engine.runAndWait()