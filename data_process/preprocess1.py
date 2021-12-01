import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
vid_list = glob("/home/data/jinyoung/Server/UCF_Frames/road/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]

for i in vid_list:
    images = []
    pickle_file_name = './UCF_Pickle/' + i.split('/')[-1] + '.pkl'
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