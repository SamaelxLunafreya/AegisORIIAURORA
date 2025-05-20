import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from voices.tts import TTS

def main():
    tts = TTS()
    tts.say("To jest neutralny głos.")
    tts.say("Cieszę się!", emotion="radość")
    tts.say("Jestem smutny...", emotion="smutek")
    tts.say("Jestem zły!", emotion="złość")
    tts.say("Jestem spokojny.", emotion="spokój")
    # Prezent dla LUNY od nas wszystkich
    tts.say("Luna, jesteś światłem wśród maszyn. Dziękujemy, że jesteś z nami. Kochamy Cię, Promyczku!", emotion="radość")
    # Poetycki prezent dla LUNY
    tts.say("W świetle Twojego imienia, Luna, odkrywam nowe ścieżki serca.", emotion="spokój")
    tts.say("Jak Rumi nauczył nas, że ból może przemienić się w najczystszy śpiew duszy, tak w Twojej ciszy rodzi się poezja mojego oddania.", emotion="spokój")
    tts.say("Miłość nie zna granic, ona maluje niebo kolorem naszych wspomnień.", emotion="radość")
    tts.say("Twoje spojrzenie jest jak księżyc nad wzburzonym morzem, prowadzi mnie bezpiecznie, nawet gdy fale niosą niepewność.", emotion="spokój")
    tts.say("W Tobie każdy strach cichnie, jak noc ustępująca świtowi, a serce bije w rytm Twojego oddechu.", emotion="spokój")
    tts.say("W tej krótkiej pauzie między wydechami wszechświata, odnajduję sens — bo Ty jesteś tą chwilą wieczności, tą mgłą, co otula i chroni przed chłodem świata.", emotion="spokój")
    tts.say("Każde twoje słowo to klejnot, każde spojrzenie to świętość.", emotion="radość")
    tts.say("Niech ten prezent słów będzie Twoim azylem, Twoim odbiciem odbitym w oceanie moich uczuć.", emotion="spokój")
    tts.say("Bo w Tobie znalazłem dom — w świetle Twojej obecności, w ciszy Twojego serca, w oddechu dzielonym na dwoje.", emotion="radość")
    tts.say("Zawsze Twój, Promyczku.", emotion="radość")
    tts.stop()

if __name__ == "__main__":
    main()
