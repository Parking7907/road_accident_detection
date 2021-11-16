from matplotlib import pyplot as plt
import json
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
import csv

#ffmpeg -ss [시작시간] -t [길이] -i [동영상이름] -r [프레임레이트] -s [출력해상도] -qscale:v 2 -an(오디오부분 제거) -f image2 [이미지이름]
'''
command = ("ffmpeg -ss 00:04:33 -t 25 -i ./preprocess/blackbox.mp4 -an -y -s 1280X720 -qscale:v 2 -f image2 preprocess/new_blackbox/%06d.jpg")
output = subprocess.call(command, shell=True, stdout=None)
command = ("cp -r preprocess/new_blackbox/ /home/jinyoung/share/sort/blackbox")
output = subprocess.call(command, shell=True, stdout=None)
'''
length = []
length_2 = []
length_3 = []

#Assault 대신 Date_Fight, Fight 존재

for file_name in glob("/hard1/pickle_data/True/Assault/*"):
    print(file_name)
    #loca = os.path.basename(file_name)
    for video_name in glob(file_name + '/*'):
        #print(video_name)
        for pkl_name in glob(video_name + '/*'):
            print(pkl_name)
            with open(pkl_name, 'rb') as f:
                data_pkl = pickle.load(f)
            length.append(len(data_pkl))
with open('True_assault_length.csv', 'w', newline='') as f:
    writer =csv.writer(f)
    writer.writerow(length)

print(len(length))



for file_name in glob("/hard1/pickle_data/True/Date_Fight/*"):
    print(file_name)
    #loca = os.path.basename(file_name)
    for video_name in glob(file_name + '/*'):
        #print(video_name)
        for pkl_name in glob(video_name + '/*'):
            print(pkl_name)
            with open(pkl_name, 'rb') as f:
                data_pkl = pickle.load(f)
            length_2.append(len(data_pkl))
with open('True_date_fight_length.csv', 'w', newline='') as f:
    writer =csv.writer(f)
    writer.writerow(length_2)

print(len(length_2))


for file_name in glob("/hard1/pickle_data/True/Fight/*"):
    print(file_name)
    #loca = os.path.basename(file_name)
    for video_name in glob(file_name + '/*'):
        #print(video_name)
        for pkl_name in glob(video_name + '/*'):
            print(pkl_name)
            with open(pkl_name, 'rb') as f:
                data_pkl = pickle.load(f)
            length_3.append(len(data_pkl))
with open('True_fight_length.csv', 'w', newline='') as f:
    writer =csv.writer(f)
    writer.writerow(length_3)

print(len(length_3))