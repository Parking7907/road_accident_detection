import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
true = glob("/home/data/jinyoung/Server/Demo4/Original/Train/True/*")
true_loc = "/home/data/jinyoung/Server/Demo4/Original/Train/True/"
false = glob("/home/data/jinyoung/Server/Demo4/Original/Train/False/*")
false_loc = "/home/data/jinyoung/Server/Demo4/Original/Train/False/"
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
#pdb.set_trace()


true_len = len(true_video_list)
false_len = len(false_video_list)
test_len = int(len(Both) * 0.2)
'''
print("Test len :", test_len)
for i,vid_n in enumerate(Both):
    if i < test_len:
        print("Both_test :", vid_n)
        for k in true:
            if k.startswith(true_loc + vid_n + '_'):
                #print("Test True : ",true_loc + vid_n )
                command = ("cp %s /home/data/jinyoung/Server/Demo4/Original/Test/True/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
        
        for l in false:
            if l.startswith(false_loc + vid_n + '_'):
                #print("Test False :", false_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo4/Original/Test/False/"%(l))
                output = subprocess.call(command, shell=True, stdout=None)
    else:
        print("Both_train :", vid_n)
        for k in true:
            if k.startswith(true_loc + vid_n + '_'):
                #print("Train True :", true_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo4/Original/Train/True/"%(k))
                output = subprocess.call(command, shell=True, stdout=None)
        
        for l in false:
            if l.startswith(false_loc + vid_n + '_'):
                #print("Train False:", false_loc + vid_n)
                command = ("cp %s /home/data/jinyoung/Server/Demo4/Original/Train/False/"%(l))
                output = subprocess.call(command, shell=True, stdout=None)
print("T_F STARTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i,vid_n in enumerate(T_F):
    print("T_F", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            #print("Train True :", true_loc + vid_n)
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Original/Train/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("F_T STARTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i,vid_n in enumerate(F_T):
    print("F_T", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            #print("Train False :", false_loc + vid_n)
             command = ("cp %s /home/data/jinyoung/Server/Demo4/Original/Train/False/"%(k))
             output = subprocess.call(command, shell=True, stdout=None)


'''
true_len = len(true_video_list)
false_len = len(false_video_list)
test_len1 = int(0.25*true_len)
test_len1_2 = int(0.5*true_len)
test_len1_3 = int(0.75*true_len)
test_len2 = int(0.25*false_len)
test_len2_2 = int(0.5*false_len)
test_len2_3 = int(0.75*false_len)
true_A = true_video_list[test_len1:]
true_A_test = true_video_list[0:test_len1]
true_B = true_video_list[0:test_len1] + true_video_list[test_len1_2:]
true_B_test = true_video_list[test_len1:test_len1_2]
true_C = true_video_list[0:test_len1_2] + true_video_list[test_len1_3:]
true_C_test = true_video_list[test_len1_2:test_len1_3]
true_D = true_video_list[:test_len1_3]
true_D_test = true_video_list[test_len1_3:]


false_A = false_video_list[test_len2:]
false_A_test = false_video_list[0:test_len2]
false_B = false_video_list[0:test_len2] + false_video_list[test_len2_2:]
false_B_test = false_video_list[test_len2:test_len2_2]
false_C = false_video_list[0:test_len2_2] + false_video_list[test_len2_3:]
false_C_test = false_video_list[test_len2_2:test_len2_3]
false_D = false_video_list[:test_len2_3]
false_D_test = false_video_list[test_len2_3:]

print(len(true_A), len(true_A_test), len(true_B), len(true_B_test), len(true_C), len(true_C_test), len(true_D), len(true_D_test))
print(len(false_A), len(false_A_test), len(false_B), len(false_B_test), len(false_C), len(false_C_test), len(false_D), len(false_D_test))
#pdb.set_trace()
print("_A True start")
for vid_n in true_A:
    print("A:", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_A/Train/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in true_A_test:
    print("A_test", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_A/Test/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("_B True start")
for vid_n in true_B:
    print("_B", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_B/Train/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in true_B_test:
    print("_B test", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_B/Test/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("_C True start")
for vid_n in true_C:
    print("_C Train:", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_C/Train/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in true_C_test:
    print("_C Test", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_C/Test/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("_D True start")
for vid_n in true_D:
    print("_D:", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_D/Train/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in true_D_test:
    print("_D test", vid_n)
    for k in true:
        if k.startswith(true_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_D/Test/True/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)


print("_A False start")
for vid_n in false_A:
    print("A:", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_A/Train/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in false_A_test:
    print("A_test", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_A/Test/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("_B True start")
for vid_n in false_B:
    print("_B test", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_B/Train/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in false_B_test:
    print("_B test", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_B/Test/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("_C True start")
for vid_n in false_C:
    print("_C Train:", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_C/Train/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in false_C_test:
    print("_C Test", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_C/Test/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
print("_D True start")
for vid_n in false_D:
    print("_D:", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_D/Train/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)
for vid_n in false_D_test:
    print("_D test", vid_n)
    for k in false:
        if k.startswith(false_loc + vid_n + '_'):
            command = ("cp %s /home/data/jinyoung/Server/Demo4/Demo4_D/Test/False/"%(k))
            output = subprocess.call(command, shell=True, stdout=None)

