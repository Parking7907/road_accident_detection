import cv2
import numpy as np
import glob
import os
 
img_array = []
#size = (1280, 720)
frame_rate = 10
videoname = '/home/jinyoung/revisiting-sepconv/videos/30fps'
name = os.path.basename(videoname)
list_ = []
for filelist in glob.glob(videoname + '/*.jpg'):
    list_.append(filelist)
list_.sort()
for filename in list_:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    
new_videoname = videoname.split('/')[-1]
print(new_videoname)
out = cv2.VideoWriter('./result/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()