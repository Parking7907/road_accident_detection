import cv2
import numpy as np
import glob
import os
import pdb
import pandas as pd
img_array = []
img_array_2 = []
#size = (1280, 720)
frame_rate = 30
dir1 = "/home/data/jinyoung/Server/result_original_video/"
video_list = glob.glob('/home/data/jinyoung/Server/result_original/*')
video_list.sort()
label = pd.read_csv('/home/data/jinyoung/Server/CADP_labeling.csv')
#pdb.set_trace()
for video_name in video_list:
    img_array = []
    #img_array_2 = []
    name = os.path.basename(video_name)
    list_ = glob.glob(video_name + '/*.jpg')
    #saliency_list = glob.glob(dir1 + name + '/*.png') # 480 X 360?
    #saliency_list2 = glob.glob(dir2 + name + '/*.png')
    list_.sort()
    #saliency_list.sort()
    #saliency_list2.sort()
    #v_ = int(name)
    #I_Frame = int(label['Impact_Frame'][v_]) 
    for i, filename in enumerate(list_):
        #if i >= I_Frame and i < I_Frame + 61:
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            #img_sal1 = cv2.imread(saliency_list[i]) / 255
            #img_sal2 = cv2.imread(saliency_list2[i]) / 255
            #dst = cv2.resize(img_sal1, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
            #dst2 = cv2.resize(img_sal2, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
            #img1 = img * img_sal1
            #img2 = img * img_sal2
            #print("Done :", filename, saliency_list[i])
            #pdb.set_trace()
            img_array.append(img)
            #img_array_2.append(img2)
        
    
        
    new_videoname = video_name.split('/')[-1]
    print(new_videoname)
    out = cv2.VideoWriter('./result_original_video/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    for i in range(len(img_array)):
        out.write(np.uint8(img_array[i]))
    out.release()