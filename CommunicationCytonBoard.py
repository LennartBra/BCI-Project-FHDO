# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 2022

@author: Lennart Brakelmann
Class for Getting Data
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
    
    #Define Stream Info for EEG-Data
    name = 'OpenBCIEEG'
    ID = 'OpenBCIEEG'
    channels = 8
    sample_rate = 250
    datatype = 'float32'
    streamType = 'EEG'
    print(f"Creating stream for EEG. \nName: {name}\nID: {ID}\n")
    ### Stream Info Objekt erstellen
    info_eeg = StreamInfo(name, streamType, channels, srate, datatype, ID)
    chns = info_eeg.desc().append_child("channels")
    ### Kanäle und Label zueinander zuweisen
    for label in label_name:
        ch = chns.append_child("channel")
        ch.append_child_value("label", label)
    outlet_eeg = StreamOutlet(info_eeg)
    
    
def record_data():
    