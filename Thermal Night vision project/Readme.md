🔥 THERMAL NIGHT VISION FACIAL RECOGNITION & ALERT SYSTEM
A real-time thermal detection and facial recognition system built using YOLOv8 segmentation, OpenCV, Face Recognition library, and a Gradio-based live video interface.

This system applies a dynamic thermal effect to detected human figures, recognizes known faces from a stored database, and triggers alert sounds when unknown persons are detected.

🖥️ Technologies Used
🐍 Python 3.x

🔍 YOLOv8 (ultralytics)

🎥 OpenCV

🧑‍🤝‍🧑 Face Recognition (Dlib based)

🎶 Winsound (for Windows alert sounds)

📊 NumPy

🎛️ Gradio (for real-time web UI)

🎯 Features
✅ Real-time webcam streaming
✅ Human detection using YOLOv8 segmentation
✅ Thermal color mapping applied to detected human regions
✅ Face recognition for known persons from stored images
✅ Dynamic brightness adjustment in low-light conditions
✅ Alert sound for unrecognized individuals
✅ Name labels displayed on screen for recognized faces
✅ Live Gradio-based web interface

📂 Project Structure

📁 Thermal_Face_Alert_System/
├── 📁 models/
│   └── yolov8-seg.pt               # Pre-trained YOLOv8 segmentation model
├── 📁 known_faces/
│   └── person1.jpg                 # Known person images for recognition
├── 📁 utils/
│   └── face_utils.py               # Face recognition and matching functions
│   └── thermal_effect.py           # Thermal color mapping functions
├── main.py                         # Main execution script
├── requirements.txt                # Required Python dependencies
├── README.md                       # Project documentation (this file)
└── 📁 outputs/
    └── captured_unknown_1.png      # Saved frames of unknown persons
