# Single Image Atmospheric Veil Removal Using New Priors for Better Generectity

This is a single image dehazing method based on the Naka-Rushton function to treat fog presents near the horizon in real images and to generalize to different kinds of fog. 
This method achieve good performances and is competitive with deep learning methods. 

More details can be found here:

The conference paper : [Single Image Atmospheric Veil Removal Using New Priors](https://ieeexplore.ieee.org/document/9506244)
The journal article : [Single Image Atmospheric Veil Removal Using New Priors for Better Genericity](https://www.mdpi.com/2073-4433/12/6/772)

![Caption](/img/flowchart.png)

# Testing

Run main.py ; don't forget to change the indir and outdir paths to your own directories

# Results

![Caption](/img/qualitatif.png)

# Sources

This code uses a [python implementation of the Kaiming He's guided filter](https://github.com/swehrwein/python-guided-filter)
