import cv2
import ffmpy
import glob
import json
import numpy as np
import os
import shutil
import wget

if os.path.exists('/home/tadhg/Documents/web_data/Workspace/'):
    shutil.rmtree('/home/tadhg/Documents/web_data/Workspace/')

if not os.path.exists('/home/tadhg/Documents/web_data/Workspace/'):
    os.makedirs('/home/tadhg/Documents/web_data/Workspace/')

base_url="https://services.swpc.noaa.gov"

json_url='/products/animations/enlil.json'
file=wget.download(base_url+json_url, '/home/tadhg/Documents/web_data/enlil.json')

if os.path.exists('/home/tadhg/Documents/web_data/enlil.json'):
    shutil.move(file,'/home/tadhg/Documents/web_data/enlil.json')

with open('/home/tadhg/Documents/web_data/enlil.json') as json_file:
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

ff=ffmpy.FFmpeg(inputs={'/var/www/html/SWmonitor/data/mp4s/Enlil_forecast_mpeg4.mp4':['-y']},outputs={'/var/www/html/SWmonitor/data/mp4s/Enlil_forecast_h264.mp4': ['-y']})

ff.run()


file=wget.download("https://data.magie.ie/magnetometer_live/arm_kindex.png", "/var/www/html/SWmonitor/data/pngs/magie/arm_kindex.png")

if os.path.exists("/var/www/html/SWmonitor/data/pngs/magie/arm_kindex.png"):
    shutil.move(file,"/var/www/html/SWmonitor/data/pngs/magie/arm_kindex.png")



file=wget.download("https://data.magie.ie/magnetometer_live/val_kindex.png", "/var/www/html/SWmonitor/data/pngs/magie/val_kindex.png")

if os.path.exists("/var/www/html/SWmonitor/data/pngs/magie/val_kindex.png"):
    shutil.move(file,"/var/www/html/SWmonitor/data/pngs/magie/val_kindex.png")



file=wget.download("https://data.magie.ie/magnetometer_live/Aurora_forecast_3day.mp4", "/var/www/html/SWmonitor/data/mp4s/Aurora_forecast_3day.mp4")

if os.path.exists("/var/www/html/SWmonitor/data/mp4s/Aurora_forecast_3day.mp4"):
    shutil.move(file,"/var/www/html/SWmonitor/data/mp4s/Aurora_forecast_3day.mp4")



file=wget.download("https://solarmonitor.org/data/latest_images/saia_00193_fd.png", "/var/www/html/SWmonitor/data/pngs/AIA/saia_00193_fd.png")

if os.path.exists("/var/www/html/SWmonitor/data/pngs/AIA/saia_00193_fd.png"):
    shutil.move(file,"/var/www/html/SWmonitor/data/pngs/AIA/saia_00193_fd.png")
