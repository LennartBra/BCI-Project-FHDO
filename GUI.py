# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 2022

@author: Lennart Brakelmann
Class for GUI
"""
#%%Import Package
import PySimpleGUI as sg


#%% Start Algorithm
class GUI:
    ###############################################################################
    ############################### Start Settings ################################
    ###############################################################################
    def __init__(self):
        self.path = "C:/Biomedizinische Informationstechnik/BCI-Projekt Arbeit/Code/BachelorarbeitTobias/Bilder/Experiment"
        self.start = "Anfang.png" 
        self.right = ["Rechts1.png",
                 "Rechts2.png",
                 "Rechts3.png",
                 "Rechts4.png"] 
        self.left = ["Links1.png",
                "Links2.png",
                "Links3.png",
                "Links4.png"] 
        self.test = ["Test_Ruhe0.png",
                "Test_Ruhe1.png",
                "Test_Ruhe2.png",
                "Test_Ruhe3.png",
                "Test_Aktion.png"]
        self.logo = "C:/Biomedizinische Informationstechnik/BCI-Projekt Arbeit/Code/BachelorarbeitTobias/Bilder/ExperimentFHDoLogo.png"
    
    #%% Create Layouts
    #################################################
    #################### Layouts ####################
    #################################################
        
    #Create Main Window Layout
    def make_window_menu(self):
        layout = [
           [sg.Text("Please choose a Session:",background_color="white",text_color="black")],
           [sg.Button("Test Sequence EEG",button_color="orange",size=(30,2))],
           [sg.Button("Test Sequence PPG",button_color="orange",size=(30,2))],
           [sg.Button("Training Session",button_color="orange",size=(30,2))],
           [sg.Button("Classification Session",button_color="orange",size=(30,2))],
           [sg.Button("EXIT",button_color="red",size=(30,2))]
           ]
        window = sg.Window("Main Window", layout,background_color="white")
        
        return window
     
    #Create Layout for Test Sequence
    def make_testsequence_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.start,key='-EEG-')]
            ]    
        window = sg.Window("Test Sequence EEG", layout).Finalize()
        window.Maximize()
        
        return window
    
    def make_testsequence_window_ppg(self):
        layout = [
            [sg.Image(self.path+self.start,key='PPG')]
            ]    
        window = sg.Window("Test Sequence PPG", layout).Finalize()
        window.Maximize()
        
        return window
    
        