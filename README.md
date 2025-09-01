# ✋ Hand Gesture Volume & Brightness Control using OpenCV  

A **real-time computer vision project** that uses **hand gestures** to control **system volume** and **screen brightness**.  
Built using **Python, OpenCV, and MediaPipe**, this project leverages hand landmarks (thumb and index finger distance) to map finger movement into control actions.  

---

## 📑 Table of Contents  

- [📖 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [🚀 Installation](#-installation)  
- [⚙️ Setup](#️-setup)  
- [🖥️ Usage](#️-usage)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📌 Requirements](#-requirements)  
- [🏗️ Project Structure](#️-project-structure)  
- [📄 License](#-license)  
- [🤝 Contributing](#-contributing)  
- [📧 Contact](#-contact)  

---

## 📖 Introduction  

This project enables **touchless control of volume and brightness** using a webcam.  
It detects the **distance between the thumb and index finger tips** and maps it to system commands:  

- **Brightness Control** → Adjusts screen brightness  
- **Volume Control** → Adjusts system volume  

The system runs in real time with smooth visual feedback including FPS, control bars, and percentages.  

---

## ✨ Features  

- 🖐️ **Hand Gesture Recognition** → Detects landmarks using MediaPipe  
- 🔊 **Volume Control** → Adjust volume by pinching thumb and index finger  
- 💡 **Brightness Control** → Adjust screen brightness using gestures  
- ⚡ **Real-Time Processing** → Runs at high FPS via OpenCV  
- 📊 **Visual Feedback** → On-screen bar indicators and live percentage  

---

## 🚀 Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/<your-username>/Hand-Gesture-Volume-Brightness-Control.git
cd Hand-Gesture-Volume-Brightness-Control
pip install -r requirements.txt
```

---

## ⚙️ Setup

1. Ensure your webcam is connected and accessible.

2. For Windows, pycaw library is used for system audio control.

3. For brightness control, screen_brightness_control is required (works on most laptops/desktops).

```bash
# For Volume Control
python gesture_volume_control.py

# For Brightness Control
python gesture_brightness_control.py

```

---

## 🖥️ Usage

1. Place your hand in front of the webcam.
2. Pinch Thumb & Index finger closer/further apart:
   * Small distance → Lower Volume/Brightness
   * Large distance → Higher Volume/Brightness
3. Live percentage and bar are displayed on screen.
---

## 🛠️ Tech Stack

* Python → Core language
* OpenCV → Image processing
* MediaPipe → Hand landmark detection
+ NumPy → Calculations
* PyCaw → Windows system audio control
* Screen Brightness Control → Brightness adjustment

---

## 📌 Requirements

See [requirements.txt](https://github.com/Mohd-Muzammil7052/hand_gesture_volume_and_brightness_control_using_opencv/blob/main/requirements.txt) for all dependencies:

```text
opencv-python
mediapipe
numpy
pycaw
screen-brightness-control
comtypes
```

---

## 🏗️ Project Structure  

```text
📦 Hand-Gesture-Volume-Brightness-Control
 ┣ 📜 gesture_brightness_control.py   # Controls brightness with hand gestures
 ┣ 📜 gesture_volume_control.py       # Controls volume with hand gestures
 ┣ 📜 hand_tracking_module.py         # Hand detection & landmark tracking
 ┣ 📜 requirements.txt                # Dependencies
 ┗ 📜 README.md                       # Documentation

```

## 📄 License  

This project is licensed under the [MIT License](https://opensource.org/license/mit).  
Feel free to use, modify, and distribute it as needed.

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve this project:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📧 Contact  

For queries or collaborations:  

**Mohd Muzammil**  
- [GitHub](https://github.com/Mohd-Muzammil7052)  
- [LinkedIn](https://www.linkedin.com/in/mohd-muzammil-109044290/) 
