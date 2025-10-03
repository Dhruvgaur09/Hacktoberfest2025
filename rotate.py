import cv2

# Read image
img = cv2.imread("your_image.jpg")

# Get dimensions
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Rotate 90 degrees clockwise
matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))

# Save & show
cv2.imwrite("rotated_image.jpg", rotated)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
