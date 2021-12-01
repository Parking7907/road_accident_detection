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
    #os.makedirs(out_true,exist_ok=True)
    #os.makedirs(out_false,exist_ok=True)
    file_list = glob(os.path.join(file_, '*'))
    file_list.sort()
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
        if length > 30:
            st = impact
        else:
            print("Too short True label")
        img_list = file_list[st:]
    elif partion == True:
        impact = label['Impact_Frame'][i]
        overall = int(label['Overall_Length'][i])
        #length = int(label['Length'][i])
        #print(impact)
        st = int(impact.split(',')[0])
        en = int(impact.split(',')[1]) + 2
        img_list = file_list[st:en]

    print("True Labeling :", st)
    if st > 0:
        images = []
        pickle_file_name = true_output + '/' + str(i) + '_'  + 'true.pkl'
        pic = open(pickle_file_name, 'wb')
        #small_img_list = img_list[start:start+31]
        for j in img_list:
            im = Image.open(j)
            not_im = np.array(im)
            images.append(not_im)
            #im.close()
        images = np.array(images)    
        pickle.dump(images,pic)
        pic.close()