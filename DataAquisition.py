# -*- coding: utf-8 -*-
"""
Created on Sat Oct 1 2022

@author: Lennart Brakelmann
Class for Data Acquisition
"""
#Import Packages
import GUI
import CommunicationCytonBoard as CCB
import PySimpleGUI as sg
import matplotlib.pyplot as plt

#%% Start Algorithm
#Define GUI Pictures and Paths
GUI.init_settings()
#Create Main Window
window_menu = GUI.make_window_menu()
event_menu, values_menu = window_menu.read()

while True:
    
    if window_menu == sg.WIN_CLOSED or event_menu == "EXIT":
        window_menu.close()
        break
    
    if event_menu == "Testaufnahme":
        #Initialize Cyton Board and Data Stream
        CytonBoard, eeg_chan = CCB.Init_CytonBoard()
        outlet_eeg = CCB.defineStreamInfo(CytonBoard)
        #Close Main Window
        window_menu.close()
        
        eegchunk = []
        #Create TestSequence Window
        window_testsequence = GUI.make_testsequence_window_()
              
        ###################
        # Start Algorithm #
        ###################
        
        ###EEG-Daten abrufen
        while True:            
            #Monitoring window status
            event_testsequence , values_testsequence = window_testsequence.read(timeout=4)
            #Load Data into Ringbuffer
            data = CytonBoard.get_board_data() 
            
            if event_testsequence == sg.WIN_CLOSED or len(eegchunk) > 10000:
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
            elif event_testsequence == sg.TIMEOUT_KEY:            
                # don't send empty data
                if len(data[0]) < 1 : continue
                #Get eeg data for all channels
                eeg_data = data[eeg_chan]
                
                print(len(eegchunk))
                
                print('------------------------------------------------------------------------------------------')
                
                ### in range (len)????
                for i in range(len(eeg_data[0])):
                    eegchunk.append((eeg_data[:,i]).tolist())
                outlet_eeg.push_chunk(eegchunk)
                
                
    if event_menu == "Trainingsaufnahme":
        sg.popup_error("Not yet implemented")
        window_menu.close()
        
    if event_menu == "Klassifikationsaufnahme":
        sg.popup_error("Not yet implemented")
        window_menu.close()

        
def plot_EEG_data(eeg_data):
    for i in range(0,6):
        plt.plot(range(0, len(eeg_data[i])),eeg_data[i])
    plt.legend()
    plt.show()
    
