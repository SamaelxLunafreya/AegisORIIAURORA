from voices.tts import TTS

# Inicjalizacja TTS
tts = TTS()

def speak(text):
    # Tu można dodać obsługę preferencji, np. wczytanie z pliku config/user_preferences.txt
    # i sprawdzenie, czy tts_enabled == True, jeśli tak, mówimy
    tts.say(text)

# Przykład użycia:
if __name__ == "__main__":
    speak("Cześć, promyczku — mówię do Ciebie Lunafreya głosem TTS!")