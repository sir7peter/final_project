"""
Created on Sat Nov 02 17:35:00 2023

@author: pedro

The following script should take the JPEG files created from the changeImage.py script
and uploads them to a web server fruit catalog - in this case we will only test the connection
"""
#!/usr/bin/env python3

import requests
import os.path


url = "http://localhost/upload/"

def upload(filename, url):
    for image in os.listdir(filename):
        name, ext = os.path.splitext(image)
        if ext == '.jpeg':
            with open(image, 'rb') as opened:
                requests.post(url, files={'file': opened})