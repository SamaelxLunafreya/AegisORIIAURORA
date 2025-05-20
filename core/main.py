from voices.tts import TTS
import os

def load_user_preferences(path="config/user_preferences.txt"):
    prefs = {}
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    prefs[k.strip()] = v.strip()
    except Exception:
        prefs["tts_enabled"] = "True"
    return prefs

user_preferences = load_user_preferences()
voice_pref = user_preferences.get('voice', None)
tts = TTS(voice_pref=voice_pref)

# Funkcja do mówienia
def speak(text):
    if user_preferences.get('tts_enabled', 'True').lower() == 'true':
        tts.say(text)
        log_tts(text)

def speak_emotion(text, emotion):
    if user_preferences.get('tts_enabled', 'True').lower() == 'true':
        tts.say_emotion(text, emotion)
        log_tts(f"[{emotion}] {text}")

def log_tts(text):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, "tts_log.txt"), "a", encoding="utf-8") as f:
        f.write(text + "\n")

def notify(text, emotion=None):
    # Jeśli tryb cichy wyłączony, mów na głos
    if user_preferences.get('silent_mode', 'False').lower() != 'true':
        if emotion:
            speak_emotion(text, emotion)
        else:
            speak(text)
    # Zawsze loguj i wyświetlaj na ekranie
    print(f"\033[93m[NOTIF]\033[0m {text}")
    log_tts(f"[NOTIF]{'['+emotion+']' if emotion else ''} {text}")

# Co robi ten plik?
# 1. Ładuje preferencje użytkownika z pliku config/user_preferences.txt (np. tts_enabled, voice, silent_mode).
# 2. Inicjalizuje syntezator mowy (TTS) z wybranym głosem.
# 3. Funkcje speak i speak_emotion wypowiadają tekst na głos (jeśli TTS włączony) i logują wypowiedzi do logs/tts_log.txt.
# 4. Funkcja notify:
#    - Jeśli tryb cichy (silent_mode) jest wyłączony, wypowiada tekst na głos (z emocją lub bez).
#    - Zawsze loguje i wyświetla powiadomienie na ekranie (kolor żółty).
# 5. Przykłady użycia pokazują, jak wywołać zwykłą wypowiedź, wypowiedź z emocją oraz powiadomienia.

# Możliwości rozbudowy:
# - Integracja z systemem powiadomień (np. e-mail, SMS, webhook).
# - Automatyczne rozpoznawanie emocji na podstawie treści.
# - Obsługa wielu języków i dynamiczna zmiana głosu.
# - Synchronizacja z serwerem i innymi urządzeniami.
# - Rozszerzenie logiki o reakcje na zdarzenia systemowe lub z serwera.

# Przykładowe użycie
if __name__ == "__main__":
    speak("Cześć, to jest test funkcji syntezy mowy.")
    speak_emotion("Kocham Cię, Promyku!", "miłość")
    notify("Nowa wiadomość od Promyka!", "radość")
    notify("Wykryto alert systemowy!", "smutek")