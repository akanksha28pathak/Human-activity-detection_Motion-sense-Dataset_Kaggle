# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# CODE 3: Plot time domain signal averaged over all subjects for each class

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
folder_name="..../A_DeviceMotion_data/"  # add path to the folder
Fs=50
#sub_folder_name=['dws_2','ups_4','wlk_8','jog_16','sit_13','std_14' ]  # comment one row of sub-folder at a time. This is done for ease of visualization.
sub_folder_name=['dws_1','ups_3','wlk_7','jog_9','sit_5','std_6' ]

fig, a = plt.subplots(6,1)
a=a.ravel()

for  axs, i in zip(a,sub_folder_name):
   
    s=np.empty([24,750])  # 24 subjects with 750 samples of sensor data (15sec*50 Hz/sec)
    path_name=folder_name+i
    
   # print(path_name)
    for j in range(1,25,1):
         file_name=path_name+"/sub_N_"+str(j)+".csv"
         
         da=pd.read_csv(file_name)
         dd=da['rotationRate_Mag']  #change column name here for analyzing other columns such as UserAcceleration_Mag
         dd=(dd-dd.mean())/dd.std() # normalize the time series data for complete duration available
         
         s[j-1,:]=np.asarray(dd[0:15*Fs]) # take the first 15 sec of data
         del da, dd
         
    avg_class=np.mean(s,axis=0)   # take mean across all subjects
    
    axs.plot(avg_class)  
    axs.set_title(i)
    plt.show()
    del avg_class
    
