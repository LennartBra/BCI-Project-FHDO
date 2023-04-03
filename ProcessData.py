# -*- coding: utf-8 -*-
"""
Class for Data - Process data
"""
#%% Import Packages
import matplotlib.pyplot as plt
from scipy import signal


#%% Class Definition Data
class Data:
    
    #Create Object of Class Data
    def __init__(self,data,channels):
        self.data = data
        #self.channels = ["FC5", "FC1", "FC2", "FC6", "C3", "C4", "--", "--"]
        self.channels = channels
    
    #Define function to plot EEG data
    def plot_EEG_data(self):
        for i in range(0,len(self.data[:,])):
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
        CutOffF = 15
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
        
        
        
        
        
        #Define function to plot all PPG channels
    def plot_PPG_data_AllChannels(self):
        for i in range(0,len(self.data[:,])):
            plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.xlabel('Sample')
        plt.ylabel('Absorption of light')
        plt.legend()
        plt.show()
        
        
    #Funktionen für das maschinelle Lernen
