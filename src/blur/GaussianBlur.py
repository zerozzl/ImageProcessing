import math
import numpy as np;
import Image
import matplotlib.pyplot as plt

def init_2d_gaussian_kernel(radius):
    theta = radius / 3.0;
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1));
    for i in range(2 * radius + 1):
        for j in range(2 * radius + 1):
            kernel[i, j] = round(np.exp(-(np.square(i - radius) + np.square(j - radius)) / (2 * np.square(theta))) / (2 * math.pi * np.square(theta)), 10);
    kernel = kernel / np.sum(kernel);
    return kernel;

def gaussian_blur_2d(filepath, radius):
    kernel = init_2d_gaussian_kernel(radius);
    
    im_src = Image.open(filepath);
    
    im = np.array(im_src);
    size_old = np.shape(im);
    im = np.column_stack((np.zeros((size_old[0], radius, size_old[2])), im));
    im = np.column_stack((im, np.zeros((size_old[0], radius, size_old[2]))));
    im = np.row_stack((np.zeros((radius, size_old[1] + 2 * radius, size_old[2])), im));
    im = np.row_stack((im, np.zeros((radius, size_old[1] + 2 * radius, size_old[2]))));
    
    size_new = np.shape(im);
    im_new = np.zeros(size_old);
    
    for k in range(size_old[2]):
        for i in range(radius, size_new[0] - radius, 1):
            for j in range(radius, size_new[1] - radius, 1):
                im_new[i - radius, j - radius, k] = np.sum(np.multiply(im[i - radius:i + radius + 1, j - radius:j + radius + 1, k], kernel)) / 255;
    
    fig = plt.figure();
    ax1 = fig.add_subplot(121);
    ax2 = fig.add_subplot(122);
    ax1.imshow(im_src);
    ax2.imshow(im_new);
    plt.show();


filepath = "E:/TestDatas/ImageProcessing/test2.png";
radius = 3;
gaussian_blur_2d(filepath, radius);
