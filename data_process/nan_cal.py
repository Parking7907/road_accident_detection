import numpy as np
import torch
import csv
import pdb
from glob import glob
#pdb.set_trace()
TeTr = glob("/home/data/jinyoung/Server/Demo/Test/True/*") 
TeFa = glob("/home/data/jinyoung/Server/Demo/Test/False/*") 
TrTr = glob("/home/data/jinyoung/Server/Demo/Train/True/*") 
TrFa = glob("/home/data/jinyoung/Server/Demo/Train/False/*")
nan_list = []
print("TestTrue")
for idx,npy_file in enumerate(TeTr):
    if idx%100 == 0:
        print(idx)
    bb = np.load(npy_file, allow_pickle = True)
    cc = torch.from_numpy(bb)
    if torch.isnan(cc).any() == True:
        print(npy_file)
        nan_list.append(npy_file)
print(nan_list)
nan_list = []
print("TeFa")
for idx,npy_file in enumerate(TeFa):
    if idx%1000 == 0:
        print(idx)
    bb = np.load(npy_file, allow_pickle = True)
    cc = torch.from_numpy(bb)
    if torch.isnan(cc).any() == True:
        print(npy_file)
        nan_list.append(npy_file)
print(nan_list)
nan_list = []
print("TrTr")
for idx,npy_file in enumerate(TrTr):
    if idx%1000 == 0:
        print(idx)
    bb = np.load(npy_file, allow_pickle = True)
    cc = torch.from_numpy(bb)
    if torch.isnan(cc).any() == True:
        print(npy_file)
        nan_list.append(npy_file)
print(nan_list)
nan_list = []
print("TrFa")
for idx,npy_file in enumerate(TrFa):
    if idx%1000 == 0:
        print(idx)
    bb = np.load(npy_file, allow_pickle = True)
    cc = torch.from_numpy(bb)
    if torch.isnan(cc).any() == True:
        print(npy_file)
        nan_list.append(npy_file)
print(nan_list)

print('feassfgdsfd')