# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:46:46 2021

@author: AKANKSHA PATHAK
"""

# code 6:  compute features from PSD of both sensors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#import seaborn as sns
from scipy import signal
import os


num_sub=24
num_fold=15

folder_name="...\A_DeviceMotion_data\DATASET/" # enter path for dataset  
Fs=50
sub_folder_name=['dws_1','dws_2','dws_11','ups_3','ups_4','ups_12','wlk_7','wlk_8', 'wlk_15','jog_9','jog_16','sit_5','sit_13','std_6','std_14' ]

sensor_name=['userAcceleration_Mag','rotationRate_Mag']

from scipy.stats import entropy
from scipy.stats import moment

# function for computing features from PSD
def features_compute(Pxx):
    
    # compute full band spectral entropy
     Pxx_hat=Pxx/np.sum(Pxx) # normalize the psd
     print(sum(Pxx_hat))
     ent=entropy(Pxx_hat,axis=0)
     
     # compute moments of spectrum
     m1=np.mean(Pxx)
     m2=np.std(Pxx)
     m3=moment(Pxx,moment=3)
     m4=moment(Pxx,moment=4)
     
     return ent,m1,m2,m3,m4
  
    
     
     

for sen in sensor_name:
    
    PSD_sen=np.load(sen+'_PSD.npy')  # assumes numpy file of PSD in same location 
    path_name=os.path.join(folder_name,sen)
    os.mkdir(path_name)
    
    for j in range(0,num_fold,1):
        fold_data=PSD_sen[j,:,:]
        feat_folder=np.empty([num_sub,5])
        
        for k in range(0,num_sub,1):
            
            PSD_sub=fold_data[k,:]
            spe,mo1,mo2,mo3,mo4=features_compute(PSD_sub)
            feat_folder[k,:]=[spe,mo1,mo2,mo3,mo4]
            del PSD_sub,spe,mo1,mo2,mo3,mo4
        
        # make data  frame for the folder
        df=pd.DataFrame(feat_folder,columns=['SPE','Mean','STD','SKEW','KURT'])
       
        #path_name=os.path.join(path_name)
        # path_name=++"/"++"/"
       
        df.to_csv(path_name+"/"+sub_folder_name[j]+"_PSD_feature.csv",index=True)    
        del df
        