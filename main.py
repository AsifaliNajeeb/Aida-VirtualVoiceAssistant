import ctypes
import pyjokes
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import webbrowser
import wikipedia
import pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning, How can I help you ?")
        talk("Good Morning, How can I help you ?")
    elif 12 <= hour < 18:
        print("Good Afternoon, How can I help you ?")
        talk("Good Afternoon, How can I help you ?")
    else:
        print("Good Evening, How can I help you ?")
        talk("Good Evening, How can I help you ?")


def take_command():
    try:
        with sr.Microphone() as source:
            # listener.adjust_for_ambient_noise(source, duration=1)
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print("You said:{}".format(command))
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'aida' in command:
                command = command.replace('aida', '')
                print(command)
    except:
        pass
    return command


def open_application(name):
    pyautogui.press("win")
    pyautogui.write(name)
    pyautogui.press("enter")


def close_application(name):
    pyautogui.hotkey("alt", "f4")


def run_aida():
    try:
        command = take_command()
        #  print(command)
        if 'play' in command:
            song = command.replace('play', ' ')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            print(date)
            talk("Today's date is " + date)
        elif 'who is' in command:
            search = 'https://www.google.com/search?q=' + command
            print(' Here is what i found on the internet..')
            talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)
        elif 'what is' in command:
            search = 'https://www.google.com/search?q=' + command
            print(' Here is what i found on the internet..')
            talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)
        elif 'tell me about' in command or 'wikipedia' in command:
            person = command.replace('who is ', ' ')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'search' in command:
            search = 'https://www.google.com/search?q=' + command
            print(' Here is what i found on the internet..')
            talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)
        elif "my location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            talk("You must be somewhere near here, as per Google maps")
        elif 'on map' in command:
            loc = command.replace('on map', ' ')
            url = 'https://google.nl/maps/place/' + loc + '/&'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc)
            talk('Here is the location of ' + loc)
        elif 'locate' in command:
            talk('locating ...')
            loc = command.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/' + loc[1] + '/&'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc[1])
            talk('Here is the location of ' + loc[1])
        elif 'location of' in command:
            talk('locating ...')
            loc = command.replace('find location of', '')
            url = 'https://google.nl/maps/place/' + loc + '/&'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc)
            talk('Here is the location of ' + loc)
        elif 'where is ' in command:
            talk('locating ...')
            loc = command.replace('where is', '')
            url = 'https://google.nl/maps/place/' + loc + '/&'
            webbrowser.get().open(url)
            print('Here is the location of ' + loc)
            talk('Here is the location of ' + loc)
        elif 'are you single' in command:
            print("I'm married to the idea of helping people.")
            talk("I'm married to the idea of helping people.")
        elif 'how are you' in command:
            print("Hello, I am fine. Thanks.")
            talk("Hello, I am fine. Thanks.")
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            # print(joke)
        elif 'lock windows' in command:
            talk("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in command:
            talk("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif 'weather' in command:
            city = command.replace('weather', '').strip()
            try:
                weather_info = pywhatkit.search(f"Weather in {city}")
                print(weather_info)
                talk(weather_info)
            except Exception as e:
                print(f"Sorry, I couldn't retrieve the weather information for {city}. Error: {str(e)}")
                talk(f"Sorry, I couldn't retrieve the weather information for {city}. Error: {str(e)}")
        elif 'open' in command:
            try:
                command = take_command()
                if command.startswith("open"):
                    name = command.split(" ")[1]
                    open_application(name)
                elif command.startswith("close"):
                    name = command.split(" ")[1]
                    close_application(name)
                else:
                    pass
            except sr.UnknownValueError:
                print("I didn't understand what you said.")
                talk("I didn't understand what you said.")
            except sr.RequestError:
                print("I couldn't connect to the speech recognition service.")
                talk("I couldn't connect to the speech recognition service.")
        elif 'translate' in command:
            search = 'https://www.google.com/search?q=' + command
            # print(' Here is what I found on the internet..')
            talk('Check it out on Google.')
            webbrowser.open(search)
        else:
            search = 'https://www.google.com/search?q=' + command
            # print(' Here is what I found on the internet..')
            talk('Check it out on Google.')
            webbrowser.open(search)
    except sr.UnknownValueError:
        print("Sorry, That is beyond my ability at the moment.")
        talk("Sorry, That is beyond my ability at the moment.")
    except sr.RequestError:
        print("Sorry could not recognize your voice")
        talk("Sorry could not recognize your voice")


wishMe()
while True:
    run_aida()
