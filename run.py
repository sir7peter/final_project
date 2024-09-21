"""
Created on Sat Nov 02 17:58:00 2023

@author: pedro

The following script should automatically process the text files (001.txt, 003.txt ...) from the
supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by
adding all the required fields, including the image associated with the fruit (image_name), and
uploading it to http://[external-IP-address]/fruits using the Python requests library.
"""
#!/usr/bin/env python3

import os
import json
import requests

def process_data(filename):
    list = []
    for item in os.listdir(filename):
        name, ext = os.path.splitext(item)
        #print(name)
        #print(ext)
        if item.endswith('.txt'):
            with open(filename + '\\' + item, 'rb') as file:
                lines = file.read().splitlines()
            # decode bytes into str
            lines = [line.decode() for line in lines ]
            # set the desired json structure
            struct = {'name': lines[0],
                      'weight': int(lines[1].replace(' lbs','')),
                      'description': lines[2],
                      'image_name': name+'.jpeg'}
            list.append(struct)
    return list

def json_file(data, filename):
    url = 'http://localhost/fruits/'
    with open(filename + '\\' + 'fruits_description.json', 'w') as item:
        '''file='''
        json.dump(data, item, indent= 2)
        response = requests.post(url, files={'file': file})
        if response.ok:
            print("uploaded data")
        else:
            print(f"error: {response.status_code}")

