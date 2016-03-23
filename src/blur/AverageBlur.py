# coding: UTF-8
import Image
import numpy as np
import matplotlib.pyplot as plt

def plotImage(datas):
    fig = plt.figure()
    fig.add_subplot(111);
    plt.imshow(datas)
    plt.show()

def blur_process(filepath):
    im = Image.open("E:/TestDatas/ImageProcessing/test.png");
    im = np.array(im);
    
    size = np.shape(im);
    im = np.column_stack((np.zeros((size[0], 1, size[2])), im));
    im = np.column_stack((im, np.zeros((size[0], 1, size[2]))));
    im = np.row_stack((np.zeros((1, size[1] + 2, size[2])), im));
    im = np.row_stack((im, np.zeros((1, size[1] + 2, size[2]))));
    
#     plotImage(im[:,:,0]);
#     plotImage(im[:,:,1]);
#     plotImage(im[:,:,2]);
#     plotImage(im[:,:,3]);

blur_process("E:/TestDatas/ImageProcessing/test.png");

