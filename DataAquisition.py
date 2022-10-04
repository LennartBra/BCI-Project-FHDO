# -*- coding: utf-8 -*-
"""
Created on Sat Oct 1 2022

@author: Lennart Brakelmann
Class for Data Acquisition
"""
#Import Packages
import numpy as np
import GUI
import CommunicationCytonBoard as CCB
import PySimpleGUI as sg
import matplotlib.pyplot as plt

#%% Functions
def plot_EEG_data(eeg_data):
    for i in range(0,6):
        plt.plot(range(0, len(eeg_data[i])),eeg_data[i])
    plt.legend()
    plt.show()
    
def process_data(eeg_data,eegchunk,outlet_eeg):
    for i in range(len(eeg_data[0])):
        #Load new data to list
        eegchunk.append((eeg_data[:,i]).tolist())
    #Push data to outlet eeg
    outlet_eeg.push_chunk(eegchunk)
    return eegchunk,outlet_eeg

def processing_testsession(raw):
    
    X_raw = np.array(raw)
    X_raw = np.moveaxis(X_raw,0,1)
    
    ### Range(0,6), weil 6 Kanäle verwendet werden --> siehe Bachelorarbeit
    X_raw_mod = []
    ### Signal Mittelwertfrei machen
    for i in range(0,6):
        temp = X_raw[i]-np.mean(X_raw[i])
        X_raw_mod.append(temp)
    
    X_raw_mod = np.array(X_raw_mod)
       
    return X_raw_mod

#%% Start Algorithm
#Define GUI Pictures and Paths
GUI.init_settings()
#Create Main Window
window_menu = GUI.make_window_menu()
event_menu, values_menu = window_menu.read()

while True:
    
    if window_menu == sg.WIN_CLOSED or event_menu == "EXIT":
        window_menu.close()
        event_menu = None
        break
    
    if event_menu == "Testaufnahme":
        #Initialize Cyton Board and Data Stream
        CytonBoard, eeg_chan = CCB.Init_CytonBoard()
        outlet_eeg = CCB.defineStreamInfo(CytonBoard)
        #Close Main Window
        window_menu.close()
        
        eegchunk = []
        #Create TestSequence Window
        window_testsequence = GUI.make_testsequence_window()
              
        ###################
        # Start Algorithm #
        ###################
        while True:            
            #Monitoring window status
            event_testsequence , values_testsequence = window_testsequence.read(timeout=1)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
            print(buffer_count)
            print('-----------------')
            
            if event_testsequence == sg.WIN_CLOSED or len(eegchunk) > 5000:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_testsequence = None
                #Close Test Sequence Window
                window_testsequence.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                break
            
            #Load data from Ringbuffer
            elif buffer_count > 64:
                #Get Board data and delete ringbuffer
                data = CytonBoard.get_board_data()
                
                eeg_data = data[eeg_chan]
                
                eegchunk,outlet_eeg = process_data(eeg_data,eegchunk,outlet_eeg)
                
                
            
            
            
            
            '''
            Tobis Version
            elif event_testsequence == sg.TIMEOUT_KEY: 
                
                # don't send empty data
                if len(data[0]) < 1 : continue
                #Get eeg data for all channels
                eeg_data = data[eeg_chan]
                
                print(len(eegchunk))
                print('-----------------------------------------------')
                
                ### in range (len)????
                for i in range(len(eeg_data[0])):
                    #Load new data to list
                    eegchunk.append((eeg_data[:,i]).tolist())
                #Push data to outlet eeg
                outlet_eeg.push_chunk(eegchunk)
                '''
                
    if event_menu == "Trainingsaufnahme":
        #sg.popup_error("Not yet implemented")
        #window_menu.close()
        
        #Initialize Cyton Board and Data Stream
        CytonBoard, eeg_chan = CCB.Init_CytonBoard()
        outlet_eeg = CCB.defineStreamInfo(CytonBoard)
        #Close Main Window
        window_menu.close()
        
        eegchunk = []
        #Create TestSequence Window
        window_testsequence = GUI.make_testsequence_window()
              
        ###################
        # Start Algorithm #
        ###################
        while True:            
            #Monitoring window status
            event_testsequence , values_testsequence = window_testsequence.read(timeout=1)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
            print(buffer_count)
            print('-----------------')
            
            if event_testsequence == sg.WIN_CLOSED or len(eegchunk) > 5000:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_testsequence = None
                #Close Test Sequence Window
                window_testsequence.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                break
            
            #Load data from Ringbuffer
            elif buffer_count > 64:
                #Get Board data and delete ringbuffer
                data = CytonBoard.get_board_data()
                
                eeg_data = data[eeg_chan]
                
                eegchunk,outlet_eeg = process_data(eeg_data,eegchunk,outlet_eeg)        
        
        
    if event_menu == "Klassifikationsaufnahme":
        sg.popup_error("Not yet implemented")
        window_menu.close()

#%%Plot anfertigen
EEG = processing_testsession(eegchunk)
plot_EEG_data(EEG)
