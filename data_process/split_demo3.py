import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
true = glob("/home/data/jinyoung/Server/True_Frames/*")
false = glob("/home/data/jinyoung/Server/False_Frames/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]
true.sort()
false.sort()
vid_len = {}
true_len = len(true)
false_len = len(false)
test_len1 = int(0.25*true_len)
test_len1_2 = int(0.5*true_len)
test_len1_3 = int(0.75*true_len)
test_len2 = int(0.25*false_len)
test_len2_2 = int(0.5*false_len)
test_len2_3 = int(0.75*false_len)
print(test_len1)
print("True split")
print(true_len, test_len1, test_len1_2, test_len1_3)
print(false_len, test_len2, test_len2_2, test_len2_3)

for i,vid_name in enumerate (true):
    if i < test_len1:
        command = ("cp %s /home/data/jinyoung/Server/Demo3/Test/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
    else:
        command = ("cp %s /home/data/jinyoung/Server/Demo3/Train/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)



print("B - True split")
for i,vid_name in enumerate (true):
    if test_len1 <= i <test_len1_2 :
        command = ("cp %s /home/data/jinyoung/Server/Demo3_B/Test/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
    else:
        command = ("cp %s /home/data/jinyoung/Server/Demo3_B/Train/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)

print("C - True split")

for i,vid_name in enumerate (true):
    if test_len1_2 <= i <test_len1_3:
        command = ("cp %s /home/data/jinyoung/Server/Demo3_C/Test/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
    else:
        command = ("cp %s /home/data/jinyoung/Server/Demo3_C/Train/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)


print("D - True split")
for i,vid_name in enumerate (true):
    if i >= test_len1_3:
        command = ("cp %s /home/data/jinyoung/Server/Demo3_D/Test/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
    else:
        command = ("cp %s /home/data/jinyoung/Server/Demo3_D/Train/True/"%(vid_name))
        output = subprocess.call(command, shell=True, stdout=None)
