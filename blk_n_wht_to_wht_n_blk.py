# ...existing code...
import cv2

# load as grayscale
img = cv2.imread("SA.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise SystemExit("Error: SA.png not found")

# ensure binary black/white (optional if already binary)
_, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# invert colors: black <-> white
inverted = cv2.bitwise_not(bw)
# alternative: inverted = 255 - bw

# show and save result
cv2.imshow("Original (B/W)", bw)
cv2.imshow("Inverted (W/B)", inverted)
cv2.imwrite("SA_inverted.png", inverted)

cv2.waitKey(0)
cv2.destroyAllWindows()
# ...existing code...