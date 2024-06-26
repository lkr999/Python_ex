import cv2

img = cv2.imread('asset/test_img.jpg', 1)
img = cv2.resize(img, (0,0), fx=2, fy=1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyWindow()