import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load and resize the images
image1 = cv2.imread(r"C:\Users\DELL\Desktop\IPLab\1bit1.png")
image2 = cv2.imread(r"C:\Users\DELL\Desktop\IPLab\2bit2.png")
image1 = cv2.resize(image1, (200, 200))
image2 = cv2.resize(image2, (200, 200))

# Convert BGR to RGB for matplotlib
def convert(img): return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Perform operations
added = cv2.add(image1, image2)
subtracted = cv2.subtract(image1, image2)
weighted = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
multiplied = cv2.multiply(image1, image2)
divided = cv2.divide(image1, image2)

bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_xor = cv2.bitwise_xor(image1, image2)
bitwise_not1 = cv2.bitwise_not(image1)
bitwise_not2 = cv2.bitwise_not(image2)

# Titles and images for plotting
titles = ['Image 1', 'Image 2', 'Added', 'Subtracted',
          'Weighted', 'Multiplied', 'Divided',
          'Bitwise AND', 'Bitwise OR', 'Bitwise XOR',
          'Bitwise NOT 1', 'Bitwise NOT 2']

images = [image1, image2, added, subtracted,
          weighted, multiplied, divided,
          bitwise_and, bitwise_or, bitwise_xor,
          bitwise_not1, bitwise_not2]

# Plot in a 3x4 grid
plt.figure(figsize=(15, 10))
for i in range(12):
    plt.subplot(3, 4, i+1)
    plt.imshow(convert(images[i]))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
