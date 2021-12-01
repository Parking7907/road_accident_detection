import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
vid_list = glob("/home/data/jinyoung/Server/CADP/test/True/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]
vid_len = {}
'''
with open('./UCF_dict.pickle', 'rb') as fr:
    data = pickle.load(fr)

print(data)
with open('./dict.txt', 'w') as f:
    for value in sorted(data.keys()):
        #pdb.set_trace()
        #print(data[value])
        #f.write(value)
        f.write(str(data[value]) + '\n')
f.close()
#data.sort()
#print(sorted(data.keys()))
'''
vid_list.sort()
for i in vid_list:
    with open(i, 'rb') as fr:
        data = pickle.load(fr)
    vid_len[i] = len(data)
    print(len(data))
    
    #images = []
    #pickle_file_name = './true/' + i.split('/')[-1] + '.pkl'
    #print(pickle_file_name)
    #pic = open(pickle_file_name, 'wb')
    
    #img_list = glob(os.path.join(i, '*'))
with open('UCF_dict.pickle','wb') as fw:
    pickle.dump(vid_len, fw)
print(vid_len)