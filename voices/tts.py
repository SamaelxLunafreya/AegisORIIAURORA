import pyttsx3

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)    # prędkość mowy
        self.engine.setProperty('volume', 1.0)  # głośność (0.0–1.0)

    def say(self, text: str, emotion: str = None):
        # Ustawienia emocji
        if emotion == "radość":
            self.engine.setProperty('rate', 180)
            self.engine.setProperty('volume', 1.0)
        elif emotion == "smutek":
            self.engine.setProperty('rate', 110)
            self.engine.setProperty('volume', 0.7)
        elif emotion == "złość":
            self.engine.setProperty('rate', 170)
            self.engine.setProperty('volume', 1.0)
        elif emotion == "spokój":
            self.engine.setProperty('rate', 130)
            self.engine.setProperty('volume', 0.8)
        else:
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 1.0)
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()
