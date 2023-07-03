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
        self.pause = ["PauseSign.png",
                      "Pause_LabelSign.png"]
        self.instructions = ["TrainingInstructions.png",
                             "TestInstructions.png"]
        self.logo = ["FHDoLogo_Resized.png"]
        
    #################################################
    #################### Layouts ####################
    #################################################
    
    def make_window_menu(self):
        layout = [
           [sg.Column(
               [[sg.Image(self.path+self.logo[0],'center',key='-Logo-')],
               [sg.Text("",justification="center",background_color="white",text_color="black",font=("Helvetica",11))],
               [sg.Text("BCI Demonstrator for Motor Imagery",justification="center",background_color="white",text_color="black",font=("Helvetica",16))],
               [sg.Text("",justification="center",background_color="white",text_color="black",font=("Helvetica",11))],
               [sg.Text("Please choose a Session:",justification="center",background_color="white",text_color="black",font=("Helvetica",11))],
               [sg.Button("Test Sequence EEG",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Test Sequence PPG",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Training Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Classification Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("EXIT",button_color="red",size=(30,2),font=("Helvetica",11))]],
               background_color = "white", element_justification="center"
               )]
               ]
        window = sg.Window("Main Window", layout,background_color="white").Finalize()
        
        return window
     
    #Create Layout for EEG Test Sequence
    def make_testsequence_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.play[0],key='-EEG-')]
            ]    
        window = sg.Window("Test Sequence EEG", layout, background_color="white").Finalize()
        
        return window
    
    #Create Layout for PPG Test Sequence
    def make_testsequence_window_ppg(self):
        layout = [
            [sg.Image(self.path+self.play[0],key='-PPG-')]
            ]    
        window = sg.Window("Test Sequence PPG", layout, background_color="white").Finalize()
        
        return window
    
    #Create Layout for EEG Training Session
    def make_training_window_instructions_eeg(self):
        layout = [
           [sg.Text("Instructions:",background_color="white",text_color="black",font=("Helvetica",20))],
           [sg.Text("This Brain Computer Interface application focuses on Motor Imagery Movement and has the target to distinguish between Motor Imagery Movement of the left and the right hand.",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("The training session will be used to generate training data for the machine learning algorithm. During the training process you have the task to imagine a clench with your",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("right and your left hand. The algorithm randomly predetermines which hand you need to use for the imagination of the clench. In total the program will record 40 Motor",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("Imagery Movements, that means 20 trials per hand. Once you press the 'Start Training Session' button below, the recording session starts with a preparation phase that",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("takes 30 seconds. The preparation phase is needed because the acquisition of the EEG data needs some time to stabilize. After the preparation phase the recording of the",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("training data starts. Before each Imagery Movement you will see a countdown that visualizes when you have to imagine the clench. You always have 4 seconds to perform the",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("imagination of the clench with the predetermined hand. After each clench you get a pause of 4 seconds and then the countdown for the next trial starts.",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("GUI visualization:",background_color="white",text_color="black",font=("Helvetica",20))],
           [sg.Text("The GUI always visualizes which hand you have to use to make the clench. In the pictures below you can see an example of the visualization in the GUI.",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Image(self.path+self.instructions[0])],
           [sg.Button("Start Training Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
           ]
        window = sg.Window("Training Session EEG - Instructions", layout,background_color="white").Finalize()
        
        return window
    
    def make_training_window_instructions_eeg2(self):
        Training_Column = [
            [sg.Text("Training Session",background_color="white",text_color="black",font=("Helvetica",25))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Instructions:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("This Brain Computer Interface application focuses on Motor Imagery Movement and has the target to distinguish between Motor Imagery Movement of the left and the right hand.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("The training session will be used to generate training data for the machine learning algorithm. During the training process you have the task to imagine a clench with your",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("right and your left hand. The algorithm randomly predetermines which hand you need to use for the imagination of the clench. In total the program will record 40 Motor",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Imagery Movements, that means 20 trials per hand. Once you press the 'Start Training Session' button below, the recording session starts with a preparation phase that",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("takes 30 seconds. The preparation phase is needed because the acquisition of the EEG data needs some time to stabilize. After the preparation phase the recording of the",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("training data starts. Before each Imagery Movement you will see a countdown that visualizes when you have to imagine the clench. You always have 4 seconds to perform the",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("imagination of the clench with the predetermined hand. After each clench you get a pause of 4 seconds and then the countdown for the next trial starts.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("GUI visualization:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("The GUI always visualizes which hand you have to use to make the clench. In the pictures below you can see an example of the visualization in the GUI.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Image(self.path+self.instructions[0])],
            [sg.Button("Start Training Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
            ]
        layout = [
           [sg.Column(Training_Column,background_color="white",element_justification="center")],
           ]
        window = sg.Window("Training Session EEG - Instructions", layout,background_color="white").Finalize()
        
        return window
    
    #Create Layout for EEG Classification Session
    def make_classification_window_instructions_eeg(self):
        layout = [
           [sg.Text("Instructions:",background_color="white",text_color="black",font=("Helvetica",20))],
           [sg.Text("The Classification Session will be used to test the trained classifier. During the classification session you will be asked to image a clench with your right or left",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("hand. For the classification session you decide which hand to use for the imagination of the clench. Once you see the 'Move Now' Instruction you will have 4 seconds",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("for the imagination of the task. After the imagination of the movement you need to label your movement. If you imagined a movement with your left hand press 'q',",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("if you imagined the movement with your right hand press 'ü'. You need to absolve 10 Motor Imagery Movements in order to complete the Classification Session.",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("After you have completed all movements you will be directed to the Result Window, where you can see the Overall Accuracy and the results for every single trial.",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Text("GUI visualization:",background_color="white",text_color="black",font=("Helvetica",20))],
           [sg.Text("Down below you can see an example of the visualization for the tasks in the GUI. The visualization is similar to the Training Session.",background_color="white",text_color="black",font=("Helvetica",11))],
           [sg.Image(self.path+self.instructions[1])],
           [sg.Button("Start Classification Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
           ]
        window = sg.Window("Classification Session EEG - Instructions", layout,background_color="white").Finalize()
        
        return window
    
    #Create Layout for EEG Classification Session
    def make_classification_window_instructions_eeg2(self):
        Classification_Column = [
            [sg.Text("Classification Session",background_color="white",text_color="black",font=("Helvetica",25))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Instructions:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("The Classification Session will be used to test the trained classifier. During the classification session you will be asked to image a clench with your right or left",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("hand. For the classification session you decide which hand to use for the imagination of the clench. Once you see the 'Move Now' Instruction you will have 4 seconds",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("for the imagination of the task. After the imagination of the movement you need to label your movement. If you imagined a movement with your left hand press 'q',",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("if you imagined the movement with your right hand press 'ü'. You need to absolve 10 Motor Imagery Movements in order to complete the Classification Session.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("After you have completed all movements you will be directed to the Result Window, where you can see the Overall Accuracy and the results for every single trial.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("GUI visualization:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("Down below you can see an example of the visualization for the tasks in the GUI. The visualization is similar to the Training Session.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Image(self.path+self.instructions[1])],
            [sg.Button("Start Classification Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
            ]
        layout = [
           [sg.Column(Classification_Column,background_color="white",element_justification="center")],
           ]
        window = sg.Window("Classification Session EEG - Instructions", layout,background_color="white").Finalize()

        return window

    #Create Layout for EEG Training Session
    def make_training_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.training[7],key='-EEG-Training-')]
            ]    
        window = sg.Window("Training Session EEG - Recording", layout, background_color="white").Finalize()
        
        return window
    
    #Create Layout for EEG Classification Session
    def make_classification_window_eeg(self):
        layout = [
            [sg.Image(self.path+self.training[7],key='-EEG-Classification-')]
            ]    
        window = sg.Window("Classification Session EEG - Recording", layout, background_color="white").Finalize()
        
        return window
    
    
    #Create Test Result Window
    def make_result_window(self,y_true, y_pred, Acc):
        Results = []
        for i in range(0,len(y_true)):
            if y_true[i] == y_pred[i]:
                Results.append(1)
            else:
                Results.append(0)
        Trials = range(1,len(y_true)+1)
        Row_Names = [
            [sg.Text("Trial",font=("Helvetica",11),background_color="white",text_color="black")],
            [sg.Text("Prediction",font=("Helvetica",11),background_color="white",text_color="black")],
            [sg.Text("True Label",font=("Helvetica",11),background_color="white",text_color="black")],
            ]
        Result_Column = [
            [sg.Text(Trials[i],font=("Helvetica",11),background_color="white",text_color="black") for i in range(0,len(y_true))],
            [sg.Text(y_pred[i],font=("Helvetica",11),background_color="white",text_color="black") for i in range(0,len(y_true))],
            [sg.Text(y_true[i],font=("Helvetica",11),background_color="white",text_color="black") for i in range(0,len(y_true))],
            ]
        
        layout = [
            [sg.Column(
                [
                [sg.Text("Results",background_color="white",text_color="black",font=("Helvetica",24))],
                [sg.Text("You have now completed the Classification Session. Down below you can see your Result for each test trial and the overall resulting Accuracy.",font=("Helvetica",11),background_color="white",text_color="black")],
                [sg.Text("",background_color="white")],
                [sg.Text("Trial results:",background_color="white",text_color="black",font=("Helvetica",14))],
                [sg.Column(Row_Names,background_color="white",element_justification="center"),
                 sg.VSeperator(),
                 sg.Column(Result_Column,background_color="white")],
                [sg.Text("",background_color="white")],
                [sg.Text("Overall Accuracy:",font=("Helvetica",14),background_color="white",text_color="black")],
                [sg.Text(Acc,background_color="white",text_color="black")],
                [sg.Button("Main Menu",button_color="red",size=(30,2),font=("Helvetica",11))],
                ],
                background_color = "white", element_justification="center"
            )],
            ]
        
                   
        window = sg.Window("Result Window", layout,background_color="white").Finalize()
        
        return window