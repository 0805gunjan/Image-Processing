import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('images3.jpeg')
(h, w) = img.shape[:2]

# 1. Reflection (Flipping)
flip_horizontal = cv2.flip(img, 1)  # Horizontal flip
flip_vertical = cv2.flip(img, 0)    # Vertical flip

# 2. Translation
tx, ty = 100, 50  # Shift right by 100 and down by 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, translation_matrix, (w, h))

# 3. Scaling (Resizing)
scaled = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# 4. Rotation (45 degrees around center)
angle = 45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D((w // 2, h // 2), angle, scale)
rotated = cv2.warpAffine(img, rotation_matrix, (w, h))

# 5. Shearing
shear_matrix = np.float32([[1, 0.5, 0],
                           [0.2, 1, 0]])
sheared = cv2.warpAffine(img, shear_matrix, (int(w * 1.5), int(h * 1.5)))

# 6. Interpolation (Resize using different interpolation)
interpolated = cv2.resize(img, (w*2, h*2), interpolation=cv2.INTER_CUBIC)

# ---------- Display Results ----------
titles = ['Original', 'Flip Horizontal', 'Flip Vertical', 'Translated',
          'Scaled (1.5x)', 'Rotated 45°', 'Sheared', 'Interpolated (Cubic)']
images = [img, flip_horizontal, flip_vertical, translated,
          scaled, rotated, sheared, interpolated]

plt.figure(figsize=(15, 10))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('geometric_operations_result.png', dpi=300)
plt.show()
