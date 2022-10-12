# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 2022

@author: Lennart Brakelmann
Class for Communication with CytonBoard
"""

#%%Import Packages
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from pylsl import StreamInfo, StreamOutlet

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
    params.serial_port = 'COM5'
    #Initialize CytonBoard with Parameters
    board = BoardShim(BoardIds.CYTON_BOARD.value, params)
    #Get List of EEG Channels
    eeg_chan = BoardShim.get_eeg_channels(BoardIds.CYTON_BOARD.value)
    #Get List of PPG Channel
    ppg_chan = BoardShim.get_analog_channels(BoardIds.CYTON_BOARD.value)
    
    #Print all EEG Channels
    print('EEG channels:')
    print(eeg_chan)
    print('PPG channels')
    print(ppg_chan)
    
    return board,eeg_chan,ppg_chan
    
def startDataStream(board,session):
    #Prepare Session and initialize ressources
    board.prepare_session()
    #Configure Board Pins for session
    if session == "EEG":
        board.config_board("/0")
        BoardMode = board.config_board("//")
        print(BoardMode)
    elif session == "PPG":
        board.config_board("/2")
        BoardMode = board.config_board("//")
        print(BoardMode)
    #Start Data Stream of Cyton Board into Ringbuffer
    board.start_stream()
    
def stopDataStream(board):
    #Stop Streaming Session
    board.stop_stream()
    #Release all Ressources
    board.release_session()
    


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
