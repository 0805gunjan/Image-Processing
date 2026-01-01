import cv2
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Apply Thresholding
_, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Plotting results with histograms
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Original image and its histogram
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("Original Image")
axes[0, 0].axis('off')
axes[1, 0].hist(img.ravel(), 256, [0, 256])
axes[1, 0].set_title("Histogram - Original")

# Blurred image and its histogram
axes[0, 1].imshow(blurred, cmap='gray')
axes[0, 1].set_title("Gaussian Blurred")
axes[0, 1].axis('off')
axes[1, 1].hist(blurred.ravel(), 256, [0, 256])
axes[1, 1].set_title("Histogram - Blurred")

# Thresholded image and its histogram
axes[0, 2].imshow(thresholded, cmap='gray')
axes[0, 2].set_title("Thresholded Image")
axes[0, 2].axis('off')
axes[1, 2].hist(thresholded.ravel(), 256, [0, 256])
axes[1, 2].set_title("Histogram - Thresholded")

plt.tight_layout()
plt.savefig('gaussian_threshold_hist.png', dpi=300)
plt.show()
