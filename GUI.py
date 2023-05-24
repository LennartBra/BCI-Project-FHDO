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
        self.training = ["TrainingSignMove.png",
                         "TrainingSign1Left.png",
                         "TrainingSign2Left.png",
                         "TrainingSign3Left.png",
                         "TrainingSign1Right.png",
                         "TrainingSign2Right.png",
                         "TrainingSign3Right.png",
                         "PrepareForRecording.png"]
        self.test = ["TrainingSignMove.png",
                         "TestSign1.png",
                         "TestSign2.png",
                         "TestSign3.png"]
        self.pause = ["PauseSign.png"]
        self.instructions = ["Instructions_cut.png"]
        
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
           [sg.Text("The training session will be used to generate training data for the machine learning algorithm. During the training process you have the task to make a clench with your right and your left hand alternately. Once you press the Button below, the recording session",background_color="white",text_color="black")],
           [sg.Text("starts and then you have 4 seconds to prepare for the recording session. After the preparation phase a countdown appears and at the end of the countdown you will be asked to make a clench with the predetermined hand. You have two seconds to perform the",background_color="white",text_color="black")],
           [sg.Text("clench with your hand. After each clench you get a pause of 4 seconds and then the next countdown starts. The GUI always visualizes which hand you have to use to make the clench. In the pictures below you can see an example of the visualization in the GUI.",background_color="white",text_color="black")],
           [sg.Image(self.path+self.instructions[0])],
           [sg.Button("Start Training Session",button_color="orange",size=(30,2))],
           ]
        window = sg.Window("Training Session EEG - Instructions", layout).Finalize()
        
        return window
    
    #Create Layout for EEG Classification Session
    def make_classification_window_instructions_eeg(self):
        layout = [
           [sg.Text("Instructions:",background_color="white",text_color="black")],
           [sg.Text("The training session will be used to generate training data for the machine learning algorithm. During the training process you have the task to make a clench with your right and your left hand alternately. Once you press the Button below, the recording session",background_color="white",text_color="black")],
           [sg.Text("The Classification Session will be used to test the trained classifier. During the classification session you will be asked to image a clench with your right or left hand. You decide with which hand you want to imagine the movement. After the imagination of the",background_color="white",text_color="black")],
           [sg.Text("of the movement you need to label your movement. If you imagined a movement with your left hand press 'q',if you imagined the movement with your right hand press 'ü'. 10 Movements will be recorded for the test session. ",background_color="white",text_color="black")],
           #[sg.Image(self.path+self.instructions[0])],
           [sg.Button("Start Classification Session",button_color="orange",size=(30,2))],
           ]
        window = sg.Window("Classification Session EEG - Instructions", layout).Finalize()
        
        return window

    #Create Layout for EEG Training Session
    def make_training_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.training[7],key='-EEG-Training-')]
            ]    
        window = sg.Window("Training Session EEG - Recording", layout).Finalize()
        
        return window
    
    #Create Layout for EEG Classification Session
    def make_classification_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.training[7],key='-EEG-Classification-')]
            ]    
        window = sg.Window("Classification Session EEG - Recording", layout).Finalize()
        
        return window
        