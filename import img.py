
import cv2
print("Module Loaded!")

img = cv2.imread("img2.jpg")
print(type(img))
cv2.imshow("Output01", img)
cv2.waitKey(0)

