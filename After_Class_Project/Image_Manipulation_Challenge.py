import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

brightness = 0 
crop_percent = 0.0  
rotation_state = 0 

print("Controls:\n 'w'/'s' = Brightness | 'a'/'d' = Crop/Zoom | 'r' = Rotate | 'q' = Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to Capture Image")
        break

    frame = cv2.convertScaleAbs(frame, alpha=1, beta=brightness)

    if rotation_state == 1:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_state == 2:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
    elif rotation_state == 3:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    if crop_percent > 0:
        h, w, _ = frame.shape
        ymin, ymax = int(h * crop_percent), int(h * (1 - crop_percent))
        xmin, xmax = int(w * crop_percent), int(w * (1 - crop_percent))

        if ymax > ymin and xmax > xmin:
            frame = frame[ymin:ymax, xmin:xmax]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w_face, h_face) in faces:
        cv2.rectangle(frame, (x, y), (x + w_face, y + h_face), (255, 0, 0), 2)
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Bright: {brightness} | Crop: {int(crop_percent*100)}%', (10, 60), font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    
    cv2.imshow("Interactive Face Detection", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('w'):    
        brightness = min(brightness + 10, 255)
    elif key == ord('s'):     
        brightness = max(brightness - 10, -255)
    elif key == ord('a'):     
        crop_percent = min(crop_percent + 0.05, 0.45)
    elif key == ord('d'):    
        crop_percent = max(crop_percent - 0.05, 0.0)
    elif key == ord('r'):     
        rotation_state = (rotation_state + 1) % 4

cap.release()
cv2.destroyAllWindows()