##### NOTE, just run once, this file will continous split 0.3 of DATASET


import os,random
import numpy as np
import shutil
import pathlib
DATASET_NAME = 'UCF-101'
TEST_SET = 0.3

DATASET_TRAIN_PATH_NAME = 'UCF-101_Train'

DATASET_PATH = os.path.join(os.getcwd(), DATASET_NAME)

for index, folder in enumerate(sorted(os.listdir(DATASET_PATH))):
#if index < 1:
    print(folder)    
    folder_path = os.path.join(DATASET_PATH,folder) # /UCF-101/ApplyEyeMakeUp
    files_in_folder = sorted(os.listdir(folder_path)) #/UCF-101/ApplyEyeMakeUp/*.avi
    number_of_files = len(files_in_folder) # Number of fiels in /UCF-101/ApplyEyeMakeUp
    limit_files_to_split = round(number_of_files*TEST_SET) 
    #print(folder_path)
    #print(files_in_folder)

    x=np.array(files_in_folder)
    idx = sorted(np.random.choice(range(0,number_of_files,1), limit_files_to_split, replace=False)) #Number of train_data

    mask=np.full(len(files_in_folder),True,dtype=bool)
    mask[idx]=False
    #print(mask)
    Train = x[mask]
    Test = x[~mask]
    print(len(Test))

#print("Total files in folder" ,number_of_files)
#print("Number of file used to train: ",limit_files_to_split)
#Test_index = sorted(np.random.uniform(low=0,high=number_of_files,size=limit_files_to_split).astype(int))
#print(Test_index)

    for video in enumerate(Test):
        # print(os.getcwd()) # /home/g1413531/keras-video-classifier/demo/very_large_data
        print(video[1])
        video_path_old = os.path.join(folder_path,video[1]) # /home/g1413531/keras-video-classifier/demo/very_large_data/UCF-101/ApplyEyeMakeupv_ApplyEyeMakeup_g01_c03.avi
        print(video_path_old)

        des_path = os.path.join(os.getcwd(),DATASET_TRAIN_PATH_NAME,folder) # .../very_large_data/UCF-101_Train/ApplyEyeMakeup
        video_path_new = os.path.join(os.getcwd(),DATASET_TRAIN_PATH_NAME,folder,video[1]) # .../very_large_data/UCF-101_Train/ApplyEyeMakeup

        pathlib.Path(des_path).mkdir(parents=True, exist_ok=True) 
        print(des_path)
        print(video_path_new)
        shutil.move(video_path_old,video_path_new)
        print("Moved " + video_path_old + " to " + video_path_new)