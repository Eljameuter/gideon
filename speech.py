import speech_recognition as sr
from gtts import gTTS
import os

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio,language="de-DE")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text): 
    # Language in which you want to convert
    language = 'de'
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    result = gTTS(text=text, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    result.save("result.mp3")
    
    # Playing the converted file
    os.system("start result.mp3")