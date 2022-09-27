# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:28:09 2022

@author: Lennart Brakelmann
"""
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

#################################################
#################### Layouts ####################
#################################################
#%% Create Layouts
def make_window_trainingsession():
    layout = [
        #[sg.Text("Testaufnahme", justification="center")],
        [sg.Image(path+sleep_img, key="-IMAGE-")]
        ]
    window = sg.Window("Trainingsphase", layout).Finalize()
    window.Maximize()
    
    return window

### Layout für die Wahl der Trainingssession
def make_window_training_end():
    layout = [  
        [sg.Text("Please choose the trainings session")],
        [sg.Button("Session No.1")],   
        [sg.Button("Session No.2")],  
        [sg.Button("Session No.3")]
        ]
    window = sg.Window("Training endmode", layout)

    return window

### Layout für den Beginn der Testaufnahme
def make_window_testing():
    layout = [
        [sg.Image(path+sleep_img)]
        ]    
    window = sg.Window("Testaufnahme", layout).Finalize()
    window.Maximize()
    
    return window

### Layout für Beginn der Testphase
def make_window_testsession():
    layout = [
        [sg.Push(),sg.Text("Anzahl MI-Links:"), sg.Text("0", key="-LEFT-"),sg.Push()],
        [sg.Push(),sg.Text("Anzahl MI-Rechts:"), sg.Text("0", key="-RIGHT-"),sg.Push()],
        [sg.Push(),sg.Text("Vorbereitung",key="-STATUS-"),sg.Push()],
        [sg.Push(),sg.Image(path+test[0], key="-IMAGE-"),sg.Push()]
        ]    
    window = sg.Window("Testphase", layout).Finalize()
    window.Maximize()
    
    return window

### Layout für den Überblick - Wahl des Modus von hier aus möglich
def make_window_menu():
    layout = [    
       [sg.Button("Testaufnahme")],
       [sg.Button("Trainingsphase")],   
       [sg.Button("Testphase")], 
       [sg.Button("EXIT")]
       ]
    window = sg.Window("Training endmode", layout)
    
    return window

