import cv2 as cv
from assistive_vision.domain.camera import VideoSource
from assistive_vision.infrastructure.opencv_camera import OpenCVCamera

def main():
    print("Starting video stream. Press 'q' to exit.")
    
    camera: VideoSource = OpenCVCamera(0)
    
    if not camera.connect():
        print("Error: Could not connect to the camera.")
        return

    try:
        while True:
            frame = camera.read_frame()
            
            if frame is None:
                print("Error: Could not receive frame from camera.")
                break
                
            cv.imshow("Assistive Vision - Debug Stream", frame)
            
            if cv.waitKey(1) & 0xFF == ord('q'):
                print("Exit signal received.")
                break
                
    finally:
        camera.release()
        cv.destroyAllWindows()
        print("Camera released. Goodbye.")

if __name__ == "__main__":
    main()