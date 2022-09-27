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
####################### Preparing Cyton Board #########################
### Kommunikation mit CytonBoard aufnehmen
### BranFlow Logger aktivieren mit Level TRACE --> Log Nachrichten
BoardShim.enable_dev_board_logger()
###BrainflowInputParams Objekt erstellen
params = BrainFlowInputParams()
### Serial Port definieren
params.serial_port = 'COM3'
### Board initialisieren --> CytonBoard mit Parametern
board = BoardShim(BoardIds.CYTON_BOARD.value, params)
### Sampling Rate abgreifen von Board
srate = board.get_sampling_rate(BoardIds.CYTON_BOARD.value)
### Streaming Session vorbereiten, Ressourcen initialisieren
### prepare_session muss vor allen BoardShim Objektmethoden aufgerufen werden
board.prepare_session()
### Datenstream des Cyton Boards starten --> Daten in Ringbuffer abspeichern
board.start_stream()
### Liste der EEG-Channel ausgeben
eeg_chan = BoardShim.get_eeg_channels(BoardIds.CYTON_BOARD.value)