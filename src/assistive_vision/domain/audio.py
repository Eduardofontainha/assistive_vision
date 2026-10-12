from abc import ABC, abstractmethod

class AudioNotifier(ABC):
    """
    Abstract contract for the issuance of audible alerts.
    """
    
    @abstractmethod
    def speak(self, text: str) -> None:
        """
        Receives a text and plays it as audio without blocking the main thread.
        """
        pass