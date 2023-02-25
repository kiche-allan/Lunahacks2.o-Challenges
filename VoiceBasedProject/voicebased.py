import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "Sorry, I didn't catch that."
    
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def main():
    while True:
        text = get_audio()
        speak(text)
        if "stop" in text:
            break
        
if __name__ == "__main__":
    main()

