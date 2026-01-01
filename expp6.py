import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_and_resize(image_path, size=(400, 400)):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Could not load image at {image_path}")
    return cv2.resize(image, size)

def compute_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist

def perform_pixel_operations(image):
    inverted_img = 255 - image
    bright_img = cv2.add(image, 50)
    _, thresholded_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    return {
        'Original': image,
        'Inverted': inverted_img,
        'Brightness +50': bright_img,
        'Thresholded': thresholded_img
    }

def display_images_matplotlib(images_dict, hist):
    plt.figure(figsize=(12, 8))

    # Plot histogram first
    plt.subplot(2, 3, 1)
    plt.title("Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.plot(hist)
    plt.xlim([0, 256])

    # Plot image results
    for i, (name, img) in enumerate(images_dict.items(), start=2):
        plt.subplot(2, 3, i)
        plt.imshow(img, cmap='gray')
        plt.title(name)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = "image3.jpg"  # Change this to your actual image path
    
    try:
        img = load_and_resize(image_path)
        hist = compute_histogram(img)
        results = perform_pixel_operations(img)
        display_images_matplotlib(results, hist)
    except ValueError as e:
        print(e)
