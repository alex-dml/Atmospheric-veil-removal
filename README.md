# Single Image Atmospheric Veil Removal Using New Priors for Better Generectity

This is a single image dehazing method based on the Naka-Rushton function to treat fog presents near the horizon in real images and to generalize to different kinds of fog. 
This method achieve good performances and is competitive with deep learning methods. 

Publications to be referred when using the previous code :

@article{duminil2021single,
  title={Single image atmospheric veil removal using new priors for better genericity},
  author={Duminil, Alexandra and Tarel, Jean-Philippe and Br{\'e}mond, Roland},
  journal={Atmosphere},
  volume={12},
  number={6},
  pages={772},
  year={2021},
  publisher={MDPI}
}


@inproceedings{duminil2021single,
  title={Single image atmospheric veil removal using new priors},
  author={Duminil, Alexandra and Tarel, Jean-Philippe and Br{\'e}mond, Roland},
  booktitle={2021 IEEE International Conference on Image Processing (ICIP)},
  pages={1719--1723},
  year={2021},
  organization={IEEE}
}


[http://perso.lcpc.fr/tarel.jean-philippe/publis/ja21.html](http://perso.lcpc.fr/tarel.jean-philippe/publis/ja21.html)


[http://perso.lcpc.fr/tarel.jean-philippe/publis/icip21.html](http://perso.lcpc.fr/tarel.jean-philippe/publis/icip21.html)


![Caption](/img/flowchart.png)

# Testing

- Run main.py 
- Don't forget to change the indir and outdir paths to your own directories.
- *mfp* function used the default parameters of the paper. Please adjust the parameters to your own images.

# Results

![Caption](/img/qualitatif.png)

# Sources

This code uses a [python implementation of the Kaiming He's guided filter](https://github.com/swehrwein/python-guided-filter)
