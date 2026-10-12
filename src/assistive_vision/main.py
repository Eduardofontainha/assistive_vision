import cv2 as cv
import time
from assistive_vision.domain.camera import VideoSource
from assistive_vision.infrastructure.opencv_camera import OpenCVCamera
from assistive_vision.infrastructure.yolo_detector import YoloDetector
from assistive_vision.infrastructure.tts_engine import TTSNotifier

def main():
    print("Starting video stream. Press 'q' to exit.")
    
    camera: VideoSource = OpenCVCamera(0)
    detector = YoloDetector("yolov8n.pt")
    prev_time = 0
    audio_notifier = TTSNotifier()
    last_spoken = {}
    SPEAK_COOLDOWN = 4.0 

    #Mapping of YOLO classes (English) to Portuguese
    YOLO_PT = {
        "person": "pessoa",
        "car": "carro",
        "motorcycle": "moto",
        "bus": "ônibus",
        "truck": "caminhão",
        "dog": "cachorro",
        "cat": "gato",
        "chair": "cadeira",
        "couch": "sofá",
        "potted plant": "planta",
        "bed": "cama",
        "dining table": "mesa",
        "door": "porta",
        "cell phone": "celular",
        "cup": "copo",
        "bottle": "garrafa",
        "bowl": "tigela",
        "refrigerator": "geladeira",
        "oven": "forno",
        "microwave": "micro-ondas",
        "toilet": "vaso sanitário",
    }

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
                area = obj.area
    
                height, width, _ = frame.shape
                area_visor = height * width
                
                nome_pt = YOLO_PT.get(obj.label, obj.label)

                if obj.area > 0.4 * area_visor:
                    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    mensagem_audio = f"Cuidado! {nome_pt} muito perto!"

                else:
                    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    mensagem_audio = f"{nome_pt} à frente."
                    label_text = f"{obj.label}: {obj.confidence:.2f}"
                    cv.putText(
                        img=frame,
                        text=label_text,
                        org=(x1, y1 - 10),
                        fontFace=cv.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5,
                        color=(0, 255, 0),
                        thickness=2
                    )
                ultimo_aviso = last_spoken.get(obj.label, 0)
                
                if curr_time - ultimo_aviso > SPEAK_COOLDOWN:
                    audio_notifier.speak(mensagem_audio)
                    last_spoken[obj.label] = curr_time
            
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