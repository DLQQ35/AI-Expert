import cv2
import numpy as np

def apply_filters(image, ftype):
    img = image.copy()
    if ftype == 'red_tint':
        img[:, :, 0] = img[:, :, 1] = 0
    elif ftype == 'green_tint':
        img[:, :, 0] = img[:, :, 2] = 0
    elif ftype == 'blue_tint':
        img[:, :, 1] = img[:, :, 2] = 0
    elif ftype == 'sobel':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sob = cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif ftype == 'canny':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)
    elif ftype == 'cartoon':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 300, 300)
        img = cv2.bitwise_and(color, color, mask=edges)
    elif ftype == 'sepia':
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        img = cv2.transform(img, kernel)
        img = np.clip(img, 0, 255).astype(np.uint8)
    elif ftype == 'invert':
        img = cv2.bitwise_not(img)
    elif ftype == 'grayscale':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif ftype == 'original':
        img = image.copy()
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    ftype = "original"
    print('Keys: r - red tint, g - green tint, b - blue tint, s - sobel, c - canny, t - cartoon, i - invert, y - grayscale, o - original, p - sepia, q - quit')
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to Capture Image")
            break
        out = apply_filters(frame, ftype)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            ftype = "red_tint"
        elif key == ord('g'):
            ftype = "green_tint"
        elif key == ord('b'):
            ftype = "blue_tint"
        elif key == ord('s'):
            ftype = "sobel"
        elif key == ord('c'):
            ftype = "canny"
        elif key == ord('t'):
            ftype = "cartoon"
        elif key == ord('i'):
            ftype = "invert"
        elif key == ord('y'):
            ftype = "grayscale"
        elif key == ord('o'):
            ftype = "original"
        elif key == ord('p'):
            ftype = "sepia"
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()