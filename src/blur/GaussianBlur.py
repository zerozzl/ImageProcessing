import math
import numpy as np;

def init_2d_gaussian_kernel(radius):
    theta = radius / 3.0;
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1));
    for i in range(2 * radius + 1):
        for j in range(2 * radius + 1):
            kernel[i, j] = round(np.exp(-(np.square(i - radius) + np.square(j - radius)) / (2 * np.square(theta))) / (2 * math.pi * np.square(theta)), 10);
    kernel = kernel / np.sum(kernel);
    return kernel;

radius = 3;
init_2d_gaussian_kernel(radius);
