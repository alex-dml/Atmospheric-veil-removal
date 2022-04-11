# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:42:39 2020

@author: duminil
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_Imax(img, winsize):
    h = np.size(img,0)
    w = np.size(img,1)
    
    Imax = np.zeros((h,w))

    k=0
    for i in range(0, w):
        for j in range(0, h):
            
            patch = img[j : j + ((winsize[0]*2)-1), k : k + ((winsize[1]*2)-1)]
            Imax[j,i] = np.max(patch)
    
        k=i+1
    
    return Imax 
#
def get_Imin(img, winsize):
    
    h = np.size(img,0)
    w = np.size(img,1)
    
    Imin = np.zeros((h,w))

    k=0
    for i in range(0, w):
        for j in range(0, h):
            
            patch = img[j : j + (winsize[0]-1), k : k + (winsize[0]-1)]
            Imin[j,i] = np.min(patch)
    
        k=i+1
    
    return Imin

def get_darkChannel (minC, winsize):

    
    dark_channel = np.zeros((np.size(minC,0),np.size(minC,1)))
    
    k=0
    # dark channel prior
    for i in range(0,np.size(minC,1)):
        for j in range(0,np.size(minC,0)):
    
            patch = minC[j : j + (winsize[0]-1), k : k + (winsize[1]-1)]
            dark_channel[j,i] = np.min(patch)
    
        k=i+1
        
    return dark_channel


    
def affichage_plt(fog):
    fog = np.float32(fog)
    plt.axis('off')
    plt.imshow(cv2.cvtColor(fog, cv2.COLOR_BGR2RGB))
    plt.show()