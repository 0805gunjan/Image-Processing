import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image, gamma):
    corrected = np.power(image / 255.0, gamma) * 255.0
    return np.uint8(corrected)

# Load the original image
img = cv2.imread('image.jpg')

# Define gamma values to apply
gammas = [0.2, 0.5, 1.5, 2.5]
corrected_images = []

# Apply gamma correction for each value and save
for g in gammas:
    corrected = gamma_correction(img, g)
    corrected_images.append((g, corrected))
    filename = f"gamma_{g}.png"
    cv2.imwrite(filename, corrected)

# Plot original + gamma corrected images
plt.figure(figsize=(15, 6))

plt.subplot(1, len(gammas) + 1, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')

for idx, (g, corrected) in enumerate(corrected_images):
    plt.subplot(1, len(gammas) + 1, idx + 2)
    plt.imshow(cv2.cvtColor(corrected, cv2.COLOR_BGR2RGB))
    plt.title(f"Gamma {g}")
    plt.axis('off')

plt.tight_layout()
plt.savefig('gamma_all_comparison.png', dpi=300)
plt.show()

