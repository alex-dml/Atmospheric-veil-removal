import cv2
import resto
import glob, os
import argparse
from evaluations import ssim_psnr


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", default = "E:/Datasets/RESIDE/SOTS/SOTS/outdoor/")
    parser.add_argument("--outdir", default = "D:/1-These/4-Images/optim/")
    parser.add_argument("--method", default = "interp_NR", help = "NR or interp_NR")
                        
    parser.add_argument("--flagrefine", default = 2, help = "bilateral filter: 1 \
                        | guided filter: 2")
                        
    parser.add_argument("--version", default = 2, help = "white fog (daytime): 1 | colored fog (nighttime) : 2")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    tot_ssim = 0
    tot_psnr = 0
    
    file = glob.glob(args.indir + 'hazy/*.jpg')
    for x in file:
        
        fog = cv2.imread(x)/255
    
        res = resto.mfp(fog, 90, 0.05, (10,10), args.flagrefine, args.version, args.method)
        
        # save results
        # cv2.imwrite(args.outdir + str(i) +'.png', res*255)
        
        # evaluation
        path_gt = args.indir + 'gt/' + os.path.basename(x).rsplit('_')[0] + '.png'
        gt = cv2.imread(path_gt)/255
        ssim, psnr = ssim_psnr(gt, res)
        
        tot_ssim += ssim
        tot_psnr += psnr
        
        # display
        # cv2.imshow('res', res)
        # cv2.waitKey(0)
        
    print("ssim", "{0:.2f}".format(tot_ssim/len(file)), "psnr", "{0:.2f}".format(tot_psnr/len(file)))


if __name__ == "__main__":
    main()

