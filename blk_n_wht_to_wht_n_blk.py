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

# optional: thicken edges (dilate the white edges) before inverting
# adjust kernel size and iterations to control thickness
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
dilated = cv2.dilate(edges, kernel, iterations=1)

# invert: black edges on white background
inverted = cv2.bitwise_not(dilated)
# alternative: inverted = 255 - dilated

# show and save
cv2.imshow("Canny (white on black)", edges)
cv2.imshow("Dilated (white on black)", dilated)
cv2.imshow("Inverted (black on white)", inverted)
cv2.imwrite("SA_canny_inverted.png", inverted)

cv2.waitKey(0)
cv2.destroyAllWindows()
# ...existing code...