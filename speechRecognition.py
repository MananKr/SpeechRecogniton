import speech_recognition as sr  # importing Google Speech API (speech_recognition)
import pyttsx3                       # pyttsx3 is a text-to-speech conversion library in Python
import pywhatkit                     # it is one of the most popular library for WhatsApp and YouTube automation
import datetime                    # importing datetime for time information
from datetime import timedelta        # It supports extracting texts, sections, links, categories, translations, etc from Wikipedia.
import wikipedia                      # wikipedia for searching the documents type information
import pyjokes                        # pyjokes for joke module
import warnings                       # for ignoring the os warnings

warnings.filterwarnings("ignore")
listener = sr.Recognizer()  # an object " listener " which recognises the voice
engine = pyttsx3.init()  # engine connects us to hardware in this case
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 185)  # setting up new voice rate
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. [0 for male , 1 for female ]


def talk(text):
    engine.say(text)
    engine.runAndWait()                           # Runs for small duration of time otherwise we may not be able to hear


def take_command():                       # write a function
    try:                                  # for exception handling block
        with sr.Microphone() as source:                             # I use my laptop mic for as a command
            print("I'm listening...")                           # for feedback checkin my input source is working or nor
            voice = listener.listen(source)                     # input command stored in variable
            command = listener.recognize_google(voice)         # variable pass to listener.recognize_google() model) & store in another variable
            command = command.lower()                          # command object's text data convert into lower case text
            if 'kumar' in command:                              # checking my data is available or not
                command = command.replace('kumar', '')            # renaming the object of command, we  always give command through "shri"
                print(command)
    except:  # skeeping the except block of statement
        pass

    return command


def run_Kumar():                 # inside run_Kumar function check input cmd
    command = take_command()                  # after that this line next function executed which name take_command
    print(command)
    if 'play' in command:                   # multiple condition write inside function which I want to perform through system
        song = command.replace('play', '')         # play cmd for pywhatkit.playonyt
        talk('playing ' + song)
        pywhatkit.playonyt(song)                # pywhatkit pass the data playonyt(youtub)

    elif 'current time is ' in command:                   # asking the time for system
        time = datetime.datetime.now().strftime('%I:%M %p')          # convert datetime into string then print
        print(time)
        talk('Current Time is ' + time)                 # my system speak to time

    elif 'send to message' in command:                    # write send command
        dt = datetime.datetime.now()                        # dt = datetime(2023, 9, 24, 9, 30, 35)
        result = dt + timedelta(hours=0, minutes=1)           # after that i add 3 minutes more in actual time
        result = result.strftime('%I%M')  # # after that again stored time(only hrs,min) in new object
        r = str(result)
        t = []  # create new empty list obj for storing the value of r obj.
        for i in r:
            t.append(int(i))            # I value storing the empty list obj of "t"
        p = t[:2]                     # p is list data type, index 0-2 value =  hours time
        q = t[2:]                       # q is list data type, index 2-4 value =  minutes time
        h = int(''.join(str(x) for x in p))              # join the p list value
        m = int(''.join(str(x) for x in q))                # join the p list value
        # Send a WhatsApp Message to a Contact at hour:minutes PM
        pywhatkit.sendwhatmsg("+918649965xyz", "Hi Manan.! pls. call me... ", h, m)  # through pywhatkit.sendwhatmsg send messages to friend
        print("your request sent in your friend whatsapp number")              # receiving feedback from print function through
        talk('your request sent in your friend whatsapp number ')            # receving feedback from talk function through( from os)

    elif 'speak to' in command:                        # passing cmd extract the information from wikipedia
        person = command.replace('speak to', '')  # from here "shri say" cmd replace for person object and other is treated as
        # input cmd
        info = wikipedia.summary(person, 1)  # by input search in wikipedia and pass the data into info object
        print(info)                    # print the information which I extract from wikipedia
        talk(info)                     # system speak the information which I extract from wikipedia

    elif 'are you available' in command:
        print('Yes, I am available...with wifi')
        talk('Yes, I am available...with wifi')

    elif 'speak joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')


while True:                                 # if source (mic) passing the data to execute the function of run_kumar
    run_Kumar()
