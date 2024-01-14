# import cv2
# import numpy as np
# from random import randint

# with open('white-uget-uget-2-patched/train/labels/SX-S-23_png.rf.ae17b0b1e35a82af984873dcf22ec750.txt', 'r') as f:
#     labels = f.read().splitlines()
# img = cv2.imread('white-uget-uget-2/train/images/SX-S-23_png.rf.ae17b0b1e35a82af984873dcf22ec750.jpg')
# h,w = img.shape[:2]

# for label in labels:
#     class_id, *poly = label.split(' ')
    
#     poly = np.asarray(poly,dtype=np.float16).reshape(-1,2) # Read poly, reshape
#     poly *= [w,h] # Unscale
    
#     cv2.polylines(img, [poly.astype('int')], True, (randint(0,255),randint(0,255),randint(0,255)), 2) # Draw Poly Lines
#     # cv2.fillPoly(img, [poly.astype('int')], (randint(0,255),randint(0,255),randint(0,255)), cv2.LINE_AA) # Draw area


# cv2.imshow('img with poly', img)
# # wait for 5 seconds
# cv2.waitKey(3000)

import cv2
import numpy as np
from random import randint

with open('white-uget-uget-2-patched/train/labels/SX-S-23_png.rf.ae17b0b1e35a82af984873dcf22ec750_0.txt', 'r') as f:
    labels = f.read().splitlines()
img = cv2.imread('white-uget-uget-2-patched/train/images/SX-S-23_png.rf.ae17b0b1e35a82af984873dcf22ec750_0.jpg')
h,w = img.shape[:2]

for label in labels:
    class_id, *poly = label.split(' ')
    
    poly = np.asarray(poly,dtype=np.float16).reshape(-1,2) # Read poly, reshape
    poly *= [w,h] # Unscale
    
    cv2.polylines(img, [poly.astype('int')], True, (randint(0,255),randint(0,255),randint(0,255)), 2) # Draw Poly Lines
    # cv2.fillPoly(img, [poly.astype('int')], (randint(0,255),randint(0,255),randint(0,255)), cv2.LINE_AA) # Draw area


cv2.imshow('img with poly', img)
# wait for 5 seconds
cv2.waitKey(3000)