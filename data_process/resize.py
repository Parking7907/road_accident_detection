import json
import pdb
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree

#ffmpeg -ss [시작시간] -t [길이] -i [동영상이름] -r [프레임레이트] -s [출력해상도] -qscale:v 2 -an(오디오부분 제거) -f image2 [이미지이름]
#command = (ffmpeg -i ./demo_video/5.mp4 -filter_complex "[0:v]crop=448:256:16:80[cropped]" -map "[cropped]"output.mp4)
#output = subprocess.call(command, shell=True, stdout=None)
vid_list = glob("/home/data/jinyoung/Server/video_data/accident_data_video/*")
out_root = "/home/data/jinyoung/Server/accident_data_frame/"
print("Start!")
print(vid_list)
for i in vid_list:
    
    vid_name = i.split('/')[-1]
    folder_name = vid_name.split('.avi')[0]
    print(folder_name)
    os.makedirs(os.path.join(out_root, folder_name),exist_ok=True)

    im_list = glob(i + '/*')
    im_list.sort()
    #print(im_list)

    for j in im_list:
        im_name = j.split('/')[-1]
        #print(im_name)
        command = ("ffmpeg -i {0} -s 224x224 -qscale:v 2 -f image2 ./False2_224_Test/{1}/{2}".format(j,folder_name,im_name))
        output = subprocess.call(command, shell=True, stdout=None)
    #os.makedirs(os.path.join(out_root, folder_name),exist_ok=True)
    #print(vid_name, folder_name)

    #print("ffmpeg -ss 00:00:00 -t 10 -i ./accident_data/{0}.mp4 -r 30 -s 224x224 -an -y  -qscale:v 2 -f image2 ./accident_data/{1}/%06d.jpg".format(vid_name,folder_name))
   
#for i in *.avi; do ffmpeg -ss 00:00:00 -t 10 -i "$i" -f image2 "./${i%.*}.mp4"; done
'''
for file_name in glob("./sk/*"):
    loca = os.path.basename(file_name)
    video_name = os.path.splitext(loca)[0]
    file_n = os.path.join(file_name,"alphapose-results.json")
    print(video_name)
    with open(file_n,"r") as alpha:
        data = json.load(alpha)
    #data = np.array(data)
    data_len = len(data)
    #print(data_len)
    tmp_box = [[0 for col in range(1)] for row in range(150)]
    tmp_list = [[0 for col in range(1)] for row in range(150)]
    tmp_1 = {}


    #print(data_len)
    for i in range(data_len):
        image_id = int(os.path.splitext(data[i]['image_id'])[0])
        keypoints = data[i]['keypoints']
        box = data[i]['box']
        #print(box)
        #print(image_id)
        #print(keypoints)
        #tmp_list = np.append([tmp_list,keypoints], axis=0)
        #print(tmp_list[image_id])
        if tmp_list[image_id] == [0]:
            tmp_list[image_id][0]=keypoints
        elif tmp_list[image_id] != [0]:
            tmp_list[image_id].append(keypoints)
        if tmp_box[image_id] == [0]:
            tmp_box[image_id][0]=box
        elif tmp_box[image_id] != [0]:
            tmp_box[image_id].append(box)
    #print(tmp_list)
    #print(len(tmp_box))
    #print(tmp_list)
#         tmp_1 = {'name':video_name, 'keypoints':tmp_list, 'box':tmp_box}
    tmp_1 = {'keypoints':tmp_list, 'box':tmp_box}
    #pickle.dump
    with open('train/Fight/'+video_name+'.pkl', 'wb') as f:  
        pickle.dump(tmp_1, f)

    print(tmp_1)
    print(len(tmp_1['box']))
    #print(len(tmp_1['keypoints'][0]))
'''
