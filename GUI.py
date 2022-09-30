# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 2022

@author: Lennart Brakelmann
"""
#%%Packages
import keyboard
import numpy as np
import random
import PySimpleGUI as sg
import matplotlib.pyplot as plt

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from pylsl import StreamInfo, StreamOutlet
from scipy import signal

#################################################
#################### Layouts ####################
#################################################
#%% Create Layouts

#Create Main Window Layout
def make_window_menu():
    layout = [    
       [sg.Button("Testaufnahme")],
       [sg.Button("EXIT")]
       ]
    window = sg.Window("Training endmode", layout)
    
    return window


#Create Layout for Test Sequence
def make_window_testing():
    layout = [
        [sg.Image(path+sleep_img)]
        ]    
    window = sg.Window("Testaufnahme", layout).Finalize()
    window.Maximize()
    
    return window


#%% Start Algorithm
###############################################################################
############################### Start Settings ################################
###############################################################################
path = "C:\Biomedizinische Informationstechnik\BCI-Projekt Arbeit\Code\BachelorarbeitTobias\Bilder"
sleep_img = "Anfang.png" 
right = ["Rechts1.png",
        "Rechts2.png",
        "Rechts3.png",
        "Rechts4.png"] 
left = ["Links1.png",
        "Links2.png",
        "Links3.png",
        "Links4.png"] 
test = ["Test_Ruhe0.png",
        "Test_Ruhe1.png",
        "Test_Ruhe2.png",
        "Test_Ruhe3.png",
        "Test_Aktion.png"]
###############################################################################
############################### Start Algorithm ###############################
###############################################################################        

window_menu = make_window_menu()
event_menu, values_menu = window_menu.read()