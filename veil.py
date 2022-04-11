# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:07:34 2020

@author: duminil

La fonction voile_estimation_3 estime le voile atmosphérique sur les trois 
canaux de couleurs

La fonction voile estimation mono estime le voile atmosphérique sur le canal 
d intensité le plus faible
"""
import cv2
import numpy as np
import function 
from preprocessing import open_filter
from scipy import ndimage, signal


def veil_estimation_rgb(fog, i_s, i0, win, eps, methode):  
    
    print("Atmospheric veil estimation ...")
    b,g,r = cv2.split(fog.astype("float"))      # split
    veil_rgb = np.zeros(fog.shape)
    
    for i in range(0, fog.shape[2]):
        # prevoile =
   
        veil_rgb[:,:,i] = function.modulation(open_filter(fog[:,:,i], win), 
                                              i_s[i], i0, eps, methode)
        
    return veil_rgb



def veil_estimation( fog, i_s, i0, win, eps, method):
    
    print("Atmospheric veil estimation ...")
    b,g,r = cv2.split(fog.astype("float"))      # split
    minChannel = cv2.min(b,g,r)
    i_s = np.mean(i_s)

    preveil = open_filter(minChannel, win)
    veil = function.modulation(preveil, i_s, i0, eps, method)

    veil = np.stack((veil,)*3, axis=-1)
    
    print("done")

    return veil