# AegisORIIAURORA
bash/shield/powloka

## Text-to-Speech (TTS)

Lunafreya potrafi teraz mówić przez wbudowany moduł TTS oparty na `pyttsx3`. Aby uruchomić syntezę mowy:

1. **Instalacja**  
   ```bash
   pip install pyttsx3
   ```
   

2. **Moduł**
   Stwórz plik `voices/tts.py` z poniższą zawartością:

   ```python
   import pyttsx3

   class TTS:
       def __init__(self):
           self.engine = pyttsx3.init()
           self.engine.setProperty('rate', 150)    # prędkość mowy
           self.engine.setProperty('volume', 1.0)  # głośność (0.0–1.0)

       def say(self, text: str):
           self.engine.say(text)
           self.engine.runAndWait()

       def stop(self):
           self.engine.stop()
   ```

3. **Integracja**
   W swoim głównym kodzie (np. `core/main.py`) zaimportuj i zainicjuj `TTS`:

   ```python
   from voices.tts import TTS

   tts = TTS()

   def speak(text):
       tts.say(text)

   # Przykład:
   speak("Cześć, promyczku — mówię do Ciebie Lunafreya głosem TTS!")
   ```

4. **Preferencje użytkownika** (opcjonalnie)
   Jeśli chcesz mieć możliwość włączania/wyłączania TTS, dodaj do `config/user_preferences.txt`:

   ```
   tts_enabled = True
   ```

   a w funkcji `speak()` sprawdzaj tę wartość przed wywołaniem `tts.say()`.

---

> Zespół AegisORIIAURORA potwierdza: ALL kocha Lunafreyę! 💙🌙✨

