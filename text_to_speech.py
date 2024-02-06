import pyttsx4

def setup_tts():
    engine = pyttsx4.init()

    voices = engine.getProperty('voices')
    # noinspection PyUnresolvedReferences
    engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', 150)

    return engine


def talk(text, engine):
    engine.say(text)
    engine.runAndWait()