from abc import ABC, abstractmethod
import numpy as np

class VideoSource(ABC):
    """
    Abstract contract for any video source in the assistive system.
    Can be implemented by a Webcam, Raspberry Pi Camera,
    or even a mocked video for automated tests.
    """

    @abstractmethod
    def connect(self) -> bool:
        """
        Attempts to establish a connection with the camera hardware.
        
        Returns:
            bool: True if connection is successful, False otherwise.
        """
        pass

    @abstractmethod
    def read_frame(self) -> np.ndarray | None:
        """
        Reads the next frame from the video source.

        Returns:
            np.ndarray: The captured image matrix.
            None: If reading fails or the video ends.
        """
        pass

    @abstractmethod
    def release(self) -> None:
        """
        Turns off the camera and releases operating system hardware resources.
        Ensures there will be no memory leaks.
        """
        pass