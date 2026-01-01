import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_histogram(image):
    # Convert to grayscale if not already
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Compute histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    # Plot histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Number of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

def invert_image(image):
    return 255 - image

def adjust_brightness(image, value=50):
    image = np.int16(image)
    image = image + value
    image = np.clip(image, 0, 255)
    return np.uint8(image)

def threshold_image(image, threshold_value=127):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    return binary

def main():
    image_path = 'image3.jpg'
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Image not loaded. Check the file path.")
        return
    
    compute_histogram(image)
    
    inverted = invert_image(image)
    brightened = adjust_brightness(image, 50)
    thresholded = threshold_image(image)
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Inverted Image", inverted)
    cv2.imshow("Brightness Adjusted", brightened)
    cv2.imshow("Thresholded Image", thresholded)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "_main_":
    main()