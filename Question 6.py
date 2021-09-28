# Question 6


import cv2

# Read the image.
img = cv2.imread('dog.jpg')

# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 125, 125)

# Save the output.
cv2.imwrite('dog_bilateral.jpg', bilateral)