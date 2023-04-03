# -*- coding: utf-8 -*-
"""
Class for GUI
"""
#%%Import PySimpleGUI Package
import PySimpleGUI as sg


#%% Start Algorithm
class GUI:
    
    #Create GUI Object with Pictures as attributes
    def __init__(self):        
        self.path = "Pictures/"
        self.play = ["Play.png",
                     "PlaySign1.png",
                     "PlaySign2.png",
                     "PlaySign3.png"]
        self.stop = ["StopSign.png",
                "StopSign2.png",
                "StopSign3.png"]
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
     
    #Create Layout for EEG Test Sequence
    def make_testsequence_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.play[0],key='-EEG-')]
            ]    
        window = sg.Window("Test Sequence EEG", layout).Finalize()
        
        return window
    
    #Create Layout for PPG Test Sequence
    def make_testsequence_window_ppg(self):
        layout = [
            [sg.Image(self.path+self.play[0],key='-PPG-')]
            ]    
        window = sg.Window("Test Sequence PPG", layout).Finalize()
        
        return window
    
    #Create Layout for EEG Training Session
    def make_training_window_instructions_eeg(self):
        layout = [
           [sg.Text("Instructions:",background_color="white",text_color="black")],
           [sg.Text("The ...",background_color="white",text_color="black")],
           [sg.Button("Start Training Session",button_color="orange",size=(30,2))],
           ]
        window = sg.Window("Training Session EEG - Instructions", layout).Finalize()
        
        return window

    #Create Layout for EEG Training Session
    def make_training_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.play[0],key='-EEG-Training-')]
            ]    
        window = sg.Window("Training Session EEG - Recording", layout).Finalize()
        
        return window
        