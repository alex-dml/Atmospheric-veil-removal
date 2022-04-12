@author: duminil
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from scipy import ndimage as ndi
from skimage import feature
import math
import utils 
import glob
import os

def ssimpsnr_eval(orig, foggy):
    ssim_ = ssim(orig, foggy, data_range=orig.max() - orig.min(), multichannel=True)
    
    label = 'PSNR: {:.2f}, SSIM: {:.2f}'

    foggy = np.float32(foggy)
    orig = np.float32(orig)
    
    psnr_ = psnr(orig, foggy)
    
    return ssim_, psnr_

def MSE_pondere(f,g, poids):
    mse = 0
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            
            mse = mse + np.abs(f[i,j]-poids*g[i,j])**2
    
    
    mse = (1/(f.shape[0]*f.shape[1])*poids)*mse
    
    return mse

def psnr_pondere(f,g):
    
    return round(10*np.log(255**2/MSE_pondere(f,g)))


def grad_psnr(orig, res):
    
    orig = np.float32(orig)
    res = np.float32(res)
    orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    
    gradV = np.array([-1,1], ndmin = 2).T
    gradH = np.array([-1,1])
    
    orig_gradV = cv2.filter2D(orig, cv2.CV_32F, gradV)
    orig_gradH = cv2.filter2D(orig, cv2.CV_32F, gradH)
    
    res_gradV = cv2.filter2D(res, cv2.CV_32F, gradV)
    res_gradH = cv2.filter2D(res, cv2.CV_32F, gradH)
    
    cv2.imshow('Frame', res_gradH)
    cv2.waitKey(0)
    cv2.imwrite("D:/1-These/eval_img/res_gradH.png", res*255)
    
    return psnr(orig_gradH, res_gradH)
    
def canny_eval(frame, minVal, maxVal):
    frame = np.uint8(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # # Smoothing without removing edges.
    #gray = cv2.bilateralFilter(gray, 3, 10, 10)
    
    # Applying the canny filter
    edges = cv2.Canny(gray, minVal, maxVal, apertureSize =3, L2gradient=False)
    #edges_filtered = cv2.Canny(gray, minVal, maxVal)
    
    # Stacking the images to print them together for comparison
    #images = np.hstack((gray, edges, edges_filtered))
    
    # Display the resulting frame

    return edges

def positive_rate(edges1, edges2):
    
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    
    for i in range(edges1.shape[0]):
        for j in range(edges1.shape[1]):
            if edges2[i,j] == 255:
                if edges1[i,j] == 255:
                    TP = TP + 1
                else:
                    FP = FP + 1
            else:
                if edges1[i,j] == 0:
                    TN = TN + 1
                else:
                    FN = FN + 1
                
    ACC = (TP+TN)/(TP+FP+FN+TN)
    
    #print("acc",ACC)
    # t_TP = TP/np.count_nonzero(edges1 == 255)
    # t_FP = FP/np.count_nonzero(edges1 == 255)
    
    return TP, FP, FN, TN
