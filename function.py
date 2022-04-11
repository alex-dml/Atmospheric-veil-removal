# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:09:59 2020

@author: duminil
"""
import numpy as np
from preprocessing import open_filter, close_filter, min_filter, max_filter
import cv2

SIZE = (10,10)

def is_estimation(fog, var):
   
   if var == 0:
       #print("is : max method")
       return np.max(fog)
   
   elif var == 1:
       #print("is : max mf method")
       return np.max(open_filter(fog, SIZE))
   
   elif var == 2:
       #print("is : max minf method")
       return np.max(min_filter(fog, SIZE))
   
   elif var == 3:
       #print("is : percentile method")
       return np.percentile(fog, 98)
   else:
       #print("is :max de minf method")
       return np.max(fog)
   
def i0_estimation(fog, var):
    
   if var == 0:
       #print("i0 : min method")
       return np.min(fog) 
   
   elif var == 1:
       #print("i0 : min mf method")
       return np.min(close_filter(fog,SIZE))
   
   elif var == 2:
       #print("i0 : min maxf method")
       return np.min(max_filter(fog, SIZE))
   
   elif var == 3:
       #print("i0 : percentile method")
       return np.percentile(fog,2)
   
   else:
       #print("i0 : min method")
       return np.min(fog)
   
def modulation(channel, i_s, i0, eps, method):
        
    # Naka-Rushton parameters
    a = (i_s-eps)/(i_s-(i0))
    f0 = 2*(i_s-eps)
    n = (2*a*i_s)/(i_s-eps)
    k = i_s
    nr = (f0*pow(channel,n)) / (pow(channel,n) + pow(k,n)) 

    x = channel
    f = (x-i0)/(1-i0)
    
    # constante
    g = i0 * np.ones((np.size(channel,0), np.size(channel,1)))
    
    # interpolations
    p = 2
    m = 0.3
    
    if method == 'NR':
        return nr
    elif method == 'interp_NR':
        return cv2.min(x,cv2.max(0,pow(i0,p)*i0+pow((m-i0),p)*nr)/(pow(i0,p) + pow((m-i0),p) ))

        