import cv2
import matplotlib.pyplot as plt

# Load the noisy image
img = cv2.imread('image.jpg')

# Apply median filter to remove salt-and-pepper noise
denoised_img = cv2.medianBlur(img, 3)  # You can also try 5 or 7

# Save the filtered image
cv2.imwrite('denoised_image.png', denoised_img)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original (with noise)")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(denoised_img, cv2.COLOR_BGR2RGB))
plt.title("Denoised Image")
plt.axis('off')

plt.tight_layout()
plt.savefig('salt_pepper_comparison.png', dpi=300)
plt.show()
