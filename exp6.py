## write a python program to compute an image histogram and pixel manipulation like inversion, brightness, adjustment and thresholding in image processing

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
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Number of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()


def perform_pixel_operations(image):
    inverted_img = 255- image
    bright_img = cv2.add(image, 50)
    _, thresholded_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    
    return {
        'Original': image,
        'Inverted': inverted_img,
        'Brightness Adjusted': bright_img,
        'Thresholded': thresholded_img
    }

def display_images(images_dict):
    for name, img in images_dict.items():
        cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "image3.jpg"  # Change to actual image path
    
    try:
        img = load_and_resize(image_path)
        compute_histogram(img)
        results = perform_pixel_operations(img)
        display_images(results)
    except ValueError as e:
        print(e)

