# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 2022

@author: Lennart Brakelmann
Class for processing data
"""
#%% Import Packages
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


#%% Class Definition
class Data:
    
    def __init__(self,data,channels):
        self.data = data
        #self.channels = ["FC5", "FC1", "FC2", "FC6", "C3", "C4", "--", "--"]
        self.channels = channels
        
    def plot_EEG_data(self):
        for i in range(0,6):
            plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.legend()
        plt.show()
    
    def plot_PPG_data(self):
        for i in range(0,3):
            plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.legend()
        plt.show()
        
    def plot_PPG_datatest(self):
        i=1
        plt.plot(range(0, len(self.data[i])),self.data[i],label = self.channels[i])
        plt.legend()
        plt.show()
        
    def filterEEG(self):
        order = 9
        CutOffF = 15
        SampleRate = 250
        b, a = signal.butter(order, CutOffF,btype="low",analog=False,fs=SampleRate) 
        EEG_filtered = signal.lfilter(b,a,self.data)
        self.data = EEG_filtered

    def filterPPG(self):
        order = 9
        CutOffF = 5
        SampleRate = 250
        b, a = signal.butter(order, CutOffF,btype="low",analog=False,fs=SampleRate) 
        PPG_filtered = signal.lfilter(b,a,self.data[1])
        self.data[1] = PPG_filtered
        
        
