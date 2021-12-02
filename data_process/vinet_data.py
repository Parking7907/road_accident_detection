import cv2
import numpy as np
import glob
import os
import pdb
import pandas as pd
import subprocess
img_array = []
img_array_2 = []
#size = (1280, 720)
frame_rate = 30
dir1 = "/home/data/jinyoung/Server/accident_data_saliency/"
dir2 = "/home/data/jinyoung/Server/accident_data_saliency2/"
video_list = glob.glob('/home/data/jinyoung/Server/accident_data_frame_ViNet/*')
video_list.sort()
label = pd.read_csv('/home/data/jinyoung/Server/CADP_labeling.csv')
#pdb.set_trace()
for video_name in video_list:
    dataname = os.path.join(video_name, "images")
    print(dataname)
    os.makedirs(dataname, exist_ok=True)
    #print("mv {0}/*.jpg {1}".format(video_name, dataname))
    command = ("mv {0}/*.jpg {1}".format(video_name, dataname)) # -s 224x224
    output = subprocess.call(command, shell=True, stdout=None)