import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
#you need to make changes in the following lines to make J.A.R.V.I.S. as per your convineice :
# 1. where ever you see Tushar you can change it to your name
# 2. on line no. 65 and 66 you have to put youur email
# 3. on line no. 65 you have to put the password of your mail (don't worry it is safe because the file remains with you only.)
# 4. on line no. 110 you have to put the person's name whom you want to mail
# 5. on line no. 97 and 108 youu have to chane the directory as per your system
# 6. if youu want the J.A.R.V.I.S. to respond in a female's voice then on line no. 22 change [0] to [1]
#___NOTE___ install all the modules above only then the code will work 




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Tushar Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry sir I did not understood it...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("YOUREMAIL@GMAIL.COM", "YOUR PASSWORD")         #enter your email and password here
    server.sendmail("YOUREMAIL@GMAIL.COM", to, content)          #enter your email
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\\Non Critical\\songs\\Favorite Songs2"                                   #change the directory
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\tushar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   #change the directory
            os.startfile(codePath)
            
        elif "send an email to PERSON'S NAME" in query:                       #change the peron's name
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Okay sir.")
                to = "PERSON'SEMAIL@GMAIL.COM"                                #put the person's email here , whom you are talking
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Tushar sir. I am not able to send this email")
