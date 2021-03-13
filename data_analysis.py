# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# CODE 1: INITIAL PREPROCESSING WITH CSV FILES.
# Initially we will work with UserAcceleration and RotationRate. Since, these inputs are given in form of x,y,z components, we first obtain their magnitude.
# Hence, this code adds magnitue of UserAcceleration and RotationRate to original csv files and removes  their x, y,z components. 
# ALong with this, time stamps are also added as an additional column

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
#fold_name=['dws_1','dws_2','dws_11','ups_3','ups_4','ups_12','wlk_7','wlk_8', 'wlk_15','jog_9','jog_16','sit_5','sit_13','std_6','std_14' ]
folder_name=".../A_DeviceMotion_data/"  # enter respective path
Fs=50 # sampling frequency
'''
def mag_comp(df,col):
# compute magnitude of vector
 df[col+'_Mag']=np.sqrt(df[col+'.x']**2+df[col+'.y']**2+df[col+'.z']**2)
 df=df.drop([col+'.x',col+'.y',col+'.z'],axis=1)
 return df

# compute magnitude of acceleartion, roation of each file, delete x,y,z vectors and add one column of time stamps

for i in fold_name:
    print(i)
    path_name=folder_name+i
    print(path_name)
    for j in range(1,25,1):
         da=pd.read_csv(path_name+"/sub_"+str(j)+".csv")
         da=mag_comp(da,'userAcceleration')
         da=mag_comp(da,'rotationRate')
         # compute time stamp 
         tt=np.arange(0,da.shape[0])
         tt=tt/Fs
         da['time_id']=tt
         file_name=path_name+"/sub_N_"+str(j)+".csv" # make new csv files for further processing
         da.to_csv(file_name,index=False)
         del da

