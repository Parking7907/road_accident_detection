import cv2
import numpy as np
import glob
import os
import pdb
img_array = []
img_array_2 = []
#size = (1280, 720)
frame_rate = 30
dir1 = "/home/data/jinyoung/Server/accident_data_saliency/"
dir2 = "/home/data/jinyoung/Server/accident_data_saliency2/"
video_list = glob.glob('/home/data/jinyoung/Server/accident_data_frame/*')
video_list.sort()
for video_name in video_list:
    img_array = []
    img_array_2 = []
    name = os.path.basename(video_name)
    list_ = glob.glob(video_name + '/*.jpg')
    saliency_list = glob.glob(dir1 + name + '/*.png') # 480 X 360?
    saliency_list2 = glob.glob(dir2 + name + '/*.png')
    list_.sort()
    saliency_list.sort()
    saliency_list2.sort()
    
    for i, filename in enumerate(list_):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_sal1 = cv2.imread(saliency_list[i]) / 255
        img_sal2 = cv2.imread(saliency_list2[i]) / 255
        dst = cv2.resize(img_sal1, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
        dst2 = cv2.resize(img_sal2, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
        img1 = img * img_sal1
        img2 = img * img_sal2
        print("Done :", filename, saliency_list[i])
        #pdb.set_trace()
        img_array.append(img1)
        img_array_2.append(img2)
        
    
        
    new_videoname = video_name.split('/')[-1]
    print(new_videoname)
    out = cv2.VideoWriter('./result/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    for i in range(len(img_array)):
        out.write(np.uint8(img_array[i]))
    out.release()

    out2 = cv2.VideoWriter('./result2/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    for i in range(len(img_array_2)):
        out2.write(np.uint8(img_array_2[i]))
    out2.release()