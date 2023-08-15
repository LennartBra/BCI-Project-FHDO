# -*- coding: utf-8 -*-
"""
GUI.py

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
                     "TestSign1.png",
                     "TestSign2.png",
                     "TestSign3.png"]
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
               [sg.Button("Impedance Check",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Test Sequence EEG",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Test Sequence PPG",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Training Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("Classification Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
               [sg.Button("EXIT",button_color="red",size=(30,2),font=("Helvetica",11))]],
               background_color = "white", element_justification="center",justification="center"
               )]
               ]
        window = sg.Window("Main Window", layout,background_color="white").Finalize()
        
        return window
 
    #Create Layout for Impedance Check
    def make_impedance_window(self):
        layout = [
            [sg.Column([
                [sg.Image(self.path+self.play[0],key='-Impedance-')]],
                background_color = "white",vertical_alignment='center', element_justification="center",justification="center"
                )] 
            ]
        window = sg.Window("Impedance Check", layout, background_color="white").Finalize()
        window.Maximize()
        
        return window
    
    
    #Create Layout for EEG Test Sequence
    def make_testsequence_window_eeg(self):
        layout = [
            [sg.Column([
                [sg.Image(self.path+self.play[0],key='-EEG-')]],
                background_color = "white",vertical_alignment='center', element_justification="center",justification="center"
                )] 
            ]
        window = sg.Window("Test Sequence EEG", layout, background_color="white").Finalize()
        window.Maximize()
        
        return window
    
    #Create Layout for PPG Test Sequence
    def make_testsequence_window_ppg(self):
        layout = [
            [sg.Column([
                [sg.Image(self.path+self.play[0],key='-PPG-')]],
                background_color = "white",vertical_alignment='center', element_justification="center",justification="center"
                )] 
            ]
        window = sg.Window("Test Sequence PPG", layout, background_color="white").Finalize()
        window.Maximize()
        
        return window
    
    
    def make_training_window_instructions_eeg(self):
        Training_Column = [
            [sg.Text("Training Session",background_color="white",text_color="black",font=("Helvetica",25))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Instructions:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("This Brain Computer Interface application focuses on Motor Imagery Movement (MIM) and has the target to distinguish between MIM of the left and the right hand. The training",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("session will be used to generate training data for the machine learning algorithm. During the training process you have the task to imagine a clench with your right and",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("left hand. The algorithm randomly predetermines which hand you need to use for the imagination of the clench. In total the program will record 60 MIMs, that means",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("30 trials per hand. The training session is divided into 3 parts with 20 Motor Imagery Movements. That means that you will get a pause after 20 MIMs and after 40 MIMs",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("have been recorded. Once you press the 'Start Training Session' button below, the recording session starts with a preparation phase that takes 30 seconds. The",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("preparation phase is needed because the acquisition of the EEG data needs some time to stabilize. After the preparation phase the recording of the training data starts.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Before each Imagery Movement you will see a countdown that visualizes when you have to imagine the clench. You always have 4 seconds to perform the imagination",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("of the clench with the predetermined hand. After each MIM you get a pause of 4 seconds and then the countdown for the next trial starts.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("GUI visualization:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("The GUI always visualizes which hand you have to use to make the clench. In the pictures below you can see an example of the visualization in the GUI.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Image(self.path+self.instructions[0])],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Button("Start Training Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
            ]
        layout = [
           [sg.Column(Training_Column,background_color="white",element_justification="center",justification="center")],
           ]
        window = sg.Window("Training Session EEG - Instructions", layout,background_color="white").Finalize()
        window.Maximize()
        
        return window
    
    #Create Layout for EEG Classification Session
    def make_classification_window_instructions_eeg(self):
        Classification_Column = [
            [sg.Text("Classification Session",background_color="white",text_color="black",font=("Helvetica",25))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Instructions:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("The Classification Session will be used to test the trained classifier. During the classification session you will be asked to image a clench with your right and left",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("hand. For the classification session you decide which hand to use for the imagination of the clench. Once the countdown has disapperaed and you see the 'Play'",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Instruction you will have 4 seconds to perform the Motor Imagery Movement (MIM). After the imagination of the clench you need to label the MIM. If you imagined a",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("clench with your left hand press 'q', if you imagined the clench with your right hand press 'ü'. You need to perform 15 MIMs in order to complete the Classification",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Session. After you have completed all MIMs you will be directed to the Result Window, where you can see the Overall Accuracy and the results for every single trial.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("GUI visualization:",background_color="white",text_color="black",font=("Helvetica",20))],
            [sg.Text("Down below you can see an example of the visualization for the tasks in the GUI. The visualization is similar to the Training Session.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Image(self.path+self.instructions[1])],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Button("Start Classification Session",button_color="orange",size=(30,2),font=("Helvetica",11))],
            ]
        layout = [
           [sg.Column(Classification_Column,background_color="white",justification="center",element_justification="center")],
           ]
        window = sg.Window("Classification Session EEG - Instructions", layout,background_color="white").Finalize()
        window.Maximize()
        
        return window

    
    def make_training_window_eeg(self,n):
        trial = n+1
        layout = [
            [sg.Column([
                [sg.Text("Trial:",background_color="white",text_color="black",font=("Helvetica",11)),sg.Text(trial,key ='Training-Trial',background_color="white",text_color="black",font=("Helvetica",11))],
                [sg.Image(self.path+self.training[7],key='-EEG-Training-')]],
                background_color = "white",vertical_alignment='center', element_justification="center",justification="center"
                )]
            ]    
        window = sg.Window("Training Session EEG - Recording", layout, background_color="white").Finalize()
        window.Maximize()
        
        return window
    
    def make_pause_window(self):
        Pause_Column = [
            [sg.Text("Pause Window",background_color="white",text_color="black",font=("Helvetica",25))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("Now you have the time to take a break from the recording of the training data.",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text(" Please press the 'Continue Recording' button below to continue the Training Session",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Text("",background_color="white",text_color="black",font=("Helvetica",11))],
            [sg.Button("Continue Recording",button_color="orange",size=(30,2),font=("Helvetica",11))],
            ]
        layout = [
           [sg.Column(Pause_Column,background_color="white",element_justification="center",justification="center")],
           ]
        window = sg.Window("Training Session EEG - Pause Window", layout,background_color="white").Finalize()
        
        return window
    

    def make_classification_window_eeg(self):
        start = 0
        layout = [
            [sg.Column([
                [sg.Text("MI Left Hand:",background_color="white",text_color="black",font=("Helvetica",11)),sg.Text(start,key='Test-Trial-Left',background_color="white",text_color="black",font=("Helvetica",11))],
                [sg.Text("MI Right Hand:",background_color="white",text_color="black",font=("Helvetica",11)),sg.Text(start,key='Test-Trial-Right',background_color="white",text_color="black",font=("Helvetica",11))],
                [sg.Image(self.path+self.training[7],key='-EEG-Classification-')]],
                background_color = "white",vertical_alignment='center', element_justification="center",justification="center"
                )]
            ]    
        window = sg.Window("Classification Session EEG - Recording", layout, background_color="white").Finalize()
        window.Maximize()
        
        return window
    
    #Create Test Result Window
    def make_result_window(self,y_true, y_pred, Acc):
        Results = []
        for i in range(0,len(y_true)):
            if y_true[i] == y_pred[i]:
                Results.append(1)
            else:
                Results.append(0)
        Trials_List = list(range(1,len(y_true)+1))
        y_true_List = list(y_true)
        y_pred_List = list(y_pred)
        
        layout = [
            [sg.Column(
                [
                [sg.Text("Results",background_color="white",text_color="black",font=("Helvetica",24))],
                [sg.Text("You have now completed the Classification Session. Down below you can see your Result for each test trial and the overall resulting Accuracy.",font=("Helvetica",11),background_color="white",text_color="black")],
                [sg.Text("",background_color="white")],
                [sg.Text("Trial results:",background_color="white",text_color="black",font=("Helvetica",14))],
                [sg.Text("0 = Motor Imagery Movement of the left hand, 1 = Motor Imagery Movement of the right hand",font=("Helvetica",11),background_color="white",text_color="black")],
                [sg.Text("      Trial:           Prediction:     True Label:",background_color="white",text_color="black",font=("Helvetica",9))],
                [sg.Listbox(Trials_List,size=(7,15),no_scrollbar=True,background_color="white"),
                 sg.VSeperator(),
                 sg.Listbox(y_pred_List,size=(7,15),no_scrollbar=True,background_color="white"),
                 sg.VSeperator(),
                 sg.Listbox(y_true_List,size=(7,15),no_scrollbar=True,background_color="white")
                ],
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
    
    
    
    
    
    
    
    #Create Test Result Window
    def make_result_window2(self,y_true, y_pred, Acc):
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
                [sg.Text("0 = Motor Imagery Movement of the left hand, 1 = Motor Imagery Movement of the right hand",font=("Helvetica",11),background_color="white",text_color="black")],
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
    
    