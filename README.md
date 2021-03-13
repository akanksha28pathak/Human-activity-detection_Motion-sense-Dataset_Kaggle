# Human-activity-detection_Motion-sense-Dataset_Kaggle
This repository contains my codes for analysis of motion sense dataset, feature engineering and classification results. The description of respectives files is as follows

1. data_preprocessing.py-  Initially we worked with UserAcceleration and RotationRate as inputs. Since, these inputs are given in form of x,y,z components, we first obtain their 
magnitude. Hence, this code adds two new columns of magnitude of UserAcceleration and RotationRate to original csv files and removes  their x, y,z components. 
Along with this, time stamps are also added as an additional column for our ease of analysis.

2. time_duration_analysis.py- For any time-series data, before heading forward with any sort of feature engineering and classificatio, it is necessary to know about the duration of data. If the entire data is of same duration, then one can proceed with a single value. But if the duration varies from instant to instant, then we need to pick up a suitable duration, that meets the criterion for sufficient analysis without discarding many instants of database. In this code, we found that 15 sec duration was apt as per the above stated requirements.


