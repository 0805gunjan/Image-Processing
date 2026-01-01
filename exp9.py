import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('image.jpg')  # Replace with your own image path

# Create the negative image
negative_img = 255 - img

# Save the negative image
cv2.imwrite('negative_image.png', negative_img)

# Display original and negative images
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative_img, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')
plt.axis('off')

plt.tight_layout()
plt.savefig('negative_comparison.png', dpi=300)
plt.show()

