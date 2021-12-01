import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
vid_list = glob("/home/data/jinyoung/Server/true/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]
vid_len = {}

with open('./dict.pickle', 'rb') as fr:
    data = pickle.load(fr)
print(data)
vid_long = []
vid_short = []
for i in vid_list:
    if data[i]> 400:
        vid_long.append(i)
    else:
        vid_short.append(i)
'''

print("Long len :" + str(len(vid_long)))
for vid_n in vid_long:
    command = ("cp %s /home/data/jinyoung/Server/long/"%(vid_n))
    output = subprocess.call(command, shell=True, stdout=None)
''' 
test_len = int(0.2*len(vid_short))
print("Test len :" + str(test_len))
print("Train len :" + str(len(vid_short)-test_len))
for i, vid_name in enumerate(vid_short):
    if i < test_len:
        command = ("cp %s /home/data/jinyoung/Server/UCF_test/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
    
    else:
        command = ("cp %s /home/data/jinyoung/Server/UCF_exp/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
