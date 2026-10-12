import cv2 as cv
import time
from assistive_vision.domain.camera import VideoSource
from assistive_vision.infrastructure.opencv_camera import OpenCVCamera
from assistive_vision.infrastructure.yolo_detector import YoloDetector

def main():
    print("Starting video stream. Press 'q' to exit.")
    
    camera: VideoSource = OpenCVCamera(0)
    detector = YoloDetector("yolov8n.pt")
    prev_time = 0

    if not camera.connect():
        print("Error: Could not connect to the camera.")
        return

    try:
        while True:
            curr_time = time.time()

            frame = camera.read_frame()
            
            if frame is None:
                print("Error: Could not receive frame from camera.")
                break
            
            detected_objects = detector.detect_objects(frame)

            for obj in detected_objects:
                x1, y1, x2, y2 = obj.bounding_box
                
                # Desenha o retângulo ao redor do objeto (Cor Verde: BGR(0, 255, 0), Espessura: 2)
                cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Prepara o texto com o Rótulo e a Confiança (ex: "person: 0.85")
                label_text = f"{obj.label}: {obj.confidence:.2f}"
                
                # Desenha o texto acima do retângulo
                cv.putText(
                    img=frame,
                    text=label_text,
                    org=(x1, y1 - 10),
                    fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(0, 255, 0),
                    thickness=2
                )
            
            fps = 1 / (curr_time - prev_time) if prev_time > 0 else 0
            prev_time = curr_time
            cv.putText(frame, f"FPS: {int(fps)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
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