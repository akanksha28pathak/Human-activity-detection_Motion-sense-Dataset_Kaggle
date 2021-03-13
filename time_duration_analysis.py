# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
#CODE 2: Analyse min-max duration of data in each folder. We have used two approaches visually as well as counter based. For visual inspection, histogram of time duration 
#  for each folder is ploted. For counter based option, we have counted number of subjects in each folder below certian threshold of time duration.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
#fold_name=['dws_1','dws_2','dws_11','ups_3','ups_4','ups_12','wlk_7','wlk_8', 'wlk_15','jog_9','jog_16','sit_5','sit_13','std_6','std_14' ]
folder_name=".../A_DeviceMotion_data/"  # enter path of folder
Fs=50

k=1

time_dur_class=[]
fig, a = plt.subplots(5,3) 
a=a.ravel()
min_dur=[]
sub_count=[]
for axs, i in zip(a,fold_name):
   # print(axs,i)
    cnt=0
    path_name=folder_name+i
    time_dur=[]
   # print(path_name)
    for j in range(1,25,1):
         file_name=path_name+"/sub_N_"+str(j)+".csv"
         #print(file_name)
         da=pd.read_csv(file_name)
         tt=da['time_id']
         time_dur.append(tt.iloc[-1])   
         if(tt.iloc[-1]<15):  # Replace 15 with any duration you want to check
            cnt=cnt+1
         del da, tt               
    

    min_dur.append(min(time_dur))
    sub_count.append(cnt)  # sub_count list contains number of subjects in each folder with duration less than 15 sec
    axs.hist(np.asarray(time_dur),bins=24)
    axs.set_title(i)
    plt.show()
    
    if(k>12):
       axs.set_xlabel("Duration (sec)")
    k=k+1   

