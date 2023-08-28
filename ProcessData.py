# -*- coding: utf-8 -*-
"""
ProcessData.py

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

def process_Training_Session(Session,time_stamps,channels):
    #Create Data Objects
    EEG_Training = Data(Session,channels)
    
    #Filter EEG
    EEG_Training.filterEEG()
    
    #Meanfree EEG
    EEG_Training.mean_free_EEG()
    
    X = make_X(EEG_Training.EEG_processed,time_stamps)
    
    return EEG_Training, X

#Function for making X
def make_X(Processed_Data, time_stamps):
    X = []
    OneSec = 250
    Movement_Duration = 4
    
    for count, time_value in enumerate(time_stamps):
        X.append(Processed_Data[:n_channels,time_value:time_value+OneSec*Movement_Duration])
        
    X = np.array(X)
    
    return X

def plot_X_different_color(X,labels):
    for i in range(0,len(X)):
        plt.plot(range(0, len(X[i])),X[i],label = labels[i])
    plt.xlabel('Sample')
    plt.ylabel('Voltage in mV')
    plt.legend()
    plt.show()     
    
def plot_X_i(X,labels):
    for i in range(0,len(X)):
        if labels[i] == 0:
            plt.plot(range(0, len(X[i])),X[i],color='blue')
        else:
            plt.plot(range(0, len(X[i])),X[i],color='red')
    plt.xlabel('Sample')
    plt.ylabel('Voltage in mV')
    #plt.legend()
    plt.show() 
    
def make_Result_plot(X_training, training_labels, X_test, classification_labels):
    fig, (ax1,ax2) = plt.subplots(1,2)
    for i in range(0,len(X_training)):
        if training_labels[i] == 0:
            ax1.plot(range(0, len(X_training[i])),X_training[i],color='blue')
        else:
            ax1.plot(range(0, len(X_training[i])),X_training[i],color='red')
    ax1.set_title('Trainingsdaten')
    for i in range(0,len(X_test)):
        if classification_labels[i] == 0:
            ax2.plot(range(0, len(X_test[i])),X_test[i],color='blue')
        else:
            ax2.plot(range(0, len(X_test[i])),X_test[i],color='red')
    ax2.set_title('Testdaten')
    ax1.set(xlabel='x',ylabel='Volatge in mV')
    ax2.set(xlabel='x',ylabel='Volatge in mV')
    fig.suptitle('Result Plot')
    plt.show()

#%% Class Definition Data
class Data:
    
    #Create Object of Class Data
    def __init__(self,data,channels):
        #Raw EEG/PPG
        self.data = data.copy()
        #Filtered EEG
        self.EEG_filtered = []
        #Filtered PPG
        self.PPG_filtered = []
        #Processed EEG --> Standardized or Meanfree
        self.EEG_processed = []
        #Used EEG channels for recording
        self.channels = channels
        
        global n_channels
        n_channels = 6
    
    #Define function to plot EEG data
    def plot_EEG_data(self, DataArray):
        n_channels = 6
        for i in range(0,n_channels):
            plt.plot(range(0, len(DataArray[i])),DataArray[i],label = self.channels[i])
        plt.xlabel('Sample')
        plt.ylabel('Voltage in mV')
        plt.legend()
        plt.show()
    
    #Define function to plot PPG data
    def plot_PPG_data(self, DataArray):
        plt.plot(range(0, len(DataArray)),DataArray)
        plt.xlabel('Sample')
        plt.ylabel('Absorption of light')
        plt.legend()
        plt.show()
    
    #Define function to filter EEG
    def filterEEG(self):
        
        SampleRate = 250
        lowcut = 0.5
        highcut = 4
        order = 1000
        CutOffF = 4
        
        #b_but, a_but = signal.butter(order, CutOff,btype="band",analog=False,fs=SampleRate)
        b_fir = signal.firwin(order, [lowcut, highcut], fs=SampleRate, pass_zero=False)
        #b_cheby, a_cheby = signal.cheby1(order,25, CutOff,btype="bandpass",fs=SampleRate)
        #b_fir = signal.firwin(order,CutOffF,fs=SampleRate)
        #w, h = signal.freqz(b_but,a_but,fs=250,worN=2000)
        w, h = signal.freqz(b_fir,1,fs=250,worN=2000)
        #w2, h2 = signal.freqz(b_cheby,a_cheby,fs=250,worN=2000)
        
        '''
        fs = 250
        nyq = 0.5 * fs
        CutOffFrequency = 4
        order = 55
        CutOff = 4 / nyq

        b_fir = signal.firwin(order,CutOff)
        
        
        w, h = signal.freqz(b_fir,1,fs=250,worN=2000)
        plt.figure()
        plt.plot(w, abs(h))
        plt.title('b,a Filter')
        plt.figure()
        plt.semilogx(w, 20 * np.log10(abs(h)))
        '''
        
        EEG_filtered = signal.filtfilt(b_fir,1,self.data)
        #self.data = EEG_filtered
        self.EEG_filtered = EEG_filtered.copy()
    
    #Define Function to filter PPG
    def filterPPG(self):
        order = 9
        CutOffF = 15
        SampleRate = 250
        b, a = signal.butter(order, CutOffF,btype="low",analog=False,fs=SampleRate) 
        PPG_filtered = signal.lfilter(b,a,self.data[1])
        #self.data[1] = PPG_filtered
        PPG_filtered = np.array(PPG_filtered)
        self.PPG_filtered = PPG_filtered
        
    def standardize_EEG(self):
        self.EEG_processed =  np.zeros(np.shape(self.EEG_filtered))
        for i in range(0,len(self.data)):
            self.EEG_processed[i] = (self.EEG_filtered[i] - np.mean(self.EEG_filtered[i])) / np.std(self.EEG_filtered[i])
    
    def mean_free_EEG(self):
        self.EEG_processed = np.zeros(np.shape(self.EEG_filtered))
        for i in range(0,len(self.data)):
            self.EEG_processed[i] = self.EEG_filtered[i] - np.mean(self.EEG_filtered[i])
        
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
        X = np.array(X)
        #self.X = X.copy()
        y = np.array(y)
        #self.y = y.copy()
        return X, y
    
    
    #Function for making X_test and y_true
    def make_Xtest_and_ytrue(self,classification_time_stamps,classification_labels):
        X_test = []
        y_true = classification_labels
        OneSec = 250
        Movement_Duration = 4
        for count, time_value in enumerate(classification_time_stamps):
            X_test.append(self.EEG_processed[:n_channels,time_value:time_value+OneSec*Movement_Duration])
            #X_test.append(self.EEG_filtered[:n_channels,time_value:time_value+OneSec*Movement_Duration])
        X_test = np.array(X_test)
        #self.X_test = X_test.copy()
        y_true = np.array(y_true)
        #self.y_true = y_true.copy()
        return X_test,y_true
       
    