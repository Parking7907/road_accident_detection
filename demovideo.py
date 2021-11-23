import cv2
import numpy as np
from glob import glob
import pickle
import pdb
import os
img_array = []
label_list = glob("/home/jinyoung/road_accident_detection/label/output_*")
for label in label_list:
    video_name = os.path.basename(label)
    video_name = video_name.split('_')[1]
    video_name = video_name.split('.')[0]
    print(video_name)
    with open(label, 'rb') as fr:
        visual_data = pickle.load(fr)
    img_list = glob("/home/jinyoung/car_accident_dataset/%s_1280/*.jpg"%video_name)
    print(len(img_list))
    visual_threshold = 0.5
    visual_label = []
    score = [0 for _ in range(len(visual_data))]
    for j in range(len(visual_data)):
        #if j < 30:
        score[j] = visual_data[j] 
        #else:
        #    score[j] = visual_data[j:j+30].sum() / 30

    img_list.sort()
    img_array = [] # 없애면 연결되는 현상..?
    for i, filename in enumerate(img_list):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        tl = round(0.002 * (3000) / 2) + 1
        tf = max(tl - 1, 1)
        if i < 31:
            cv2.putText(img, 'Visual : waiting..', (900,80), 0, tl / 3, [0, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        else:
            if score[i-31] > visual_threshold:
                cv2.putText(img, 'Visual : True', (900,80), 0, tl / 3, [0, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
            elif score[i-31] < visual_threshold:
                cv2.putText(img, 'Visual : False', (900,80), 0, tl / 3, [0, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    out = cv2.VideoWriter('./result/demo_%s.avi'%video_name,cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()



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