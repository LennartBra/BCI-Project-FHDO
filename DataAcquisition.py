# -*- coding: utf-8 -*-
"""
Created on Sat Oct 1 2022

@author: Lennart Brakelmann
Class for Data Acquisition
"""
#Import Packages
import numpy as np
from GUI import GUI
import CommunicationCytonBoard as CCB
import PySimpleGUI as sg
import matplotlib.pyplot as plt

#%% Functions
def plot_EEG_data(eeg_data):
    for i in range(0,6):
        plt.plot(range(0, len(eeg_data[i])),eeg_data[i])
    plt.legend()
    plt.show()
    
def process_eegchunk(eegchunk,EEG):
    for i in range(len(eegchunk[0])):
        #Load new data to list
        EEG.append((eegchunk[:,i]).tolist())
    return EEG


#%% Start Algorithm
#Define GUI Pictures and Paths
GUI = GUI()
#Create Main Window
window_menu = GUI.make_window_menu()
event_menu, values_menu = window_menu.read()


###############################################################################
################################Check GUI Status###############################
###############################################################################

while True:
    
    if window_menu == sg.WIN_CLOSED or event_menu == "EXIT":
        window_menu.close()
        event_menu = None
        break
  
    if event_menu == "Test Sequence EEG":
        #Initialize Cyton Board
        CytonBoard, eeg_chan = CCB.Init_CytonBoard()
        #Start Data Stream
        CCB.startDataStream(CytonBoard)
        
        #Close Main Window
        window_menu.close()
        
        #Create Array for EEG_Data
        eeg_data = []
        eegchunk = []
        EEG = []
        #Create TestSequence Window
        window_testsequence_eeg = GUI.make_testsequence_window_eeg()
              
        ###################
        # Start Algorithm #
        ###################
        while True:            
            #Monitoring window status
            event_testsequence_eeg , values_testsequence_eeg = window_testsequence_eeg.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
            
            if event_testsequence_eeg == sg.WIN_CLOSED or len(EEG) > 5000:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_testsequence_eeg = None
                #Close Test Sequence Window
                window_testsequence_eeg.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                
                EEG = np.array(EEG)
                EEG = np.moveaxis(EEG,0,1)
                
                break
            
            if len(EEG) > 2500:
                window_testsequence_eeg["-IMAGE-"].update(filename=GUI.path+GUI.test[0])
            
            #Load data from Ringbuffer
            if buffer_count > 1:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                eegchunk = data[eeg_chan]
                #Save eegchunk in EEG
                EEG = process_eegchunk(eegchunk,EEG)
                
    if event_menu == "Test Sequence PPG":        
        break
            
            
            

#%%Plot anfertigen
plot_EEG_data(EEG)

