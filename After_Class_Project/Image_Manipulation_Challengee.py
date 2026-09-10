import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('After_Class_Project\\DJ Cat.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image_rgb, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title('Rotated Image')
plt.show()

brightness_matrix = np.ones(image_rgb.shape, dtype='uint8') * 50
brighter = cv2.add(image_rgb, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title('Brighter Image')
plt.show()

cropped_image = image[100:200, 100:200]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title('Cropped Image')
plt.show()