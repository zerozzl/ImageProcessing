# coding: UTF-8
import Image
import numpy as np
import matplotlib.pyplot as plt

def plotImage(datas):
    fig = plt.figure()
    fig.add_subplot(111);
    plt.imshow(datas)
    plt.show()

def blur_process(filepath, radius):
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
                im_new[i - radius, j - radius, k] = ((np.sum(im[i - radius:i + radius + 1, j - radius:j + radius + 1, k]) - im[i, j, k]) / (np.square(radius * 2 + 1) - 1)) / 255;
    
    fig = plt.figure()
    ax1 = fig.add_subplot(121);
    ax2 = fig.add_subplot(122)
    ax1.imshow(im_src)
    ax2.imshow(im_new)
    plt.show()


filepath = "E:/TestDatas/ImageProcessing/test1.png";
radius = 5;
blur_process(filepath, radius);

