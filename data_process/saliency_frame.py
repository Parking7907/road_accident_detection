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
dir1 = "/home/data/jinyoung/Server/mask_Unet1/"
dir2 = "/home/data/jinyoung/Server/mask_Unet2/"
video_list = glob.glob('/home/data/jinyoung/Server/CADP_Frames/*')
video_list.sort()
label = pd.read_csv('/home/data/jinyoung/Server/CADP_labeling.csv')
#pdb.set_trace()
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
    v_ = int(name)
    partion = label['Partion'][v_]
    if label['Impact_Frame'][v_] == 'Not':
        print("Passing because of Not Accident") 
        continue
    if label['Impact_Frame'][v_] == 'SV':
        print("Passing because of Same Video")
        continue
    if partion == True:
        print("Partion!")
        I_Frame = int(label['Impact_Frame'][v_].split(',')[0])
        I_Frame2 = int(label['Impact_Frame'][v_].split(',')[1])
        for i, filename in enumerate(list_):
            if i >= I_Frame and i <= I_Frame2:
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width,height)
                img_sal1 = cv2.imread(saliency_list[i]) / 255
                img_sal2 = cv2.imread(saliency_list2[i]) / 255
                dst = cv2.resize(img_sal1, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
                dst2 = cv2.resize(img_sal2, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
                img1 = img * dst
                img2 = img * dst2
                print("Partion Done :", filename, saliency_list[i], (height, width))
                #pdb.set_trace()
                os.makedirs('./frame_Unet1/%06d'%v_, exist_ok=True)
                os.makedirs('./frame_Unet2/%06d'%v_, exist_ok=True)
                cv2.imwrite("./frame_Unet1/%06d/%06d.jpg"%(v_,i), img1)
                cv2.imwrite("./frame_Unet2/%06d/%06d.jpg"%(v_,i), img2)
                
            
            #img_array.append(img1)
            #img_array_2.append(img2)
    else:
        I_Frame = int(label['Impact_Frame'][v_])
        for i, filename in enumerate(list_):
            if i >= I_Frame and i < I_Frame + 61:
                img = cv2.imread(filename)
                height, width, layers = img.shape
                size = (width,height)
                img_sal1 = cv2.imread(saliency_list[i]) / 255
                img_sal2 = cv2.imread(saliency_list2[i]) / 255
                dst = cv2.resize(img_sal1, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
                dst2 = cv2.resize(img_sal2, dsize=(height, width), interpolation=cv2.INTER_LINEAR)
                img1 = img * dst
                img2 = img * dst2
                print("Done :", filename, saliency_list[i], (height, width))
                #pdb.set_trace()
                os.makedirs('./frame_Unet1/%06d'%v_, exist_ok=True)
                os.makedirs('./frame_Unet2/%06d'%v_, exist_ok=True)
                cv2.imwrite("./frame_Unet1/%06d/%06d.jpg"%(v_,i), img1)
                cv2.imwrite("./frame_Unet2/%06d/%06d.jpg"%(v_,i), img2)
            
            
            #img_array.append(img1)
            #img_array_2.append(img2)
        
    
    
    new_videoname = video_name.split('/')[-1]
    print(new_videoname)
    '''
    out = cv2.VideoWriter('./result_true/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    for i in range(len(img_array)):
        out.write(np.uint8(img_array[i]))
    out.release()

    out2 = cv2.VideoWriter('./result2_true/%s_demo.avi'%name,cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, size)
    for i in range(len(img_array_2)):
        out2.write(np.uint8(img_array_2[i]))
    out2.release()
    '''