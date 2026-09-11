import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

baseline_brightness = None
calibration_frames = 0

print("Starting... Keep a neutral, still face for the first 30 frames to calibrate.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to Capture Image")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        mouth_y1 = int(y + (h * 0.65))
        mouth_y2 = int(y + (h * 0.9))
        mouth_x1 = int(x + (w * 0.25))
        mouth_x2 = int(x + (w * 0.75))
        
        cv2.rectangle(frame, (mouth_x1, mouth_y1), (mouth_x2, mouth_y2), (0, 255, 0), 1)
        
        mouth_roi = gray[mouth_y1:mouth_y2, mouth_x1:mouth_x2]
        
        if mouth_roi.size > 0:
            current_brightness = np.mean(mouth_roi)
            
            if calibration_frames < 30:
                if baseline_brightness is None:
                    baseline_brightness = current_brightness
                else:
                    baseline_brightness = (baseline_brightness * 0.9) + (current_brightness * 0.1)
                
                calibration_frames += 1
                status_text = f"Calibrating... ({calibration_frames}/30)"
            
            else:
                diff = current_brightness - baseline_brightness
                
                if diff > 3.5:
                    status_text = "Expression: Smile / Expression Shift"
                elif diff < -3.5:
                    status_text = "Expression: Frown / Closed Shape"
                else:
                    status_text = "Expression: Neutral"
            
            cv2.putText(frame, status_text, (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Zero-Download Contrast Tracker - Press 'q' to quit", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        baseline_brightness = None
        calibration_frames = 0
        print("Re-calibrating baseline...")

cap.release()
cv2.destroyAllWindows()