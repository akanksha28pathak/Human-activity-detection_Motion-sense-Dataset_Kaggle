# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:22:56 2021

@author: AKANKSHA PATHAK
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import signal
import os

# code 5: save PSD of both sensors in numpy format
folder_name="....\A_DeviceMotion_data\DATASET/" # enter path for dataset
Fs=50
sub_folder_name=['dws_1','dws_2','dws_11','ups_3','ups_4','ups_12','wlk_7','wlk_8', 'wlk_15','jog_9','jog_16','sit_5','sit_13','std_6','std_14' ]

sensor_name=['userAcceleration_Mag','rotationRate_Mag']

for sen in sensor_name:
    print(sen)
    PSD_all=np.empty([15,24,65]) # 15 folders, 24 subjects and 65 points FFT
    
    for k, i in enumerate(sub_folder_name): 
        s=np.empty([24,65])
        path_name=folder_name+i
        
       # print(path_name)
        for j in range(1,25,1):
            
             file_name=path_name+"/sub_N_"+str(j)+".csv"
             
             da=pd.read_csv(file_name)
             dd=da[sen]  
             # find index of 15 sec time stamp
             
             if dd.shape[0]<=15*Fs:
                 loc_15=dd.shape[0]
             else:
                 loc_15=da.loc[da['time_id']==15].index[0]
             
             # take data of sensor upto 15 sec
             dd=dd[0:loc_15+1]
             
             dd=(dd-dd.mean())/dd.std()
             f, Pxx_den = signal.welch(dd, Fs, nperseg=50,nfft=128)
             s[j-1,:]=Pxx_den
             del da, dd, Pxx_den
             
       # avg_psd=np.mean(s,axis=0) 
        PSD_all[k,:,:]=s
    np.save(sen+'_PSD.npy',PSD_all)
           
        
    # just cheking by plotting 
    
    plt.plot(PSD_all[14,23,:])
    plt.show()    