import cv2

import numpy as np 

import matplotlib.pyplot as plt

def display_image(title, image):

    plt.figure(figsize=(8, 8))

    if len(image.shape) == 2:

        plt.imshow(image, cmap='gray')

    else:

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)

    plt.axis('off')

    plt.show()

def apply_edge_detection(image, method='sobel', ksize=3, threshold1=100, threshold2=200):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "sobel":

        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)       
        return cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
    
    elif method == "canny":

        return cv2.Canny(gray_image, threshold1, threshold2)
    

    elif method == "Laplacian":

        return cv2.Laplacian(gray_image, cv2.CV_64F).astype(np.uint8)
    
def apply_filter(image, filter_type="gaussian", ksize=5):

        if filter_type == "gaussian":

            return cv2.GaussianBlur(image, (ksize, ksize), 0)
        
        elif filter_type == "median":

            return cv2.medianBlur(image, ksize)
        
def interactive_edge_detection(image_path):

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            edges = apply_edge_detection(image, method='sobel')
            display_image("Sobel Edge Detection", edges)

        elif choice == '2':
            edges = apply_edge_detection(image, method='canny')
            display_image("Canny Edge Detection", edges)

        elif choice == '3':
            edges = apply_edge_detection(image, method='Laplacian')
            display_image("Laplacian Edge Detection", edges)

        elif choice == '4':
            smoothed = apply_filter(image, filter_type="gaussian")
            display_image("Gaussian Smoothing", smoothed)

        elif choice == '5':
            smoothed = apply_filter(image, filter_type="median")
            display_image("Median Filtering", smoothed)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    interactive_edge_detection(image_path)

    