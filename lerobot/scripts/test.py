import torch
import torchvision
import cv2
import numpy as np

# Crete a black image
img = np.zeros((100, 100, 3), dtype=np.uint8)

# Show the image
cv2.imshow('Test Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()