import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
import pandas as pd

test_vid_list = glob("/home/data/jinyoung/Server/frame_data/UCF_Frames/Testing_Normal_Frames/*")
test_source = '/home/data/jinyoung/Server/frame_data/UCF_Frames/Testing_Normal_Frames/'
test_output = '/home/data/jinyoung/Server/UCF_short_test'
train_vid_list = glob("/home/data/jinyoung/Server/frame_data/UCF_Frames/Training_Normal_Frames/*")
train_source = '/home/data/jinyoung/Server/frame_data/UCF_Frames/Training_Normal_Frames/'
train_output = '/home/data/jinyoung/Server/UCF_short'
'''
for video in test_vid_list:
    frame = 7
    vid_folder = os.path.basename(video)
    file_list = glob(os.path.join(video, '*'))
    file_list.sort()
    print(vid_folder)
    img_list = file_list[0:61]
    #pdb.set_trace()
    start = 0
    for k in range(frame):
        images = []
        pickle_file_name = test_output + '/' + vid_folder + '_' + str(k) + '_' + 'false.pkl'
        #print(pickle_file_name)
        pic = open(pickle_file_name, 'wb')
        small_img_list = img_list[start:start+31]
        for j in small_img_list:
            im = Image.open(j)
            not_im = np.array(im)
            images.append(not_im)
        images = np.array(images)    
        pickle.dump(images,pic)        
        pic.close()
        start += 5
'''
for video in train_vid_list:
    frame = 7
    vid_folder = os.path.basename(video)
    file_list = glob(os.path.join(video, '*'))
    file_list.sort()
    print(vid_folder)
    img_list = file_list[0:61]
    start = 0
    #pdb.set_trace()
    for k in range(frame):
        images = []
        pickle_file_name = train_output + '/' + vid_folder + '_' + str(k) + '_' + 'false.pkl'
        pic = open(pickle_file_name, 'wb')
        small_img_list = img_list[start:start+31]
        for j in small_img_list:
            im = Image.open(j)
            not_im = np.array(im)
            images.append(not_im)
        images = np.array(images)    
        pickle.dump(images,pic)        
        pic.close()
        start += 5
