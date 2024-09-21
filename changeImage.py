"""
Created on Sat Nov 02 15:27:00 2023

@author: pedro

The following script should iterate over a set of .TIFF images and change them to .JPEG;
besides the resolution of the images should go from 3000x2000 to 600x400 pixel
""" 
#!/usr/bin/env python3

import os.path
from PIL import Image

def converter(filename):
    for image in os.listdir(filename):
        #print(image)
        name, ext = os.path.splitext(image)
        if image.endswith('.tiff'):
            im = Image.open(filename + '\\'+ image)
            print("open image")
            new_im = im.resize(size= (600,400))
            print("resize")
            name+='.jpeg'
            new_im.convert("RGB").save(filename+ '\\' + name,"JPEG")
            print("converting  1st RGB and 2nd JPEG")
            im.close() 