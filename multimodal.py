import cv2
import numpy as np
from glob import glob
import pickle
import pdb
import os
from moviepy.editor import *

### Hyper Parameters
visual_threshold = 0.71
multimodal_threshold = 0.81
img_array = []
label_list =[]
audio_label_list = []
#data load
#with open('output_demo6_1.pkl', 'rb') as fr:
with open('output_movie0.pkl', 'rb') as fr:
    visual_data = pickle.load(fr)
#with open('name_demo6_1.pkl', 'rb') as f:
with open('name_movie0.pkl', 'rb') as fr:
    visual_label = pickle.load(f)
#Labeling
f = open("./label/20_score.txt", 'r', encoding='UTF-8')
lines = f.readlines()
for i in range(len(visual_label)):
    for j in range(len(visual_label[i])):
        lab = int(os.path.basename(visual_label[i][j]).split('_')[1])
        label_list.append(lab)

#Audio 처리
audio_score = [0 for _ in range(len(visual_data))]
print(len(audio_score))
for i in range(len(lines)):
    sc = lines[i].split('\n')[0]
    #print(sc)
    start = int(i*3)
    end = int(i*3) + 2
    print(i, start, end)
    if sc == 'False':
        for j in range(3):
            audio_score[start + j] = 0
    elif sc == 'True':
        for j in range(3):
            audio_score[start + j] = 1


#Image 처리
img_list = glob("/home/jinyoung/car_accident_dataset/Demo_20_1280/*.jpg")
img_list.sort()
print(len(img_list))
visual_label = []

score = [0 for _ in range(len(visual_data))]
for j in range(len(visual_data)):
    score[j] = visual_data[label_list[j]]
score = np.array(score)
score_list = [0 for _ in range(len(visual_data))]
for j in range(len(visual_data)):
    if j < 15:
        score_list[j] = score[0:j].sum()/(len(score[0:j])+1)
    else:
        score_list[j] = score[j-15:j].sum() / 15
#Multimodal 처리
multimodal_score = [0 for _ in range(len(visual_data))]
for j in range(len(visual_data)):
    multimodal_score[j] = score_list[j] + audio_score[j]
multimodal_score = np.array(multimodal_score)

multimodal_label = ["False" for _ in range(len(visual_data))]
print(len(multimodal_label))
for j in range(len(visual_data)):
    if multimodal_score[j] > multimodal_threshold:
        multimodal_label[j:j+15] = ["True"] * 15
print(len(multimodal_label),len(multimodal_score),len(score_list), len(audio_score))
    
