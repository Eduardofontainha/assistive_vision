from dataclasses import dataclass
from abc import ABC, abstractmethod
import numpy as np

@dataclass
class DetectedObject:
    label: str
    confidence: float
    bounding_box: tuple[int, int, int, int]  # (x_min, y_min, x_max, y_max)

class ObjectDetector(ABC):
    """
    Abstract contract for any object detection model in the assistive system.
    Can be implemented by a YOLO model, SSD model, or even a mocked detector for automated tests.
    """

    @abstractmethod
    def detect_objects(self, image: np.ndarray) -> list[DetectedObject]:
        """
        Detects objects in the provided image.

        Args:  
            image (np.ndarray): The input image in which to detect objects.
        
        Returns:
            list[DetectedObject]: A list containing the detected objects.
        """
        pass
