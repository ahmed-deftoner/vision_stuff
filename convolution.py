import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# test filters
sharpen = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

blur = np.array([
    [0.0625, 0.125, 0.0625],
    [0.125,  0.25,  0.125],
    [0.0625, 0.125, 0.0625]
])

outline = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

def plot_image(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray')
    plt.show()

def plot_two_images(img1: np.array, img2: np.array):
    _, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(img1, cmap='gray')
    ax[1].imshow(img2, cmap='gray')
    plt.show()

def input_filter(matrix):
    R = int(input("Enter the dimension:"))
    print("Enter the entries rowwise:")
    for i in range(R):         
        a = []
        for j in range(R):      
            a.append(int(input()))
        matrix.append(a)
    return R

def print_filter(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()

def calculate_target_size(img_size: int, kernel_size: int) -> int:
    num_pixels = 0
 
    for i in range(img_size):
        added = i + kernel_size
        if added <= img_size:
            num_pixels += 1
            
    return num_pixels

def convolve(img: np.array, kernel: np.array) -> np.array:
    tgt_size = calculate_target_size(
        img_size=img.shape[0],
        kernel_size=kernel.shape[0]
    )
    k = kernel.shape[0]
    convolved_img = np.zeros(shape=(tgt_size, tgt_size))

    for i in range(tgt_size):
        for j in range(tgt_size):
            mat = img[i:i+k, j:j+k]
            convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
            
    return convolved_img

def main():
    matrix = []
    n = input_filter(matrix)
    print_filter(matrix, n)
    img = Image.open('C:\Users\Nadeem Nisar\Pictures')
    img = ImageOps.grayscale(img)
    img = img.resize(size=(224, 224))
    
    img_sharpened = convolve(img=np.array(img), kernel=matrix)
    plot_two_images(
        img1=img, 
        img2=img_sharpened
    )

main()