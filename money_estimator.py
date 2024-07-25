import numpy as np
import cv2

img = cv2.imread('sample-photo.png', cv2.IMREAD_GRAYSCALE)
original_img = cv2.imread('sample-photo.png', 1)
img = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('Detected Money', img)
#cv2.waitkey(0)
#cv2.destroyAllWindows()