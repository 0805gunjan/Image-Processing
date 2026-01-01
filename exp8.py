import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Simulate Overexposed and Underexposed images
overexposed = cv2.convertScaleAbs(img, alpha=1.5, beta=50)
underexposed = cv2.convertScaleAbs(img, alpha=0.5, beta=-50)

# Apply Histogram Equalization
equalized_over = cv2.equalizeHist(overexposed)
equalized_under = cv2.equalizeHist(underexposed)

# Save adjusted images
cv2.imwrite('equalized_overexposed.png', equalized_over)
cv2.imwrite('equalized_underexposed.png', equalized_under)

# Plotting and Saving Histogram Plots
def plot_and_save(title, original, equalized, filename):
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs[0, 0].imshow(original, cmap='gray')
    axs[0, 0].set_title(f"{title} - Original")
    axs[0, 0].axis('off')

    axs[0, 1].imshow(equalized, cmap='gray')
    axs[0, 1].set_title(f"{title} - Equalized")
    axs[0, 1].axis('off')

    axs[1, 0].hist(original.ravel(), 256, [0, 256], color='gray')
    axs[1, 0].set_title("Original Histogram")

    axs[1, 1].hist(equalized.ravel(), 256, [0, 256], color='gray')
    axs[1, 1].set_title("Equalized Histogram")

    plt.tight_layout()
    plt.savefig(f'{filename}', dpi=300)
    plt.show()

# Save both cases
plot_and_save("Overexposed", overexposed, equalized_over, "histogram_overexposed.png")
plot_and_save("Underexposed", underexposed, equalized_under, "histogram_underexposed.png")



