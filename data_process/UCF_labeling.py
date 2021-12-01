import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
import pandas as pd
label = pd.read_csv('UCF_labeling.csv')
source = '/home/data/jinyoung/Server/frame_data/UCF_Frames/road/'
true_output = '/home/data/jinyoung/Server/UCF_True'
false_output = '/home/data/jinyoung/Server/UCF_False'
#pdb.set_trace()
for i in label['Video_Name']:
    name = i + '_x264'
    print(name)
    if int(i[-3:]) < 45 :
        i = int(i[-3:]) - 1 
    else:
        i = int(i[-3:]) - 2
    print('processing' + str(i))
    file_ = os.path.join(source + name)
    out_true = os.path.join(true_output + name)
    out_false = os.path.join(false_output + name)
    #os.makedirs(out_true,exist_ok=True)
    #os.makedirs(out_false,exist_ok=True)
    file_list = glob(os.path.join(file_, '*'))
    file_list.sort()
    #print(file_list)
    #print(file_, out_true, out_false)
    
    st = 0
    en = 0
    frame = 0
    false_en = 0
    partion = label['Partion'][i]
    if label['Impact_Frame'][i] == 'Not':
        print("Passing because of Not Accident") 
        continue
    if label['Impact_Frame'][i] == 'SV':
        print("Passing because of Same Video")
        continue
    if partion == False:
        impact = int(label['Impact_Frame'][i])
        overall = int(label['Overall_Length'][i])
        length = int(label['Length'][i])
        false_en = impact - 10
        if length > 60:
            st = impact
            en = impact + 61
            frame = 4
        elif length > 50:
            st = impact
            en = impact + 51
            frame = 3
        elif length > 40:
            st = impact
            en = impact + 41
            frame = 2
        elif length > 30:
            st = impact
            en = impact + 31
            frame = 1
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
            frame = 4
        elif length > 50: 
            frame = 3
        elif length > 40:
            frame = 2
        elif length > 30:
            frame = 1
        #print(st,en,frame)
    #print(false_en)
    print("True Labeling :", st, en, frame, overall)
    img_list = file_list[st:en]
    start = 0
    for k in range(frame):
        images = []
        pickle_file_name = true_output + '/' + name + '_' + str(k) + '_' + 'true.pkl'
        #print(pickle_file_name)
        pic = open(pickle_file_name, 'wb')
        small_img_list = img_list[start:start+31]
        for j in small_img_list:
            im = Image.open(j)
            not_im = np.array(im)
            images.append(not_im)
            #im.close()
        images = np.array(images)    
        pickle.dump(images,pic)        
        pic.close()
        start += 10
    false_frame = 0
    #print(false_en)
    false_en = false_en - 20
    for p in range(8):
        if false_en > 10:
            false_frame += 1
            false_en = false_en - 10
    false_img_list = file_list[false_en:false_en+21+10*false_frame]
    false_start = 0
    #if false_en < -30:
    #    pdb.set_trace()
    #
    print("False Labeling :", false_en, false_frame)
    for q in range(false_frame):
        images = []
        pickle_file_name = false_output + '/' + name + '_' + str(q) + '_' + 'false.pkl'
        #print(pickle_file_name)
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
        false_start += 10
    #print(images.shape)
    
        