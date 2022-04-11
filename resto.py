# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:17:49 2020

@author: duminil

fog : input hazy image
sigma_s : paramètre spatial du filtre bilatéral
sigma_r : paramètre 2 du filtre bilatéral
win : taille de patch filtrage morphologique
"""


import numpy as np
import cv2
from function import is_estimation, i0_estimation
from veil import veil_estimation, veil_estimation_rgb
from bilateralfilter import bilateralfilter
from cv2 import ximgproc
# from gf import guided_filter, _gf_gray


VAR_IS = 1
VAR_I0 = 1

def mfp(fog, sigma_s, sigma_r, win, FLAGREFINE, VERSION, method):            
    
    # Is / I0 estimation-----------------------------------------------------
    b,g,r = cv2.split(fog)
    is_b = is_estimation(b, VAR_IS)
    is_g = is_estimation(g, VAR_IS)
    is_r = is_estimation(r, VAR_IS)
    i0 = i0_estimation(fog, VAR_I0)
    is_rgb = [is_b,is_g,is_r]
    
    # calcul epsilon
    N = np.min(is_rgb)
    min_eps = 0.05
    max_eps = 0.3
    min_is = 0.6
    max_is = 0.8
        
    if  N >= max_is:
        eps = max_eps
    elif N <= min_is:
        eps = min_eps
    else:    
        eps = (N*max_eps)/max_is   
    #-------------------------------------------------------------------------
    if VERSION == 1:
        # Calcul voile atmospherique : white fog
        veil = veil_estimation(fog, is_rgb , i0, win, eps, method)
    if VERSION == 2:
        # Calcul voile atmospherique : colored fog
        veil = veil_estimation_rgb(fog, is_rgb, i0, win, eps, method)

    
    print("Refinement process...")
    if FLAGREFINE == 1:
        veil = bilateralfilter(veil, fog, sigma_s, sigma_r)
    if FLAGREFINE == 2:
        veil = ximgproc.guidedFilter(np.float32(fog), np.float32(veil),
                                      sigma_s, sigma_r) 

    # Inversion Koschmieder
    veil = np.float64(veil)
    i0 = np.zeros(fog.shape)
    e = 0.001

    for i in range(0,3):
        # Contraintes pour empêcher les valeurs négatives
        veil[:,:,i] = cv2.min(cv2.min(veil[:,:,i],fog[:,:,i]),is_rgb[i])
        veil[:,:,i] = cv2.max ((veil[:,:,i])-e, 0)
 
        i0[:,:,i] = (fog[:,:,i] - veil[:,:,i])/(1-(veil[:,:,i]/is_rgb[i]))

    
    i0 = np.clip(i0,0,1)
    
    return i0



    

