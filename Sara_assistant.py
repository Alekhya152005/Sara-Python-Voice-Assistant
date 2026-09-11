import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
from datetime import datetime


def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()


def processQuestion(question):
    if "hi" in question:
        print("Hello! How can I help you?")
        talk("Hello! How can I help you?")
        return True

    elif 'what are you doing' in question:
        print('I am waiting for your question')
        talk('I am waiting for your question')
        return True

    elif 'how are you' in question:
        print('I am good, thank you. How are you?')
        talk('I am good, thank you. How are you?')
        return True

    elif 'good morning' in question:
        print('Good morning! How can I help you?')
        talk('Good morning! How can I help you?')
        return True

    elif 'good evening' in question:
        print('Good evening! How can I help you?')
        talk('Good evening! How can I help you?')
        return True

    elif 'good night' in question:
        print('Good night! Have a nice day.')
        talk('Good night! Have a nice day.')
        return True

    elif 'play' in question:
        question = question.replace('play', '')
        pywhatkit.playonyt(question)
        return True

    elif 'time' in question:
        time = datetime.today().strftime("%I:%M %p")
        print(time)
        talk(time)
        return True

    elif 'date' in question:
        date = datetime.today().strftime("%d %B %Y")
        print(date)
        talk(date)
        return True

    elif 'open google' in question:
        webbrowser.open("https://www.google.com")
        talk("Opening Google")
        return True

    elif 'bye' in question:
        talk("Bye! Have a nice day.")
        return False

    else:
        print("I didn't get your question, can you say that again?")
        talk("I didn't get your question, can you say that again?")
        return True


def getQuestion():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        question = r.recognize_google(audio)
        print(question)

        question = question.lower()

        if 'sara' in question:
            question = question.replace('sara', '')
            print(question)
            return question

        else:
            print("You are not talking with me, please carry on")
            talk("You are not talking with me, please carry on")
            return "notwithme"

    except sr.UnknownValueError:
        print("Sorry, I can't get your question")
        return "notwithme"


canAskQuestion = True

while canAskQuestion:
    question = getQuestion()

    if question == "notwithme":
        talk("Ok, carry on with your friends, bye!")
        canAskQuestion = False

    else:
        canAskQuestion = processQuestion(question)
