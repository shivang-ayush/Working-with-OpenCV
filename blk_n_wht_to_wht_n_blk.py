# ...existing code...
import cv2

img = cv2.imread("SA.png")
if img is None:
    raise SystemExit("Error: SA.png not found")

# convert to grayscale and optionally blur for cleaner edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

# detect edges (white edges on black background)
edges = cv2.Canny(blur, 50, 50)

# invert: black edges on white background
inverted = cv2.bitwise_not(edges)
# alternative: inverted = 255 - edges

# optional: thicken edges (uncomment if you want thicker black borders)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# inverted = cv2.dilate(inverted, kernel, iterations=1)

# show and save
cv2.imshow("Canny (white on black)", edges)
cv2.imshow("Inverted (black on white)", inverted)
cv2.imwrite("SA_canny_inverted.png", inverted)

cv2.waitKey(0)
cv2.destroyAllWindows()
# ...existing code...