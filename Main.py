# -*- coding: utf-8 -*-
"""
Main script for Data Acquisition
"""
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
#Import Packages
import numpy as np
from GUI import GUI
from ProcessData import Data
import CommunicationCytonBoard as CCB
import PySimpleGUI as sg
import matplotlib.pyplot as plt

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
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
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
                #Make EEG NumPy Array --> Rows = , Channels =
                EEG = np.array(EEG)
                EEG = np.transpose(EEG)
                
                break
            
            if len(EEG) > 4250:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[3])
            if len(EEG) > 4500:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[2])
            if len(EEG) > 4750:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[1])
                
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
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
        
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
                PPG = np.transpose(PPG)
                #Invert PPG
                PPG = -PPG
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                
                break
            
            if len(PPG) > 1750:
                window_testsequence_ppg["-PPG-"].update(filename=GUI.path+GUI.play[3])
            if len(PPG) > 2000:
                window_testsequence_ppg["-PPG-"].update(filename=GUI.path+GUI.play[2])
            if len(PPG) > 2250:
                window_testsequence_ppg["-PPG-"].update(filename=GUI.path+GUI.play[1])
                
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into ppgchunk
                ppgchunk = data[ppg_chan]

                #Save ppgchunk in PPG
                PPG = process_ppgchunk(ppgchunk,PPG)

    if event_menu == "Training Session": 
        #Close Main Window
        window_menu.close()
        #Create Instruction Window for Training Session
        training_window_instructions = GUI.make_training_window_instructions_eeg()
        
        #Create Arrays for EEG_Data
        eegchunk = []
        EEG = []
        EEG_temp = []
        time_stamps = []
        OneSec = 250
        TimeStampCheck = False
        n = 0
        
        while True:
            #Monitoring window status --> Start of Training Session
            event_training_window_instructions , values_training_window_instructions = training_window_instructions.read(timeout=4)
            
            if event_training_window_instructions == 'Start Training Session':
                break
            
        #Close Instruction Window
        training_window_instructions.close()
        
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
        
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"EEG")
        
        #Create Recording Window
        training_window = GUI.make_training_window_eeg()
        
        while True:
            #Monitoring Window Status
            event_training_window, values_training_window = training_window.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
        
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                eegchunk = data[eeg_chan]
                #Save eegchunk in EEG
                EEG = process_eegchunk(eegchunk,EEG)
                EEG_temp = process_eegchunk(eegchunk,EEG_temp)
                
            if len(EEG_temp) > OneSec*4:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[3])
            if len(EEG_temp) > OneSec*5:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[2])
            if len(EEG_temp) > OneSec*6:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[1])
            if len(EEG_temp) > OneSec*7:
                if TimeStampCheck == False:
                    time_stamps.append(len(EEG))
                    TimeStampCheck == True
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[0])
            if len(EEG_temp) > OneSec*7 + OneSec*2:
                EEG_temp = []
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.stop[0])
                TimeStampCheck = False
                n = n+1
                
        
            if event_training_window == sg.WIN_CLOSED or n == 9:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_training_window = None
                #Close Test Sequence Window
                training_window.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                #Make EEG NumPy Array --> Rows = , Channels =
                EEG = np.array(EEG)
                EEG = np.transpose(EEG)
                
                break
        
        
        
    if event_menu == "Classification Session": 
        #Close Main Window
        window_menu.close()
        sg.popup("Error: not implemented yet",background_color="white",button_color="orange",text_color="black")
        break


#%%Process EEG Data
channels = ["Cz","Fz","FC5", "FC1", "FC2", "FC6", "C3", "C4"]
EEG_TestAufnahme = Data(EEG,channels)
EEG_TestAufnahme.plot_EEG_data()


#%%Process PPG Data
channels = ["19","PPG","21"]
PPG_TestSequence = Data(PPG,channels)
PPG_TestSequence.filterPPG()
PPG_TestSequence.plot_PPG_data()

