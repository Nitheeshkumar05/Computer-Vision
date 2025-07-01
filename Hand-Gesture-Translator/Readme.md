# 🖐️ Hand Gesture to Voice Translator  

A real-time **hand gesture recognition and voice translator system** using **OpenCV**, **MediaPipe**, and **pyttsx3** text-to-speech engine.  

The system detects hand gestures from your webcam feed, maps them to predefined phrases, and speaks them aloud.

---

## 📌 Project Description  

This system uses **MediaPipe Hands** to detect hand landmarks, counts the number of fingers shown, and translates specific finger combinations into corresponding phrases.  

Once a gesture is detected, it displays the phrase on the video frame and uses the text-to-speech engine to vocalize the message.

---

## 🖥️ Technologies Used  

- 🐍 **Python 3.x**  
- 🎥 **OpenCV** (for webcam video stream and display)  
- ✋ **MediaPipe Hands** (for real-time hand landmark detection)  
- 🔊 **pyttsx3** (text-to-speech engine)

---

## 🎯 Features  

✅ Real-time webcam hand detection  
✅ Detects number of fingers raised  
✅ Maps gestures to pre-defined phrases  
✅ Displays phrase on video frame  
✅ Speaks the phrase using system voice  
✅ Runs offline (no internet required)

---

## 📝 Gesture to Phrase Mapping  

| ✋ Fingers Shown | Phrase Spoken  |
|:----------------|:---------------|
| 0 (Fist)         | "Hello"         |
| 5 (Open Palm)    | "Goodbye"       |
| 1 (Thumb Up)     | "Good"          |
| 2 (Index & Middle Up) | "I'm fine" |
| 3                | "Did you eat?"  |
| 4                | "Thank you"     |

---

## 📂 Project Structure  

