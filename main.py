import text_to_speech as TTS

TTS_Engine = TTS.setup_tts()


def main():
    TTS.talk("Hello, How are you?", TTS_Engine)


main()
