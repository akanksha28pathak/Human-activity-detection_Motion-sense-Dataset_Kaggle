# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# CODE 4: plot average spectrum of  signal   averaged over all subjects for each class
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import signal

folder_name="..../A_DeviceMotion_data/" #add folder path for dataset
Fs=50

#sub_folder_name=['dws_2','ups_4','wlk_8','jog_16','sit_13','std_14' ] # comment one subfolder at a time for ease of visualization
sub_folder_name=['dws_1','ups_3','wlk_7','jog_9','sit_5','std_6' ]
fig, a = plt.subplots(6,1)
a=a.ravel()

for  axs, i in zip(a,sub_folder_name):
   
    s=np.empty([24,65])  # empty numpy array for storing one-sided PSD(NFFT/2+1 points of FFT) of 24 subjects
    path_name=folder_name+i
    
   # print(path_name)
    for j in range(1,25,1):
         file_name=path_name+"/sub_N_"+str(j)+".csv"
         
         da=pd.read_csv(file_name)
         dd=da['userAcceleration_Mag']  #change column name here for analyzing other columns
         dd=(dd-dd.mean())/dd.std()
         f, Pxx_den = signal.welch(dd, Fs, nperseg=50,nfft=128)
         s[j-1,:]=Pxx_den
         del da, dd, Pxx_den
         
    avg_psd=np.mean(s,axis=0)   
    
    axs.plot(f,avg_psd)  
    axs.set_title(i)
    plt.show()
    del avg_psd
