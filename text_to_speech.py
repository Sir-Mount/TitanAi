import os


def speak(text):
    os.popen('espeak "' + text + '"')