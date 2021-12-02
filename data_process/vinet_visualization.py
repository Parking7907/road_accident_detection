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
dir1 = "/home/data/jinyoung/Server/result_ViNet/"
output_dir1 = "/home/data/jinyoung/Server/result_vinet_video/"
#dir2 = "/home/data/jinyoung/Server/accident_data_saliency2/"
video_list = glob.glob('/home/data/jinyoung/Server/accident_data_frame/*')
video_list.sort()
label = pd.read_csv('/home/data/jinyoung/Server/CADP_labeling.csv')
#pdb.set_trace()
for video_name in video_list:
    img_array = []
    name = os.path.basename(video_name)
    list_ = glob.glob(video_name + '/*.jpg')
    saliency_list = glob.glob(dir1 + name + '/*.jpg') # 480 X 360?
    list_.sort()
    saliency_list.sort()
    v_ = int(name)
    I_Frame = int(label['Impact_Frame'][v_]) 
    for i, filename in enumerate(list_):
        #if i >= I_Frame and i < I_Frame + 61: # For True Label only
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_sal1 = cv2.imread(saliency_list[i]) / 255
            dst = cv2.resize(img_sal1, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
            img1 = img * img_sal1
            print("Done :", filename, saliency_list[i])
            img_array.append(img1)
        
    
        
    new_videoname = video_name.split('/')[-1]
    print(new_videoname)
    out = cv2.VideoWriter('%s%s_demo.avi'%(output_dir1, name),cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    for i in range(len(img_array)):
        out.write(np.uint8(img_array[i]))
    out.release()

    #out2 = cv2.VideoWriter('./result2_true/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    #for i in range(len(img_array_2)):
    #    out2.write(np.uint8(img_array_2[i]))
    #out2.release()