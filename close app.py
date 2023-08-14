import pyautogui
import speech_recognition as sr


# This function will listen for a voice command and return the text of the command.
def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        print("Listening...")
        audio = recognizer.listen(mic)
    try:
        command = recognizer.recognize_google(audio)
        print("You said: {}".format(command))
        return command
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
        return None


# This function will open the specified application.
def open_application(name):
    pyautogui.press("win")
    pyautogui.write(name)
    pyautogui.press("enter")


# This function will close the specified application.
def close_application(name):
    pyautogui.hotkey("alt", "f4")


# This is the main loop of the program.
while True:
    # Get the voice command.
    command = get_command()
    # If the command is to open an application, open it.
    if command.startswith("open"):
        name = command.split(" ")[1]
        open_application(name)
    # If the command is to close an application, close it.
    elif command.startswith("close"):
        name = command.split(" ")[1]
        close_application(name)
    # Otherwise, do nothing.
    else:
        pass