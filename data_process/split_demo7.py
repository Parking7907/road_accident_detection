import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
true = glob("/home/data/jinyoung/Server/True_Frames/*")
true_loc = "/home/data/jinyoung/Server/True_Frames/"
false = glob("/home/data/jinyoung/Server/False_Frames/*")
false_loc = "/home/data/jinyoung/Server/False_Frames/"
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]
true.sort()
false.sort()
true_video_list = []
false_video_list = []
for name in true:
    vid_ = os.path.basename(name)
    vid_ = vid_.split('_')[0]# + vid_.split('_')[2]
    #video_n[i] = vid_
    if vid_ not in true_video_list:
        true_video_list.append(vid_)
        #GT_dict[vid_] = int(labels[i])

for name in false:
    vid_ = os.path.basename(name)
    vid_ = vid_.split('_')[0]# + vid_.split('_')[2]
    #video_n[i] = vid_
    if vid_ not in false_video_list:
        false_video_list.append(vid_)
        #GT_dict[vid_] = int(labels[i])

Both = [i for i in true_video_list if i in false_video_list]

T_F = list(set(true_video_list) - set(false_video_list))
F_T = list(set(false_video_list) - set(true_video_list))
#len D = 862, F_T = 33, T_F = 356 overall 1245
for p in true:
    for k in T_F:
        if p.startswith(true_loc + k + '_'):
            print(p)
for q in false:
    for l in F_T:
        if q.startswith(false_loc + l + '_'):
            print(q)
#pdb.set_trace()

true_len = len(true_video_list)
false_len = len(false_video_list)
test_len_TF = int(len(T_F) * 0.2)
test_len_FT = int(len(F_T) * 0.2)
test_len = int(len(Both) * 0.2)

print("Train len : ", len(Both)-test_len)
print("Test len :", test_len)
print("T_F len Train/Test : ",len(T_F)-test_len_TF, test_len_TF)
print("F_T len Train/Test : ",len(F_T)-test_len_FT, test_len_FT)
for i,vid_n in enumerate(Both):
    if i < test_len:
        print("Both_test :", vid_n)
        for k in true:
            if k.startswith(true_loc + vid_n + '_'):
                #print("Test True : ",true_loc + vid_n )
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Test/True/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
        
        for l in false:
            if l.startswith(false_loc + vid_n + '_'):
                #print("Test False :", false_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Test/False/"%(l))
                output = subprocess.call(command, shell=True, stdout=None)
    else:
        print("Both_train :", vid_n)
        for k in true:
            if k.startswith(true_loc + vid_n + '_'):
                #print("Train True :", true_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Train/True/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
        
        for l in false:
            if l.startswith(false_loc + vid_n + '_'):
                #print("Train False:", false_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Train/False/"%(l))
                output = subprocess.call(command, shell=True, stdout=None)
print("T_F STARTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i,vid_n in enumerate(T_F):
    if i < test_len_TF:
        print("T_F_test", vid_n)
        for k in true:
            if k.startswith(true_loc + vid_n + '_'):
                #print("Train True :", true_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Test/True/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
    else:
        print("T_F_train", vid_n)        
        for k in true:
            if k.startswith(true_loc + vid_n + '_'):
                #print("Train True :", true_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Train/True/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
    
print("F_T STARTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i,vid_n in enumerate(F_T):
    print("F_T", vid_n)
    if i < test_len_FT:
        for k in false:
            if k.startswith(false_loc + vid_n + '_'):
                #print("Train False :", false_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Test/False/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
    else:
        for k in false:
            if k.startswith(false_loc + vid_n + '_'):
                #print("Train False :", false_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo7/Train/False/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)

