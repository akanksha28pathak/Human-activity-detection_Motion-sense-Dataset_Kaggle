# Human-activity-detection_Motion-sense-Dataset_Kaggle
This repository contains my codes for analysis of motion sense dataset, feature engineering and classification results. The description of respectives files is as follows

1. data_preprocessing.py-  Initially we worked with UserAcceleration and RotationRate as inputs. Since, these inputs are given in form of x,y,z components, we first obtain their 
magnitude. Hence, this code adds two new columns of magnitude of UserAcceleration and RotationRate to original csv files and removes  their x, y,z components. 
Along with this, time stamps are also added as an additional column for our ease of analysis.
