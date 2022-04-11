# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:09:34 2020

@author: alxdn
"""
import numpy as np
import cv2

def open_filter(channel, size):
    
    kernel = np.ones(size, np.uint8)
    pv = cv2.morphologyEx(channel, cv2.MORPH_OPEN, kernel)
    
    return pv

def close_filter(channel, size):
    
    kernel = np.ones(size, np.uint8)
    pv = cv2.morphologyEx(channel, cv2.MORPH_CLOSE, kernel)
    
    return pv


def min_filter(channel, size):
    
    # Creating kernel 
    kernel = np.ones(size, np.uint8) 
    # Using cv2.erode() method  
    pv = cv2.erode(channel, kernel)  
    
    return pv

def max_filter(channel, size):
    
    # Creating kernel 
    kernel = np.ones(size, np.uint8) 
    # Using cv2.erode() method  
    pv = cv2.dilate(channel, kernel)  
    
    return pv

def white_balance(img):
    
    #img = np.float32(img)
    result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.3)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.3)
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    
    return result