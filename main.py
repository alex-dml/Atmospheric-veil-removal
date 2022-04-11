# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:15:52 2020

@author: duminil
"""

import cv2
import resto
import glob
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", default = "E:/Datasets/RESIDE/SOTS/SOTS/outdoor/hazy/*")
    parser.add_argument("--outdir", default = "D:/1-These/4-Images/optim/")
    parser.add_argument("--method", default = "interp_NR", help = "NR or interp_NR")
                        
    parser.add_argument("--flagrefine", default = 2, help = "bilateral filter: 1 \
                        | guided filter: 2")
                        
    parser.add_argument("--version", default = 2, help = "white fog (daytime): 1 | colored fog (nighttime) : 2")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    i = 0
    for x in glob.glob(args.indir):
        
        fog = cv2.imread(x)/255
    
        res = resto.mfp(fog, 90, 0.05, (10,10), args.flagrefine, args.version, args.method)
        
        
        # save results
        # cv2.imwrite(args.outdir + str(i) +'.png', res*255)
        
        # display
        cv2.imshow('res', res)
        cv2.waitKey(0)


if __name__ == "__main__":
    main()

