import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def plot_image(img: np.array):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray');

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

def main():
    matrix = []
    n = input_filter(matrix)
    print_filter(matrix, n)

main()