pdb.set_trace()
for i, filename in enumerate(img_list):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    tl = round(0.002 * (3000) / 2) + 1
    tf = max(tl - 1, 1)
    if i < 31:
        cv2.putText(img, 'Visual: Standby', (930,150), 0, tl / 3, [0, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cv2.putText(img, 'Audio: Standby', (930,200), 0, tl / 3, [0, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cv2.putText(img, 'Multimodal: Standby', (620,80), 0, tl / 2, [0, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cv2.rectangle(img, (595,25), (1275,105), [0, 255, 255], 5)
    else:
        if score_list[i-31] > visual_threshold:
            cv2.putText(img, 'Visual: True', (980,150), 0, tl / 3, [0, 255, 0], thickness=tf, lineType=cv2.LINE_AA)
        elif score_list[i-31] < visual_threshold:
            cv2.putText(img, 'Visual: False', (980,150), 0, tl / 3, [0, 0, 255], thickness=tf, lineType=cv2.LINE_AA)
        
        if audio_score[i-31] == 1:
            cv2.putText(img, 'Audio: True', (980,200), 0, tl / 3, [0, 255, 0], thickness=tf, lineType=cv2.LINE_AA)
        elif audio_score[i-31] == 0:
            cv2.putText(img, 'Audio: False', (980,200), 0, tl / 3, [0, 0, 255], thickness=tf, lineType=cv2.LINE_AA)
        
        if multimodal_label[i-31] == 'True':
            cv2.putText(img, 'Multimodal: True', (700,80), 0, tl / 2, [255, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
            cv2.rectangle(img, (695,25), (1275,105), [255, 0, 0], 5)
        
        #if audio_score[i-31] == 1 and score_list[i-31] > visual_threshold:
        #    cv2.putText(img, 'Multimodal: True', (700,80), 0, tl / 2, [255, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
        #    cv2.rectangle(img, (695,25), (1275,105), [255, 0, 0], 5)
        #elif audio_score[i-31] == 1 and score_list[i-31] < visual_threshold:    
        #    cv2.putText(img, 'Multimodal: True', (700,80), 0, tl / 2, [255, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
        #    cv2.rectangle(img, (695,25), (1275,105), [255, 0, 0], 5)
        #elif audio_score[i-31] == 1 and score_list[i-31] < visual_threshold:
        #    cv2.putText(img, 'Multimodal: True', (700,80), 0, tl / 2, [255, 0, 0], thickness=tf, lineType=cv2.LINE_AA)
        #    cv2.rectangle(img, (695,25), (1275,105), [255, 0, 0], 5)
        
        elif multimodal_label[i-31] == 'False':
            cv2.putText(img, 'Multimodal: False', (700,80), 0, tl / 2, [0, 0, 255], thickness=tf, lineType=cv2.LINE_AA)
            cv2.rectangle(img, (695,25), (1275,105), [0, 0, 255], 5)

out = cv2.VideoWriter('./result/demo_%s_%0.2f.avi'%("demo6", visual_threshold),cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


videoclip = VideoFileClip('./result/demo_%s_%0.2f.avi'%("demo6", visual_threshold)).subclip(0, 20)
audioclip = AudioFileClip("./20.wav").subclip(0, 20)

videoclip.audio = audioclip
videoclip.write_videofile("output_%0.2f_%0.2f.mp4"%(visual_threshold, multimodal_threshold))

'''

        for idx_frame in image_list:
            fn = os.path.join(image_path,'%06d.jpg'%(idx_frame))
            print(fn)
            ori_im =cv2.imread(fn, cv2.IMREAD_COLOR)
            tl = round(0.002 * (3000) / 2) + 1  # line/font thickness
            tf = max(tl - 1, 1)
            
            if idx_frame % self.args.frame_interval:
                continue

            start = time.time()
            #im = cv2.cvtColor(ori_im, cv2.COLOR_BGR2RGB)
            im = ori_im
            height = len(ori_im) # 720
            width = len(ori_im[0]) # 1280
            threshold = 0.06
            # do detection
            #bbox_xywh, cls_conf, cls_ids = self.detector(im)


            # select car class
            #mask = cls_ids == 2
            
            

            #bbox_xyxy = np.array(dets_bbox[idx_frame])
            bbox_xywh = np.array(dets_bbox[idx_frame])
            #for j in range(len(dets_bbox[idx_frame])):
            #    bbox_xywh[j][2] = abs(bbox_xyxy[j][0] - bbox_xyxy[j][2])
            #    bbox_xywh[j][3] = abs(bbox_xyxy[j][1] - bbox_xyxy[j][3])
                
            # bbox dilation just in case bbox too small, delete this line if using a better pedestrian detector
            #bbox_xywh[:, 3:] *= 1.2
            cls_conf = dets_conf[idx_frame]
            

            # do tracking
            outputs = self.deepsort.update(bbox_xywh, cls_conf, im)
            #pdb.set_trace()

            # draw boxes for visualization
            if len(outputs) > 0:
                bbox_tlwh = []
                bbox_xyxy = outputs[:, :4]
                #print(bbox_xyxy)
                
                identities = outputs[:, -1]
                ori_im = draw_boxes(ori_im, bbox_xyxy, identities)
                #pdb.set_trace()


                for i in range(len(outputs)):
                    pos_dict[identities[i]].append((idx_frame, (float(bbox_xyxy[i][0]+bbox_xyxy[i][2])/2),float((bbox_xyxy[i][1]+bbox_xyxy[i][3])/2)))
                    #print(pos_dict[identities[i]])
                    if len(pos_dict[identities[i]]) > 2: 
                        time_d = pos_dict[identities[i]][-1][0] - pos_dict[identities[i]][-2][0]
                        #print(vel_dict[identities[i]])
                        vel_dict[identities[i]].append((idx_frame, (pos_dict[identities[i]][-1][1]-pos_dict[identities[i]][-2][1])/time_d, (pos_dict[identities[i]][-1][2]-pos_dict[identities[i]][-2][2])/time_d))
                    
                    if len(vel_dict[identities[i]]) > 2:
                        time_d_2 = vel_dict[identities[i]][-1][0] - vel_dict[identities[i]][-2][0]
                        acc_dict[identities[i]].append((idx_frame, (vel_dict[identities[i]][-1][1]-vel_dict[identities[i]][-2][1])/time_d_2, (vel_dict[identities[i]][-1][2]-vel_dict[identities[i]][-2][2])/time_d_2))
                        if abs(acc_dict[identities[i]][-1][1]) > threshold * width or abs(acc_dict[identities[i]][-1][2]) > threshold * height:
                            #print("acc_dict")
                            label = True
                            stack = 0
                        if label == True:
                            cv2.putText(ori_im, 'Road Accident Occured : %i, %f, %f'%(identities[i], acc_dict[identities[i]][-1][1], acc_dict[identities[i]][-1][2]), (100,80), 0, tl / 3, [0, 0, 255], thickness=tf, lineType=cv2.LINE_AA)
                            #print(idx_frame)
                            stack += 1
                        if stack >= 30:
                            stack = 0
                            label = False
                #pdb.set_trace()
            
                    
                

                for bb_xyxy in bbox_xyxy:
                    bbox_tlwh.append(self.deepsort._xyxy_to_tlwh(bb_xyxy))

                results.append((idx_frame - 1, bbox_tlwh, identities))

'''