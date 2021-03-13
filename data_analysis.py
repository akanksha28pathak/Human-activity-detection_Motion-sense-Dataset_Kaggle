# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# CODE 1: INITIAL PREPROCESSING WITH CSV FILES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
#fold_name=['dws_1','dws_2','dws_11','ups_3','ups_4','ups_12','wlk_7','wlk_8', 'wlk_15','jog_9','jog_16','sit_5','sit_13','std_6','std_14' ]
folder_name="E:/LOCKDOWN_READING/KAGGLE_PRACTISE/A_DeviceMotion_data/"
Fs=50
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
         file_name=path_name+"/sub_N_"+str(j)+".csv"
         da.to_csv(file_name,index=False)
         del da

#CODE 2: Find min-max duration of data in each folder
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
         if(tt.iloc[-1]<15):
            cnt=cnt+1
         del da, tt               
    
#plt.figure()
    min_dur.append(min(time_dur))
    sub_count.append(cnt)
    #fig.suptitle('Horizontally stacked subplots')
    axs.hist(np.asarray(time_dur),bins=24)
    #axs=sns.boxplot(np.asarray(time_dur))
    axs.set_title(i)
    plt.show()
    
    if(k>12):
       axs.set_xlabel("Duration (sec)")
    k=k+1   

'''
'''
num_point=da.shape[0]
arr=np.arange(0,num_point,1)
da['id']=arr

#plt.figure()
da.plot(kind='line', y='userAcceleration_Mag',x='id')
plt.show()
da.plot(kind='line', y='rotationRate_Mag',x='id')
plt.show()
#zz=pd.dataframe(arr,colums=['ind'])
'''

# code 3: plot time domain signal averaged over all subjects for each class
'''
#sub_folder_name=['dws_2','ups_4','wlk_8','jog_16','sit_13','std_14' ]
sub_folder_name=['dws_1','ups_3','wlk_7','jog_9','sit_5','std_6' ]
fig, a = plt.subplots(6,1)
a=a.ravel()

for  axs, i in zip(a,sub_folder_name):
   
    s=np.empty([24,750])
    path_name=folder_name+i
    
   # print(path_name)
    for j in range(1,25,1):
         file_name=path_name+"/sub_N_"+str(j)+".csv"
         
         da=pd.read_csv(file_name)
         dd=da['rotationRate_Mag']  #change column name here for analyzing other columns
         dd=(dd-dd.mean())/dd.std()
         
         s[j-1,:]=np.asarray(dd[0:15*Fs])
         del da, dd
         
    avg_class=np.mean(s,axis=0)   
    
    axs.plot(avg_class)  
    axs.set_title(i)
    plt.show()
    del avg_class
    '''
# code 4: plot average spectrum of  signal   averaged over all subjects for each class
from scipy import signal

#sub_folder_name=['dws_2','ups_4','wlk_8','jog_16','sit_13','std_14' ]
sub_folder_name=['dws_1','ups_3','wlk_7','jog_9','sit_5','std_6' ]
fig, a = plt.subplots(6,1)
a=a.ravel()

for  axs, i in zip(a,sub_folder_name):
   
    s=np.empty([24,65])
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