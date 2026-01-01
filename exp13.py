import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image.jpg', 0)

# Define kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply all morphological operations
operations = {
    "Erosion": cv2.erode(img, kernel, iterations=1),
    "Dilation": cv2.dilate(img, kernel, iterations=1),
    "Opening": cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel),
    "Closing": cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel),
    "Gradient": cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel),
    "Top Hat": cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel),
    "Black Hat": cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
}

# Plotting all operations
plt.figure(figsize=(12, 10))

plt.subplot(3, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

for i, (name, result) in enumerate(operations.items(), start=2):
    plt.subplot(3, 3, i)
    plt.imshow(result, cmap='gray')
    plt.title(name)
    plt.axis('off')

plt.tight_layout()
plt.savefig('morph_ops_output.png', dpi=300)
plt.show()
