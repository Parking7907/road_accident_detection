import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image

vid_list = glob("/home/data/jinyoung/Server/Testing_Normal_pickle/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]/home/data/jinyoung/Server/frame_data/UCF_Frames/Testing_Normal_Frames/

for i in vid_list:
    images = []
    pickle_file_name = './UCF_normal_test_pickle/' + i.split('/')[-1] + '.pkl'
    print(pickle_file_name)
    pic = open(pickle_file_name, 'wb')
    img_list = glob(os.path.join(i, '*'))
    img_list.sort()
    for j in img_list:
        im = Image.open(j)
        not_im = np.array(im)
        images.append(not_im)
        #im.close()
        
    images = np.array(images)
    
    #print(images.shape)
    pickle.dump(images,pic)
    #print(img_list)
    pic.close()