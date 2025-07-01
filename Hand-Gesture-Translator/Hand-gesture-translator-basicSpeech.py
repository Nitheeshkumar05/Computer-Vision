import cv2
import mediapipe as mp
import pyttsx3

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Text-to-speech engine
engine = pyttsx3.init()

# Start video capture
cap = cv2.VideoCapture(0)

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    gesture_text = ""

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = frame.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            if lm_list:
                fingers = []

                # Thumb
                if lm_list[4][0] > lm_list[3][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Other four fingers
                for tip_id in [8, 12, 16, 20]:
                    if lm_list[tip_id][1] < lm_list[tip_id - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = fingers.count(1)

                # Gesture to phrase mapping
                if total_fingers == 0:
                    gesture_text = "Hello"
                elif total_fingers == 5:
                    gesture_text = "Goodbye"
                elif total_fingers == 1 and fingers[0] == 1:
                    gesture_text = "Good"
                elif total_fingers == 2 and fingers[1] == 1 and fingers[2] == 1:
                    gesture_text = "I'm fine"
                elif total_fingers == 3:
                    gesture_text = "Did you eat?"
                elif total_fingers == 4:
                    gesture_text = "Thank you"
                elif total_fingers == 5:
                    gesture_text = "How are you?"

                if gesture_text:
                    speak_text(gesture_text)

                # Show text on frame
                cv2.putText(frame, gesture_text, (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Translator", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
