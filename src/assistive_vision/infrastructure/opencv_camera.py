from assistive_vision.domain.camera import VideoSource
import cv2 as cv
import numpy as np

class OpenCVCamera(VideoSource):
    """
    OpenCV adapter for local webcams.
    """
    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.cap = cv.VideoCapture(self.camera_index)

    def connect(self) -> bool:
        return self.cap.isOpened()

    def read_frame(self) -> np.ndarray | None:
        if not self.cap.isOpened():
            return None
            
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def release(self) -> None:
        if self.cap.isOpened():
            self.cap.release()