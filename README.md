# Assistive Vision 👁️

An open-source assistive technology project designed to help visually impaired individuals navigate their environment safely. By combining Edge AI (Computer Vision) with embedded systems, this project provides real-time object detection and proximity alerts.

## 🎯 Project Overview

The primary goal of this project is to create a wearable, accessible solution that processes environmental data locally. Currently in its MVP stage, the system uses a standard webcam to detect objects, calculate their proximity via bounding box heuristics, and issue real-time collision warnings via UI and Audio Feedback.

## 🏗️ Software Architecture

This project strictly adheres to **Clean Architecture** and **SOLID** principles to ensure the codebase remains maintainable, testable, and hardware-agnostic. 

* **Domain-Driven Design:** The core business rules (e.g., collision heuristics, `DetectedObject` entity) are completely isolated from external libraries.
* **Dependency Inversion Principle (DIP):** The main orchestrator relies on abstract interfaces (`VideoSource`, `ObjectDetector`), allowing seamless swapping of hardware (e.g., from a PC Webcam to a Raspberry Pi Camera) without altering business logic.
* **Encapsulation:** Entities manage their own state and calculations (e.g., area calculation as a property of the detected object).

### Directory Structure
```text
src/assistive_vision/
├── domain/               # Pure business rules and abstract contracts
│   ├── camera.py         # VideoSource interface
│   └── vision.py         # ObjectDetector interface & DetectedObject entity
├── infrastructure/       # Concrete implementations of external tools
│   ├── opencv_camera.py  # OpenCV adapter
│   └── yolo_detector.py  # Ultralytics YOLOv8 adapter
└── main.py               # Dependency injection and stream orchestration
```
## 🛠️ Tech Stack
* **Language:** Python 3.10+

* **Package Management:** uv

* **Computer Vision:** OpenCV (opencv-python)

* **Artificial Intelligence:** Ultralytics (YOLOv8 Nano - quantized for edge performance)

* **Architecture:** Clean Architecture, SOLID, Design Patterns (Adapter, Dependency Injection)

## 🚀 Getting Started (MVP)
**1.Clone the repository:**

-git clone [https://github.com/your-username/assistive-vision.git](https://github.com/your-username/assistive-vision.git)

-cd assistive-vision

**2.Set up the environment using uv:**

-uv sync

**3.Run the core stream:**
-python -m uv run src/assistive_vision/main.py

Press 'q' to exit the debug video stream.

## 🗺️ Roadmap
**[x]** Phase 1.1: Desktop MVP (Webcam + YOLOv8 + Proximity Heuristics).

**[ ]** Phase 1.2: Audio Feedback (Text-to-Speech alerts for detected obstacles).

**[ ]** Phase 2: Hardware Integration (Arduino real-time proximity sensors via Serial).

**[ ]** Phase 3: Embedded Migration (Porting inference to Raspberry Pi with TFLite/TensorRT).

**[ ]** Phase 4: Haptic Feedback (Vibration motors on wearable frame).

**[ ]** Phase 5: SLAM and Indoor Mapping (Floor plan navigation).

## 📄 License
**This project is licensed under the Apache License 2.0 - see the LICENSE file for details.**
