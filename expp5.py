### write a python program to perform arithmetic and bitwise operation on two in image processsing

import cv2

import numpy as np

# Load two images
image1 = cv2.imread(r"C:\Users\DELL\Desktop\IPLab\1bit1.png")
image2 = cv2.imread(r"C:\Users\DELL\Desktop\IPLab\2bit2.png")

# Ensure both images are the same size
image1 = cv2.resize(image1, (200, 200))
image2 = cv2.resize(image2, (200, 200))

# Arithmetic operations
added = cv2.add(image1, image2)  # Add the pixel values
subtracted = cv2.subtract(image1, image2)  # Subtract the pixel values
weighted = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)  # Weighted addition

# Multiply (element-wise multiplication, scaled to avoid overflow)
multiplied = cv2.multiply(image1, image2)

# Divide (element-wise division, handles divide by zero)
divided = cv2.divide(image1, image2)

# Bitwise operations
bitwise_and = cv2.bitwise_and(image1, image2)  # AND operation
bitwise_or = cv2.bitwise_or(image1, image2)  # OR operation
bitwise_xor = cv2.bitwise_xor(image1, image2)  # XOR operation
bitwise_not1 = cv2.bitwise_not(image1)  # NOT operation on the first image
bitwise_not2 = cv2.bitwise_not(image2)  # NOT operation on the second image

# Save results directly
cv2.imwrite("Image1.png", image1)
cv2.imwrite("Image2.png", image2)
cv2.imwrite("Added.png", added)
cv2.imwrite("Subtracted.png", subtracted)
cv2.imwrite("Weighted.png", weighted)
cv2.imwrite("Multiplied.png", multiplied)
cv2.imwrite("Divided.png", divided)
cv2.imwrite("Bitwise_AND.png", bitwise_and)
cv2.imwrite("Bitwise_OR.png", bitwise_or)
cv2.imwrite("Bitwise_XOR.png", bitwise_xor)
cv2.imwrite("Bitwise_NOT_Image1.png", bitwise_not1)
cv2.imwrite("Bitwise_NOT_Image2.png", bitwise_not2)

# Display results
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Added', added)
cv2.imshow('Subtracted', subtracted)
cv2.imshow('Weighted', weighted)
cv2.imshow('Multiplied', multiplied)
cv2.imshow('Divided', divided)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.imshow('Bitwise NOT (Image 1)', bitwise_not1)
cv2.imshow('Bitwise NOT (Image 2)', bitwise_not2)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()


