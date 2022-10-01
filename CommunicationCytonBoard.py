# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 2022

@author: Lennart Brakelmann
Class for Communication with CytonBoard
"""
###############################################################################
#################################Import Packages###############################
###############################################################################
#%%Packages
import keyboard
import numpy as np
import brainflow
import random
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import GUI

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from pylsl import StreamInfo, StreamOutlet
from scipy import signal

###############################################################################
###################################Communication###############################
###############################################################################
#%%Initialize Communication with CYTON Board
def Init_CytonBoard():
    #Activate BrainFlow Logger
    BoardShim.enable_dev_board_logger()
    #Create BrainFlowInputParams Object
    params = BrainFlowInputParams()
    #Define Serial Port
    params.serial_port = 'COM3'
    #Initialize CytonBoard with Parameters
    board = BoardShim(BoardIds.CYTON_BOARD.value, params)
    #Get Sampling Rate
    srate = board.get_sampling_rate(BoardIds.CYTON_BOARD.value)
    #Prepare Session and initialize ressources
    board.prepare_session()
    ### Datenstream des Cyton Boards starten --> Daten in Ringbuffer abspeichern
    #Start Data Stream of Cyton Board into Ringbuffer
    board.start_stream()
    #Get List of EEG Channels
    eeg_chan = BoardShim.get_eeg_channels(BoardIds.CYTON_BOARD.value)
    
    #Print all EEG Channels
    print('EEG channels:')
    print(eeg_chan)
    
    return board,eeg_chan

def defineStreamInfo(board):
    #Define Stream Info for EEG-Data
    name = 'OpenBCIEEG'
    ID = 'OpenBCIEEG'
    channels = 8
    label_name = ["FC5", "FC1", "FC2", "FC6", "C3", "C4", "--", "--"]
    sample_rate = board.get_sampling_rate(BoardIds.CYTON_BOARD.value)
    datatype = 'float32'
    streamType = 'EEG'
    print(f"Creating stream for EEG. \nName: {name}\nID: {ID}\n")
    ### Stream Info Objekt erstellen
    info_eeg = StreamInfo(name, streamType, channels, sample_rate, datatype, ID)
    chns = info_eeg.desc().append_child("channels")
    ### Kanäle und Label zueinander zuweisen
    for label in label_name:
        ch = chns.append_child("channel")
        ch.append_child_value("label", label)
    outlet_eeg = StreamOutlet(info_eeg)
    
    return outlet_eeg

def stopDataStream(board):
    ### Datenstream beenden
    board.stop_stream()
    ### Alle Ressourcen releasen
    board.release_session()
    

'''
def record_EEGData():
    board = Init_CytonBoard()
    outlet_eeg = defineStreamInfo(board)
    
    ###########################
    # Start Setting Streaming #
    ###########################
    
    eegchunk = []
    
    ##################
    # Setting Window #
    ##################
    
    window_menu.close()
    window_testing = make_window_testing()
           
    ###################
    # Start Algorithm #
    ###################
    
    ###EEG-Daten abrufen
    while True:            
        # Getting data from Cyton Board
        ### Abfrage der GUI
        event_testing, values_testing = window_testing.read(timeout=4)
        ### Daten einlesen in Variable data --> aus Ringbuffer Objekt
        data = board.get_board_data() 
        
        # Stop Streaming
        ### Wenn Test-EEG 40 Sekunden lang ist oder das Fenster geschlossen wird
        ### Verarbeitung der Daten
        if event_testing == sg.WIN_CLOSED or len(eegchunk) > 10000:
            ### Datenstream beenden
            board.stop_stream()
            ### Alle Ressourcen releasen
            board.release_session()  
            
            # Plot data
            ### Daten plotten, EEG aus Kanal über Länge des Kanals plotten +
            ### Kanallabel --> Legende
            test_data = processing_testsession(eegchunk)
            for i in range(0,6):
                plt.plot(range(0, len(test_data[i])),test_data[i], label=label_name[i])
            plt.legend()
            plt.show()
            
            event_testing = None
            window_testing.close()
            window_menu = make_window_menu()
            event_menu, values_menu = window_menu.read()

            break
        
        
        # Work with the data from Cyton Board
        ### EEG-Daten der unterschiedlichen Channels aus eeg_data abgreifen
        ### und in eegchunk abspeichern
        ### Wenn eine bestimmte Zeit vergangen ist, werden die Daten abgerufen
        elif event_testing == sg.TIMEOUT_KEY:            
            # don't send empty data
            if len(data[0]) < 1 : continue
            ### EEG-Daten für die einzelnen Channels aus data abgreifen
            eeg_data = data[eeg_chan]
            
            print(len(eegchunk))
            
            print('------------------------------------------------------------------------------------------')
            
            ### in range (len)????
            for i in range(len(eeg_data[0])):
                eegchunk.append((eeg_data[:,i]).tolist())
            outlet_eeg.push_chunk(eegchunk)
            
'''