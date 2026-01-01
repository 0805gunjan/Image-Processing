import cv2
import numpy as np

def load_and_resize(image_path, size=(400, 400)):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image at {image_path}")
    return cv2.resize(image, size)

def perform_operations(image1, image2):
    # Arithmetic operations
    add_img = cv2.add(image1, image2)
    sub_img = cv2.subtract(image1, image2)
    mul_img = cv2.multiply(image1, image2)
    div_img = cv2.divide(image1, image2)
    
    # Bitwise operations
    bitwise_and = cv2.bitwise_and(image1, image2)
    bitwise_or = cv2.bitwise_or(image1, image2)
    bitwise_xor = cv2.bitwise_xor(image1, image2)
    bitwise_not1 = cv2.bitwise_not(image1)
    bitwise_not2 = cv2.bitwise_not(image2)
    
    return {
        'Addition': add_img,
        'Subtraction': sub_img,
        'Multiplication': mul_img,
        'Division': div_img,
        'Bitwise AND': bitwise_and,
        'Bitwise OR': bitwise_or,
        'Bitwise XOR': bitwise_xor,
        'Bitwise NOT (Image 1)': bitwise_not1,
        'Bitwise NOT (Image 2)': bitwise_not2
    }

def display_images(images_dict):
    for name, img in images_dict.items():
        cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image1_path = "image1.jpg"  # Change to actual image path
    image2_path = "image2.jpg"  # Change to actual image path
    
    try:
        img1 = load_and_resize(image1_path)
        img2 = load_and_resize(image2_path)
        results = perform_operations(img1, img2)
        display_images(results)
    except ValueError as e:
        print(e)
