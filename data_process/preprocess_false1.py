import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
from PIL import Image
vid_list = glob("/home/data/jinyoung/Server/False2/*")
#vid_list = ["/home/data/jinyoung/Server/accident_data/000003"]
for i in vid_list:
    #print(pickle_file_name)
    big_img_list = glob(os.path.join(i, '*'))
    big_img_list.sort()
    st = 0
    en = 0
    print(big_img_list)
    for k in range(100):
        if st <len(big_img_list) - 400:
            vidlen = np.random.randint(40, 400)
            en = en + vidlen
            images = []
            img_list = big_img_list[st:en]
            print(str(st) + "~" + str(en))
            pickle_file_name = './false/false1/' + i.split('/')[-1] +'_' +str(k) + '.pkl'
            pic = open(pickle_file_name, 'wb')
            for j in img_list:
                im = Image.open(j)
                not_im = np.array(im)
                images.append(not_im)
                #im.close()
            images = np.array(images)    
            pickle.dump(images,pic)
            print(images.shape)
            pic.close()
            st = en
        
    
    
    #print(images.shape)
    
    #print(img_list)
    