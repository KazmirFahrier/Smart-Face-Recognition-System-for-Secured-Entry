# 👁️‍🗨️ Facial Recognition-Based Attendance & Access Control System

This project implements a **real-time facial recognition system** for attendance marking and access control using Python, OpenCV, and the `face_recognition` library. It captures, encodes, and identifies human faces using live video input, allowing seamless and contactless authentication.

---

## 🧠 Project Overview

The system consists of three primary modules:

1. **Face Capture & Dataset Preparation**
   - Captures headshots using a webcam (or PiCamera).
   - Organizes images for each individual to prepare training data.

2. **Model Training**
   - Encodes facial features from collected images.
   - Saves the encodings using Python’s `pickle` module for future recognition.

3. **Real-Time Recognition & Trigger**
   - Detects and recognizes faces using OpenCV and dlib's deep learning-based face recognition.
   - Identifies individuals and can trigger custom actions (e.g., marking attendance, sending HTTP requests, unlocking doors, etc.).


---

## ⚙️ Technologies Used

- Python 3.x
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- Haar Cascade Classifier (from OpenCV)
- Imutils
- Pickle

---

## 🚀 Example Use Case

- **Smart Classroom Attendance**: Automatically logs students' presence.
- **Door Access System**: Unlocks only for recognized individuals.
- **Employee Tracking**: Logs in/out time for employees without manual input.

---

## 📝 How to Run

1. **Capture Images**  
   Run `headshots_picam.py` to capture training images for individuals.

2. **Train the Model**  
   Use `train_model.py` to generate face encodings and save them to `.pickle` files.

3. **Run Recognition System**  
   Execute `facial_req_and_trigger.py` to begin real-time recognition.

---

## 🔐 Disclaimer

This project was built for educational purposes. For production-grade deployments, consider:
- Using secure data storage.
- Encrypting facial data.
- Implementing access controls and logging.

---

## 🙌 Acknowledgments

- [Adam Geitgey](https://github.com/ageitgey) for the `face_recognition` library.
- OpenCV community and documentation.


