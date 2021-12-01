import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
import pandas as pd
vid_list = glob("/home/data/jinyoung/Server/true/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]
vid_len = {}

#with open('./dict.pickle', 'rb') as fr:
#    data = pickle.load(fr)
#with open('./dict.txt', 'w') as f:
#    for value in sorted(data.keys()):
        #f.write(str(data[value]) + '\n')
#f.close()
#data.sort()
#print(sorted(data.keys()))
label = pd.read_csv('CADP_labeling.csv')
source = '/home/data/jinyoung/Server/CADP_Frames'
true_output = '/home/data/jinyoung/Server/True_Frames'
false_output = '/home/data/jinyoung/Server/False_Frames'
for i in label['Video_Name']:
    print('processing' + str(i))
    file_ = os.path.join(source + str('/%06d'%i))
    out_true = os.path.join(true_output + str('/%06d'%i))
    out_false = os.path.join(false_output + str('/%06d'%i))
    file_list = glob(os.path.join(file_, '*'))
    file_list.sort()
    
    ##################exception################
    if label['Impact_Frame'][i] == 'Not':
        print("Passing because of Not Accident") 
        continue
    if label['Impact_Frame'][i] == 'SV':
        print("Passing because of Same Video")
        continue

    ##################True################
    st = 0
    en = 0
    frame = 0
    false_en = 0
    partion = label['Partion'][i]
    if partion == False:
        impact = int(label['Impact_Frame'][i])
        overall = int(label['Overall_Length'][i])
        length = int(label['Length'][i])
        false_en = impact - 10
        if length > 60:
            st = impact
            en = impact + 61
            frame = 7
        elif length > 30: 
            frame = int ((length - 26) / 5)
            st = impact
            en = impact + 26 + (frame * 5)
        else:
            print("Too short True label")
        #print(st,en,frame)
    elif partion == True:
        impact = label['Impact_Frame'][i]
        
        overall = int(label['Overall_Length'][i])
        #length = int(label['Length'][i])
        #print(impact)
        st = int(impact.split(',')[0])
        false_en = st - 10
        en = int(impact.split(',')[1]) + 2
        length = en - st
        if length > 60:
            frame = 7
        elif length > 30: 
            frame = int ((length - 26) / 5)
        else:
            print("Too short True")
        
    print("True Labeling :", st, en, frame, overall)
    img_list = file_list[st:en]
    start = 0
    for k in range(frame):
        images = []
        pickle_file_name = true_output + '/' + str(i) + '_' + str(k) + '_' + 'true.pkl'
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

    ##################False################
    false_frame = 0
    false_length = false_en
    if false_length > 60:
        false_frame = 7
    elif false_length > 30:
        false_frame = int ((false_length - 26) / 5)
    else:
        print("too short false")
    false_st = false_en - 26 - (false_frame * 5)
    false_img_list = file_list[false_st:false_en]
    false_start = 0
    print("False Labeling :", false_st, false_en, false_st, false_frame)
    for q in range(false_frame):
        images = []
        pickle_file_name = false_output + '/' + str(i) + '_' + str(q) + '_' + 'false.pkl'
        pic = open(pickle_file_name, 'wb')
        false_small_img_list = false_img_list[false_start:false_start+31]
        for j in false_small_img_list:
            im = Image.open(j)
            not_im = np.array(im)
            images.append(not_im)
            #im.close()
        images = np.array(images)
        
        pickle.dump(images,pic)        
        pic.close()
        false_start += 5
        