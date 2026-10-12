import numpy as np
from ultralytics import YOLO
from assistive_vision.domain.vision import ObjectDetector, DetectedObject

class YoloDetector(ObjectDetector):
    """
    Concrete adapter for the YOLOv8 model using the Ultralytics library.
    """
    def __init__(self, model_name: str = "yolov8n.pt"):
        self.model = YOLO(model_name)

    def detect_objects(self, image: np.ndarray) -> list[DetectedObject]:

        results = self.model(image, verbose=False)
        
        detected_objects = []
        
        for box in results[0].boxes:
            box_xyxy = tuple(int(x) for x in box.xyxy[0].tolist())
            confidence = float(box.conf[0])
            label = self.model.names[int(box.cls[0])]

            detected_objects.append(DetectedObject(label=label, confidence=confidence, bounding_box=box_xyxy))

        return detected_objects