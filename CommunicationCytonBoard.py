# -*- coding: utf-8 -*-
"""
Communication.py

Class for Communication with CytonBoard
"""

#%%Import Packages
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import time


#%%Define Functions for Communication with CytonBoard
###############################################################################
###################################Communication###############################
###############################################################################

def init_CytonBoard():
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
        board.config_board("//")
        BoardMode = board.config_board("/")
        print(BoardMode)
    elif session == "PPG":
        board.config_board("/2")
        BoardMode = board.config_board("/")
        print(BoardMode)
    elif session == 'Impedance':
        Version = board.config_board("V")
        print(Version)
        #Configure Board for Impedance Measurement
        board.config_board("z 2 0 1 Z")
        time.sleep(1)
        BoardMode = "Impedance Check"
        print(BoardMode)
        
    #Start Data Stream of Cyton Board into Ringbuffer
    board.start_stream()
    
def stopDataStream(board):
    #Stop Streaming Session
    board.stop_stream()
    #Release all Ressources
    board.release_session()
    
    
