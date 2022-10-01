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


global path,start,right,left,test
#%% Start Algorithm
###############################################################################
############################### Start Settings ################################
###############################################################################
def init_settings():
    global path,start,right,left,test
    path = "C:/Biomedizinische Informationstechnik/BCI-Projekt Arbeit/Code/BachelorarbeitTobias/Bilder/Experiment"
    start = "Anfang.png" 
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

#%% Create Layouts
#################################################
#################### Layouts ####################
#################################################
    
#Create Main Window Layout
def make_window_menu():
    layout = [    
       [sg.Button("Testaufnahme")],
       [sg.Button("Trainingsaufnahme")],
       [sg.Button("Klassifikationsaufnahme")],
       [sg.Button("EXIT")]
       ]
    window = sg.Window("Training endmode", layout)
    
    return window


#Create Layout for Test Sequence
def make_testsequence_window_():
    layout = [
        [sg.Image(path+start)]
        ]    
    window = sg.Window("Testaufnahme", layout).Finalize()
    window.Maximize()
    
    return window


def make_trainingsession_window():
    ###Missing Code
    a=1
    
def make_classificationsession_window():
    ### Missing Code
    a=1
    