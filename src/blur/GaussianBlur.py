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
    
    return im_new;

def init_1d_gaussian_kernel(radius):
    theta = radius / 3.0;
    kernel = np.zeros(2 * radius + 1);
    for i in range(2 * radius + 1):
        kernel[i] = round(np.exp(-np.square(i - radius) / (2 * np.square(theta))) / (theta * np.sqrt(2 * math.pi)), 10);
    kernel = kernel / np.sum(kernel);
    return kernel;

def gaussian_blur_1d(filepath, radius):
    kernel = init_1d_gaussian_kernel(radius);
    
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
                im_new[i - radius, j - radius, k] = (np.sum(np.multiply(im[i - radius:i + radius + 1, j, k], kernel)) / 255 + np.sum(np.multiply(im[i, j - radius:j + radius + 1, k], kernel)) / 255) / 2;
    
    return im_new;

def gaussian_blur(filepath, radius):
    im_src = Image.open(filepath);
    im_2d = gaussian_blur_2d(filepath, radius);
    im_1d = gaussian_blur_1d(filepath, radius);
    
    fig = plt.figure();
    ax1 = fig.add_subplot(131);
    ax2 = fig.add_subplot(132);
    ax3 = fig.add_subplot(133);
    ax1.imshow(im_src);
    ax2.imshow(im_2d);
    ax3.imshow(im_1d);
    plt.show();
    

filepath = "E:/TestDatas/ImageProcessing/test1.png";
radius = 12;
gaussian_blur(filepath, radius);
