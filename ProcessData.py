# -*- coding: utf-8 -*-
"""
Class for Data - Process data
"""
#%% Import Packages
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import random

#Functions for processing recorded chunks
def process_eegchunk(eegchunk,EEG):
    for i in range(len(eegchunk[0])):
        #Load new data to list
        EEG.append((eegchunk[:,i]).tolist())
    return EEG

def process_ppgchunk(ppgchunk,PPG):
    for i in range(len(ppgchunk[0])):
        #Load new data to list
        PPG.append((ppgchunk[:,i]).tolist())
    return PPG

#Function for filtering X
def filter_X(X):
    order = 9
    CutOffF = 4
    SampleRate = 250
    b, a = signal.butter(order, CutOffF,btype="low",analog=False,fs=SampleRate) 
    X_filtered = signal.lfilter(b,a,X.copy())
    return X_filtered

#Function for standardizing X
def standardize_X(X):
    X_standardized = []
    for i in range(0,len(X)):
        X_temp = X[i].copy()
        for i in range(0,len(X_temp)):
            X_temp[i] = (X_temp[i] - np.mean(X_temp[i])) / np.std(X_temp[i])
        X_standardized.append(X_temp)
    X_standardized = np.array(X_standardized)
    return X_standardized  

def meanfree_X(X):
    X_meanfree = []
    for i in range(0,len(X)):
        X_temp = X[i].copy()
        for i in range(0,len(X_temp)):
            X_temp[i] = (X_temp[i] - np.mean(X_temp[i]))
        X_meanfree.append(X_temp)
    X_meanfree = np.array(X_meanfree)
    return X_meanfree 

def make_random_order(n_trials):
    order = []
    for i in range(0,n_trials):
        if i % 2 == 0:
            order.append(0)
        else:
            order.append(1)
    order = np.array(order)       
    random.shuffle(order)
    
    return order
    
#%% Class Definition Data
class Data:
    
    #Create Object of Class Data
    def __init__(self,data,channels):
        self.data = data.copy()
        self.channels = channels
        self.X = []
        self.y = []
        self.X_test = []
        self.y_test = []
        global n_channels
        n_channels = 6
    
    #Define function to plot EEG data
    def plot_EEG_data(self):
        for i in range(0,n_channels):
            plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.xlabel('Sample')
        plt.ylabel('Voltage in mV')
        plt.legend()
        plt.show()
    
    #Define function to plot PPG data
    def plot_PPG_data(self):
        i = 1
        plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.xlabel('Sample')
        plt.ylabel('Absorption of light')
        plt.legend()
        plt.show()
    
    #Define function to filter EEG
    def filterEEG(self):
        order = 9
        CutOffF = 4
        SampleRate = 250
        b, a = signal.butter(order, CutOffF,btype="low",analog=False,fs=SampleRate) 
        EEG_filtered = signal.lfilter(b,a,self.data)
        self.data = EEG_filtered
    
    #Define Function to filter PPG
    def filterPPG(self):
        order = 9
        CutOffF = 15
        SampleRate = 250
        b, a = signal.butter(order, CutOffF,btype="low",analog=False,fs=SampleRate) 
        PPG_filtered = signal.lfilter(b,a,self.data[1])
        self.data[1] = PPG_filtered
        
    def standardize_EEG(self):
        for i in range(0,len(self.data)):
            self.data[i] = (self.data[i] - np.mean(self.data[i])) / np.std(self.data[i])
    
    def mean_free_EEG(self):
        for i in range(0,len(self.data)):
            self.data[i] = self.data[i] - np.mean(self.data[i])
        
        
        #Define function to plot all PPG channels
    def plot_PPG_data_AllChannels(self):
        for i in range(0,len(self.data[:,])):
            plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.xlabel('Sample')
        plt.ylabel('Absorption of light')
        plt.legend()
        plt.show()
        
        

        
    #Functions for Machine Learning
    
    #Function for making X and y
    def make_X_and_y(self,time_stamps,training_labels):
        X = []
        y = training_labels
        OneSec = 250
        Movement_Duration = 4
        for count, time_value in enumerate(time_stamps):
            X.append(self.data[:n_channels,time_value:time_value+OneSec*Movement_Duration])
            print(count)
        X = np.array(X)
        self.X = X
        y = np.array(y)
        self.y = y
        return X, y
    
    #Function for making X_test and y_true
    def make_Xtest_and_ytrue(self,classification_time_stamps,classification_labels):
        X_test = []
        y_true = classification_labels
        OneSec = 250
        Movement_Duration = 4
        for count, time_value in enumerate(classification_time_stamps):
            X_test.append(self.data[:n_channels,time_value:time_value+OneSec*Movement_Duration])
        X_test = np.array(X_test)
        self.X_test = X_test
        y_true = np.array(y_true)
        self.y_true = y_true
        return X_test,y_true
    