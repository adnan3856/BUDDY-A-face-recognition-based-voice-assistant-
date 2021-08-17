import pyttsx3
import pyperclip
def speak(text_audio):
    speaker = pyttsx3.init('sapi5')
    voices = speaker.getProperty('voices')
    voice_id = voices[0].id
    speaker.setProperty('voice', voice_id)
    speaker.setProperty('rate',180)
    speaker.say(text_audio)
    speaker.runAndWait()

# speak("Hello sir , say Wake up Buddy")
# speak("I am Jarvis")
# speak("I am BUDDY. A personal Voice Assistant made by Adnan and Aaman ")
# speak("I am BUDDY, A personal voice assistant made by Adnan and Aaman. Currently I am programmed to do small tasks such as open websites, application, play music... Do you want me to do Something?")