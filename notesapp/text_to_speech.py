import pyttsx3
from pathlib import Path


VOICE_DIR = str(Path(__file__).resolve().parent) + "\\media\\voice_notes\\"


class TxtToAudioConverter:
    def set_rate(self, rate=130):
        self.__engine.setProperty('rate', rate)

    def __init__(self, path=str(Path(__file__).resolve().parent)):
        self.__engine = pyttsx3.init()
        self.__path = path
        self.set_rate()

    def generate(self, text, name):
        note_voice_path = VOICE_DIR + f'{name}.mp3'
        self.__engine.save_to_file(text, note_voice_path)
        self.__engine.runAndWait()
        return note_voice_path


if __name__ == "__main__":
    actor = TxtToAudio(VOICE_DIR)
    actor.generate("The quick brown fox jumped over the lazy dog.", 'test')
