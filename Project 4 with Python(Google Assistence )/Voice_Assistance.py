import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time
import os

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing.... ")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError :
            print(" Not Understand ")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    # if "hey ankit" in sptext():

        while True :
            data1=sptext()
            try:
                if "your name" in data1:
                    name = " my name is ankit mishra "
                    speechtx(name)

                elif "old are you" in data1:
                    age = "i am twentyfour years old"
                    speechtx(age)

                elif 'time' in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif 'google' in data1:
                    webbrowser.open("https://www.google.co.in/")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="neutral")
                    print(joke_1)
                    speechtx(joke_1)

                elif 'play song' in data1:
                    add = r"D:\New folder\songs"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add,listsong[0]))

                elif "exit" in data1:
                    speechtx('thank you')
                    break
            except Exception as e:
                print('Try again in 1 sec')
            time.sleep(1)

        else:
            print("thanks")
