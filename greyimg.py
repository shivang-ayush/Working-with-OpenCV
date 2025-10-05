import cv2

imgNormal = cv2.imread("img2.jpg")
imgGrey = cv2.cvtColor(imgNormal, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (9,9), 0)
imgCanny = cv2.Canny(imgNormal, 150, 200)




cv2.imshow("Normal Image", imgNormal)
cv2.imshow("Grey Image", imgGrey)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)




cv2.waitKey(0)


