# -*- coding: utf-8 -*-
"""
Created on Sat Oct 1 2022

@author: Lennart Brakelmann
Script for Data Acquisition
"""
#Import Packages
import numpy as np
from GUI import GUI
from ProcessData import Data
import CommunicationCytonBoard as CCB
import PySimpleGUI as sg
import matplotlib.pyplot as plt

#%% Functions    
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



#%% Start Algorithm - Create GUI
#Create Object of Class GUI
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
        CytonBoard, eeg_chan, ppg_chan = CCB.Init_CytonBoard()
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"EEG")
        
        #Close Main Window
        window_menu.close()
        
        #Create Arrays for EEG_Data
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
            
            if len(EEG) > 2000:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.test[1])
            if len(EEG) > 2250:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.test[2])
            if len(EEG) > 2500:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.test[3])
                
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                eegchunk = data[eeg_chan]
                #print("Laenge Chunk",len(eegchunk[0]),"Buffer Count",buffer_count)
                #Save eegchunk in EEG
                EEG = process_eegchunk(eegchunk,EEG)
                
    if event_menu == "Test Sequence PPG":        
        #Initialize Cyton Board
        CytonBoard, eeg_chan, ppg_chan = CCB.Init_CytonBoard()
        
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"PPG")
        
        #Close Main Window
        window_menu.close()
        
        
        #Create Arrays for PPG Data
        ppgchunk = []
        PPG = []
        #Create TestSequence Window
        window_testsequence_ppg = GUI.make_testsequence_window_ppg()
        
        ###################
        # Start Algorithm #
        ###################
        while True:            
            #Monitoring window status
            event_testsequence_ppg , values_testsequence_ppg = window_testsequence_ppg.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
            
            if event_testsequence_ppg == sg.WIN_CLOSED or len(PPG) > 2500:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_testsequence_ppg = None
                #Close Test Sequence Window
                window_testsequence_ppg.close()
                #Make PPG NumPy Array
                PPG = np.array(PPG)
                PPG = np.moveaxis(PPG,0,1)
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                
                
                break
                
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                ppgchunk = data[ppg_chan]
                
                #print("Laenge Chunk",len(ppgchunk[0]),"Buffer Count",buffer_count)
                #Save ppgchunk in PPG
                PPG = process_ppgchunk(ppgchunk,PPG)
            
            

#%%Plot anfertigen
#channels = ["FC5", "FC1", "FC2", "FC6", "C3", "C4", "--", "--"]
#EEG_TestAufnahme = Data(EEG,channels)
#EEG_TestAufnahme.plot_EEG_data()

channels = ["19","20","21"]
PPG_TestAufnahme = Data(PPG,channels)
PPG_TestAufnahme.filterPPG()
PPG_TestAufnahme.plot_PPG_datatest()


