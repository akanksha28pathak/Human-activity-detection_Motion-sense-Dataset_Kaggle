# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# CODE 1: INITIAL PREPROCESSING WITH CSV FILES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
#import seaborn as sns
from scipy import signal
import os

#fold_name=['dws_1','dws_2','dws_11','ups_3','ups_4','ups_12','wlk_7','wlk_8', 'wlk_15','jog_9','jog_16','sit_5','sit_13','std_6','std_14' ]
#folder_name="E:\LOCKDOWN_READING\KAGGLE_PRACTISE\A_DeviceMotion_data\DATASET/"
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
'''
'''
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

'''
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
    
axs.set_xlabel("Frequency (Hz)")    
'''


# code 5: save PSD of both sensors in numpy format
'''
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
             dd=da[sen]  #change column name here for analyzing other columns
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
'''    
 

# code 6:  compute features from PSD of both sensors
'''
num_sub=24
num_fold=15
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
    
    PSD_sen=np.load(sen+'_PSD.npy')
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
        
'''

# code 7: classification code
path_name="E:\LOCKDOWN_READING\KAGGLE_PRACTISE\A_DeviceMotion_data/"
sub_folder_name=['dws_1','dws_2','ups_1','ups_2','wlk_1','wlk_2', 'jog_1','jog_2','sit_1','sit_2','std_1','std_2' ]
class_name=['dws','ups','wlk', 'jog','sit','std']

sensor_name=['userAcceleration_Mag','rotationRate_Mag']

for i in sensor_name:
    
    for cnt,j in enumerate(class_name):
      
        for l in range(1,3,1):
            df=pd.read_csv(path_name + i+"/" + j +"_"+str(l)+ "_PSD_feature.csv")
       
             # add target column in df
            df['target']=cnt
            df.to_csv()
      
       

      
      