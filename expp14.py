import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")

denoised_img = cv2.medianBlur(img, 3)

plt.figure(figsize=(12,10))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(denoised_img, cv2.COLOR_BGR2RGB))
plt.title('original')
plt.axis('off')

plt.tight_layout()
plt.show()