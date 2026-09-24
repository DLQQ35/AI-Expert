import cv2, time, pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

SCROLL_SPEED = 300
SCROLL_DELAY = 1
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == 'Right' and thumb_tip.x > thumb_ip.x) or (handedness == 'Left' and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    return 'Scroll_up' if sum(fingers) == 5 else 'Scroll_down' if len(fingers) == 0 else 'None'
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)
last_scroll = p_time = 0
print("Gesture Scroll Control activated \n Open Palm : Scroll Up \n Close Fist : Scroll Down")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
    results = hands.process(img)
    gesture = detect_gesture(results.multi_hand_landmarks[0], results.multi_handedness[0].classification[0].label) if results.multi_hand_landmarks else 'None'
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness = handedness.classification[0].label
            mp_drawing.draw_landmarks(img, hands, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks, handedness)
            if gesture == "Scroll_up":pyautogui.scroll(SCROLL_SPEED)
                pyautogui.scroll(SCROLL_SPEED)
                last_scroll = c_time
            elif gesture == 'Scroll_down' and c_time - last_scroll > SCROLL_DELAY:
                pyautogui.scroll(-SCROLL_SPEED)
                last_scroll = c_time

    c_time = time.time()
    fps = 1 / (c_time - p_time) if c_time != p_time else 0
    p_time = c_time
    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Gesture Based Scrolling Control', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break