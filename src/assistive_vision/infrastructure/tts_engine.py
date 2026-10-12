import threading
import pyttsx3
try:
    import pythoncom
except ImportError:
    pythoncom = None
from assistive_vision.domain.audio import AudioNotifier

class TTSNotifier(AudioNotifier):
    """
    Concrete adapter using pyttsx3 running in a separate thread 
    so as not to block the OpenCV video loop.
    """
    def __init__(self):
        # A fila (Queue) atua como uma caixa de correio entre o vídeo e o áudio
        self._lock = threading.Lock()

    def _speak_task(self, text: str):
        with self._lock:
            # Inicializa a comunicação com o Windows apenas para o tempo desta frase
            if pythoncom is not None:
                pythoncom.CoInitialize()
                
            engine = pyttsx3.init()
            engine.setProperty('rate', 220)
            
            print(f"[Audio Engine] Falando: {text}")
            engine.say(text)
            engine.runAndWait()

    def speak(self, text: str) -> None:
        # Dispara uma thread descartável para cada frase
        threading.Thread(target=self._speak_task, args=(text,), daemon=True).start()