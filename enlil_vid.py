import cv2
import ffmpy
import glob
import json
import numpy as np
import os
import shutil
import wget

base_url="https://services.swpc.noaa.gov"

json_url='/products/animations/enlil.json'
file=wget.download(base_url+json_url, '/home/tadhg/Documents/web_data/enlil.json')

if os.path.exists('/home/tadhg/Documents/web_data/enlil.json'):
    shutil.move(file,'/home/tadhg/Documents/web_data/enlil.json')

with open('enlil.json') as json_file:
    dat = json.load(json_file)

for p in range(len(dat)):
    wget.download(base_url+dat[p]['url'],'/home/tadhg/Documents/web_data/Workspace/')

img_array = []
files=glob.glob('/home/tadhg/Documents/web_data/Workspace/*.jpg')
files.sort()
for filename in files:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('/var/www/html/SWmonitor/data/mp4s/Enlil_forecast_mpeg4.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 12, size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()

ff=ffmpy.FFmpeg(inputs={'/var/www/html/SWmonitor/data/mp4s/Enlil_forecast_mpeg4.mp4':None},outputs={'/var/www/html/SWmonitor/data/mp4s/Enlil_forecast_h264.mp4': ['-y']})

ff.run()
