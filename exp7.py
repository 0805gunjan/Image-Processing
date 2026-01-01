import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert_to_cmy(image):
    cmy = 1 - image / 255.0
    return (cmy * 255).astype(np.uint8)

def convert_to_cmyk(image):
    r, g, b = cv2.split(image)
    k = np.minimum(np.minimum(255 - r, 255 - g), 255 - b)
    c = (255 - r - k) / (255 - k + 1e-5) * 255
    m = (255 - g - k) / (255 - k + 1e-5) * 255
    y = (255 - b - k) / (255 - k + 1e-5) * 255
    return cv2.merge([c.astype(np.uint8), m.astype(np.uint8), y.astype(np.uint8), k.astype(np.uint8)])

# Read the image
image = cv2.imread(r"images.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Increase brightness
brightness_factor = 50
manipulated_image = np.clip(image + brightness_factor, 0, 255).astype(np.uint8)

# Convert to CMY and CMYK
cmy_image = convert_to_cmy(image)
cmyk_image = convert_to_cmyk(image)
cmy_manipulated = convert_to_cmy(manipulated_image)
cmyk_manipulated = convert_to_cmyk(manipulated_image)

# Convert to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
hsv_manipulated = cv2.cvtColor(manipulated_image, cv2.COLOR_RGB2HSV)

# Split channels
C, M, Y = cv2.split(cmy_image)
K = cmyk_image[:, :, 3]
C_m, M_m, Y_m = cv2.split(cmy_manipulated)
K_m = cmyk_manipulated[:, :, 3]
H, S, V = cv2.split(hsv_image)
H_m, S_m, V_m = cv2.split(hsv_manipulated)

# Organizing the original images in grid format
grid_images_original = [
    [None, None, K, None],
    [image[:, :, 2], Y, cmyk_image[:, :, 2], V],
    [image[:, :, 1], M, cmyk_image[:, :, 1], S],
    [image[:, :, 0], C, cmyk_image[:, :, 0], H],
    [image, cmy_image, cmyk_image, hsv_image]
]

grid_titles = [
    [None, None, "K", None],
    ["B", "Y", "Y (CMYK)", "V"],
    ["G", "M", "M (CMYK)", "S"],
    ["R", "C", "C (CMYK)", "H"],
    ["RGB", "CMY", "CMYK", "HSV"]
]

fig, axes = plt.subplots(5, 4, figsize=(12, 12))
for i in range(5):
    for j in range(4):
        ax = axes[i, j]
        img = grid_images_original[i][j]
        title = grid_titles[i][j]
        if img is not None:
            ax.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        ax.set_title(title, fontsize=10)
        ax.axis('off')

plt.tight_layout()
plt.show()

# Organizing the manipulated images in grid format
grid_images_manipulated = [
    [None, None, K_m, None],
    [manipulated_image[:, :, 2], Y_m, cmyk_manipulated[:, :, 2], V_m],
    [manipulated_image[:, :, 1], M_m, cmyk_manipulated[:, :, 1], S_m],
    [manipulated_image[:, :, 0], C_m, cmyk_manipulated[:, :, 0], H_m],
    [manipulated_image, cmy_manipulated, cmyk_manipulated, hsv_manipulated]
]

fig, axes = plt.subplots(5, 4, figsize=(12, 12))
for i in range(5):
    for j in range(4):
        ax = axes[i, j]
        img = grid_images_manipulated[i][j]
        title = (grid_titles[i][j] + " (Manipulated)") if grid_titles[i][j] else None
        if img is not None:
            ax.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        if title:
            ax.set_title(title, fontsize=10)
        ax.axis('off')

plt.tight_layout()
plt.show()




