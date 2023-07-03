# -*- coding: utf-8 -*-
"""
Main script for Data Acquisition
"""

#%% Start Algorithm - Create GUI
#Import Packages
import numpy as np
from GUI import GUI
from ProcessData import Data
import ProcessData as PD
import CommunicationCytonBoard as CCB
import PySimpleGUI as sg
import matplotlib.pyplot as plt
# pyriemann
from pyriemann.estimation import XdawnCovariances
#sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
#Vecotrizer
from mne.decoding import Vectorizer
#Keyboard
import keyboard
from scipy import signal
#time
import time
#random
import random

#%matplotlib qt


#Set variables for Training and Classification
Movement_Duration = 4 #Time to execute movement/ imagine movement
Training_Trials = 20 #50 in total, 25 per side
Test_Trials = 10
OneSec = 250 

#Create Object of Class GUI
GUI = GUI()
#Create Main Window
window_menu = GUI.make_window_menu()
event_menu, values_menu = window_menu.read() 


###############################################################################
################################Check GUI Status###############################
###############################################################################

while True:
    
    if window_menu == sg.WIN_CLOSED or event_menu == "EXIT":
        window_menu.close()
        event_menu = None
        
        break
  
    if event_menu == "Test Sequence EEG":
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"EEG")
        
        #Close Main Window
        window_menu.close()
        
        #Create Arrays for EEG_Data
        eegchunk = []
        EEG = []
        #Create TestSequence Window
        window_testsequence_eeg = GUI.make_testsequence_window_eeg()
              
        ###################
        # Start Algorithm #
        ###################
        while True:            
            #Monitoring window status
            event_testsequence_eeg , values_testsequence_eeg = window_testsequence_eeg.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
            
            if event_testsequence_eeg == sg.WIN_CLOSED or len(EEG) > 5000:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_testsequence_eeg = None
                #Close Test Sequence Window
                window_testsequence_eeg.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                #Make EEG NumPy Array --> Rows = , Channels =
                EEG = np.array(EEG)
                EEG = np.transpose(EEG)
                
                break
            
            if len(EEG) > 4250:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[3])
            if len(EEG) > 4500:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[2])
            if len(EEG) > 4750:
                window_testsequence_eeg["-EEG-"].update(filename=GUI.path+GUI.play[1])
                
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                eegchunk = data[eeg_chan]
                #print("Laenge Chunk",len(eegchunk[0]),"Buffer Count",buffer_count)
                #Save eegchunk in EEG
                EEG = PD.process_eegchunk(eegchunk,EEG)
                
    if event_menu == "Test Sequence PPG":     
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
        
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"PPG")
        
        #Close Main Window
        window_menu.close()
        
        
        #Create Arrays for PPG Data
        ppgchunk = []
        PPG = []
        #Create TestSequence Window
        window_testsequence_ppg = GUI.make_testsequence_window_ppg()
        
        ###################
        # Start Algorithm #
        ###################
        while True:            
            #Monitoring window status
            event_testsequence_ppg , values_testsequence_ppg = window_testsequence_ppg.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
            
            if event_testsequence_ppg == sg.WIN_CLOSED or len(PPG) > 2500:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_testsequence 
                event_testsequence_ppg = None
                #Close Test Sequence Window
                window_testsequence_ppg.close()
                #Make PPG NumPy Array
                PPG = np.array(PPG)
                PPG = np.transpose(PPG)
                #Invert PPG
                PPG = -PPG
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                
                break
            
            if len(PPG) > 1750:
                window_testsequence_ppg["-PPG-"].update(filename=GUI.path+GUI.play[3])
            if len(PPG) > 2000:
                window_testsequence_ppg["-PPG-"].update(filename=GUI.path+GUI.play[2])
            if len(PPG) > 2250:
                window_testsequence_ppg["-PPG-"].update(filename=GUI.path+GUI.play[1])
                
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into ppgchunk
                ppgchunk = data[ppg_chan]

                #Save ppgchunk in PPG
                PPG = PD.process_ppgchunk(ppgchunk,PPG)

    if event_menu == "Training Session": 
        #Close Main Window
        window_menu.close()
        #Create Instruction Window for Training Session
        training_window_instructions = GUI.make_training_window_instructions_eeg2()
            
        #Create Arrays for EEG_Data
        eegchunk = []
        EEG = []
        EEG_temp = []
        time_stamps = []
        training_labels = []
        TimeStampCheck = False
        n = 0
        instruction_window_status = False
        StabilizedData = False
        Training_Order = PD.make_random_order(Training_Trials)
        
        while True:
            #Monitoring window status --> Start of Training Session
            event_training_window_instructions , values_training_window_instructions = training_window_instructions.read(timeout=4)
            
            if event_training_window_instructions == 'Start Training Session':
                break
            if event_training_window_instructions == sg.WIN_CLOSED:
                training_window_instructions.close()
                instruction_window_status = True
                break
        
        if instruction_window_status == True:
            window_menu = GUI.make_window_menu()
            event_menu, values_menu = window_menu.read()
            continue
            
            
        #Close Instruction Window
        training_window_instructions.close()
        
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
        
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"EEG")
        
        #Create Recording Window
        training_window = GUI.make_training_window_eeg()
        
        while True:
            #Monitoring Window Status
            event_training_window, values_training_window = training_window.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
        
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                eegchunk = data[eeg_chan]
                #Save eegchunk in EEG
                EEG = PD.process_eegchunk(eegchunk,EEG)
                EEG_temp = PD.process_eegchunk(eegchunk,EEG_temp)
            
            if StabilizedData == False and len(EEG_temp) > OneSec * 30:
                StabilizedData = True
                EEG_temp = []
                
            
            #Even Numbers --> Left Hand --> 0, Odd Numbers --> Right Hand --> 1
            if StabilizedData == True and len(EEG_temp) > OneSec*4:
                if Training_Order[n] == 0:
                    training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[3])
                else:
                    training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[6])
            if StabilizedData == True and len(EEG_temp) > OneSec*5:
                if Training_Order[n] == 0:
                    training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[2])
                else:
                    training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[5])
            if StabilizedData == True and len(EEG_temp) > OneSec*6:
                if Training_Order[n] == 0:
                    training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[1])
                else:
                    training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[4])
            if StabilizedData == True and len(EEG_temp) > OneSec*7:
                if TimeStampCheck == False:
                    time_stamps.append(len(EEG))
                    TimeStampCheck = True
                    if Training_Order[n] == 0:
                        training_labels.append(0)
                    else:
                        training_labels.append(1)
                training_window["-EEG-Training-"].update(filename=GUI.path+GUI.training[0])
            if StabilizedData == True and len(EEG_temp) > OneSec*7 + OneSec*Movement_Duration:
                EEG_temp = []
                training_window["-EEG-Training-"].update(filename=GUI.path+GUI.pause[0])
                n = n+1
                TimeStampCheck = False
            
        
            if event_training_window == sg.WIN_CLOSED: #or n == Training_Trials:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_training_window 
                event_training_window = None
                #Close Test Sequence Window
                training_window.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                #Make EEG NumPy Array --> Rows = Channels, Columns = Measured Values
                EEG = np.array(EEG)
                EEG_Training_Raw = np.transpose(EEG)
                
                break
        
            if n == Training_Trials:
                #Wait for 2 secs
                time.sleep(2)
                #Load data for last time
                data = CytonBoard.get_board_data()
                eegchunk = data[eeg_chan]
                EEG = PD.process_eegchunk(eegchunk,EEG)
                
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_training_window 
                event_training_window = None
                #Make EEG NumPy Array --> Rows = Channels, Columns = Measured Values
                EEG = np.array(EEG)
                EEG_Training_Raw = np.transpose(EEG)
                #Process Data
                channels = ["FC1","C3","FC1", "FC2", "C4", "FC6", "/", "/"]
                EEG_Training = Data(EEG_Training_Raw,channels)
                #Filter EEG
                EEG_Training.filterEEG()
                #Meanfree EEG
                EEG_Training.mean_free_EEG()
                #Make X and y
                X, y = EEG_Training.make_X_and_y(time_stamps, training_labels)
                #Define Classifier
                classifier = LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')
                #Define xDawn algorithm
                xdawn = XdawnCovariances(2,estimator="lwf",xdawn_estimator = "lwf")
                #Transform data with Xdawn
                X_transformed_dawn = xdawn.fit_transform(X,y)
                #Vectorize Data
                vc = Vectorizer()
                X_transformed = vc.fit_transform(X_transformed_dawn)
                #Fit Classifier and Data
                classifier.fit(X_transformed,y)
                
                #Close Test Sequence Window
                training_window.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                
                break        
            
    if event_menu == "Classification Session": 
        #Check if Training Session has been executed before
        if 'classifier' in locals():
            pass
        else:
            #Close Main Window
            window_menu.close()
            sg.popup("Classifier has not been trained yet. Please first execute the Training Session!",background_color="white",button_color="orange",text_color="black")
            #Create Main Window
            window_menu = GUI.make_window_menu()
            event_menu, values_menu = window_menu.read()
            continue
        #Close Main Window
        window_menu.close()
        #Create Instruction Window for Classification Session
        classification_window_instructions = GUI.make_classification_window_instructions_eeg2()

        #Create Arrays for EEG_Data
        eegchunk = []
        EEG = []
        EEG_temp = []
        classification_time_stamps = []
        classification_labels = []
        TimeStampCheck = False
        n = 0
        classification_instruction_window_status = False
        result_window_status = False
        StabilizedData = False
        
        while True:
            #Monitoring window status --> Start of Training Session
            event_classification_window_instructions , values_classification_window_instructions = classification_window_instructions.read(timeout=4)
            
            if event_classification_window_instructions == 'Start Classification Session':
                break
            if event_classification_window_instructions == sg.WIN_CLOSED:
                classification_window_instructions.close()
                classification_instruction_window_status = True
                break
        
        if classification_instruction_window_status == True:
            window_menu = GUI.make_window_menu()
            event_menu, values_menu = window_menu.read()
            continue 
        
        #Close Instruction Window
        classification_window_instructions.close()
        
        #Initialize Cyton Board and get channels
        CytonBoard, eeg_chan, ppg_chan = CCB.init_CytonBoard()
        
        #Start Data Stream
        CCB.startDataStream(CytonBoard,"EEG")
        
        #Create Recording Window
        classification_window = GUI.make_classification_window_eeg()
        
        while True:
            #Monitoring Window Status
            event_classification_window, values_classification_window = classification_window.read(timeout=4)
            #Check Sample Count in Ringbuffer
            buffer_count = CytonBoard.get_board_data_count()
        
            #Load data from Ringbuffer
            if buffer_count > 50:
                #Get Board data from ringbuffer and delete ringbuffer
                data = CytonBoard.get_board_data()
                #Load data Chunk into eegchunk
                eegchunk = data[eeg_chan]
                #Save eegchunk in EEG
                EEG = PD.process_eegchunk(eegchunk,EEG)
                EEG_temp = PD.process_eegchunk(eegchunk,EEG_temp)
            
            #Check if Data has stabilized --> stabilized after 30 secs
            if StabilizedData == False and len(EEG_temp) > OneSec * 30:
                StabilizedData = True
                EEG_temp = []
            
            if StabilizedData == True and len(EEG_temp) > OneSec*4:
                classification_window["-EEG-Classification-"].update(filename=GUI.path+GUI.test[3])
            if StabilizedData == True and len(EEG_temp) > OneSec*5:
                classification_window["-EEG-Classification-"].update(filename=GUI.path+GUI.test[2])
            if StabilizedData == True and len(EEG_temp) > OneSec*6:
                classification_window["-EEG-Classification-"].update(filename=GUI.path+GUI.test[1])
            if StabilizedData and len(EEG_temp) > OneSec*7:
                if TimeStampCheck == False:
                    classification_time_stamps.append(len(EEG))
                    TimeStampCheck = True
                classification_window["-EEG-Classification-"].update(filename=GUI.path+GUI.test[0])
            if StabilizedData == True and len(EEG_temp) > OneSec*7 + OneSec*Movement_Duration:
                classification_window["-EEG-Classification-"].update(filename=GUI.path+GUI.pause[1])
                if keyboard.is_pressed("q"):
                    classification_labels.append(0)
                    n = n+1
                    TimeStampCheck = False
                    EEG_temp = []
                elif keyboard.is_pressed("ü"):
                    classification_labels.append(1)
                    n = n+1
                    TimeStampCheck = False
                    EEG_temp = []
                       
            
            
            if event_classification_window == sg.WIN_CLOSED: #or n == Test_Trials:
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_training_window 
                event_classification_window = None
                #Close Test Sequence Window
                classification_window.close()
                #Create Main Window
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                #Make EEG NumPy Array --> Rows = Channels, Columns = Measured Values
                EEG = np.array(EEG)
                EEG_Test_Raw = np.transpose(EEG)
                
                break

            if n == Test_Trials:
                #Wait for 2 secs
                time.sleep(2)
                #Load data for last time
                data = CytonBoard.get_board_data()
                eegchunk = data[eeg_chan]
                EEG = PD.process_eegchunk(eegchunk,EEG)
                
                #Stop Data Stream
                CCB.stopDataStream(CytonBoard)
                #Reset event_training_window 
                event_classification_window = None
                #Close Test Sequence Window
                classification_window.close()
                #Make EEG NumPy Array --> Rows = Channels, Columns = Measured Values
                EEG = np.array(EEG)
                EEG_Test_Raw = np.transpose(EEG)
                #Process Data
                channels = ["FC1","C3","FC1", "FC2", "C4", "FC6", "/", "/"]
                EEG_Test = Data(EEG_Test_Raw,channels)
                #Filter Test Data
                EEG_Test.filterEEG()
                #Meanfree Test Data
                EEG_Test.mean_free_EEG()
                #Make X_test and y_true
                X_test, y_true = EEG_Test.make_Xtest_and_ytrue(classification_time_stamps, classification_labels)
                #Transform Data with Xdaüqüüqüqqüqwn algorithm
                X_test_transformed_dawn = xdawn.transform(X_test)
                #Vectorize Data
                X_test_transformed = vc.fit_transform(X_test_transformed_dawn)
                #Make predictions for Test Data
                y_pred = classifier.predict(X_test_transformed)
                #Calculate Accuracy
                Acc = accuracy_score(y_true,y_pred)
                #Create Result Window
                result_window = GUI.make_result_window(y_true, y_pred, Acc)
                
                while True:
                    #Monitoring window status
                    event_result_window , values_result_window = result_window.read(timeout=4)
                    
                    if event_result_window == 'Main Menu':
                        result_window.close()
                        break
                    if event_result_window == sg.WIN_CLOSED:
                        result_window.close()
                        break
                    
                window_menu = GUI.make_window_menu()
                event_menu, values_menu = window_menu.read()
                    
                break
            
        
#%%Process EEG Data
channels = ["FC1","C3","FC1", "FC2", "C4", "FC6", "/", "/"]
EEG_TestAufnahme = Data(EEG,channels)
EEG_TestAufnahme.plot_EEG_data()


#%%Process PPG Data
channels = ["19","PPG","21"]
PPG_TestSequence = Data(PPG,channels)
PPG_TestSequence.filterPPG()
PPG_TestSequence.plot_PPG_data()

#%% Training Session
channels = ["FC1","C3","FC1", "FC2", "C4", "FC6", "/", "/"]
EEG_Training = Data(EEG_Training_Raw,channels) 


EEG_Training.filterEEG()

EEG_Training.mean_free_EEG()
#EEG_Training.standardize_EEG()
#EEG_Training.filterEEG()


X, y = EEG_Training.make_X_and_y(time_stamps, training_labels)
#X_standardized = PD.meanfree_X(X)
#X_standardized = PD.standardize_X(X)
X_standardized = X.copy()

vc = Vectorizer()
classifier = LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')
classifier2 = LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')
classifier3 = LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto')


xdawn = XdawnCovariances(1,estimator="lwf",xdawn_estimator = "lwf")
xdawn2 = XdawnCovariances(2,estimator="lwf",xdawn_estimator = "lwf")
xdawn3 = XdawnCovariances(5,estimator="lwf",xdawn_estimator = "lwf")

X_transformed_dawn = xdawn.fit_transform(X_standardized,y)
X_transformed_dawn2 = xdawn2.fit_transform(X_standardized,y)
X_transformed_dawn3 = xdawn3.fit_transform(X_standardized,y)

X_transformed = vc.fit_transform(X_transformed_dawn)
X_transformed2 = vc.fit_transform(X_transformed_dawn2)
X_transformed3 = vc.fit_transform(X_transformed_dawn3)


classifier.fit(X_transformed,y)
classifier2.fit(X_transformed2,y)
classifier3.fit(X_transformed3,y)

#%% Classification Session
EEG_Test = Data(EEG_Test_Raw,channels)

EEG_Test.filterEEG()

EEG_Test.mean_free_EEG()
#EEG_Test.standardize_EEG()
#EEG_Test.filterEEG()

X_test, y_true = EEG_Test.make_Xtest_and_ytrue(classification_time_stamps, classification_labels)
#X_test_standardized = PD.meanfree_X(X_test)
#X_test_standardized = PD.standardize_X(X_test)

X_test_standardized = X_test.copy()

X_test_transformed_dawn = xdawn.transform(X_test_standardized)
X_test_transformed = vc.fit_transform(X_test_transformed_dawn)
y_pred = classifier.predict(X_test_transformed)
Accuracy = accuracy_score(y_true,y_pred)

X_test_transformed_dawn2 = xdawn2.transform(X_test_standardized)
X_test_transformed2 = vc.fit_transform(X_test_transformed_dawn2)
y_pred2 = classifier2.predict(X_test_transformed2)
Accuracy2 = accuracy_score(y_true,y_pred2)

X_test_transformed_dawn3 = xdawn3.transform(X_test_standardized)
X_test_transformed3 = vc.fit_transform(X_test_transformed_dawn3)
y_pred3 = classifier3.predict(X_test_transformed3)
Accuracy3 = accuracy_score(y_true,y_pred3)

#%% Plot erstellen
#EEG_Training.plot_EEG_data()
#EEG_Test.plot_EEG_data()
PD.plot_X(X_test_transformed,training_labels)

#%%
channels = ["FC1","C3","FC1", "FC2", "C4", "FC6", "/", "/"]
EEG_Training = Data(EEG_Training_Raw,channels) 


EEG_Training.filterEEG()

#EEG_Training.mean_free_EEG()
EEG_Training.standardize_EEG()
#EEG_Training.filterEEG()

TestSignal = EEG_Training.data.copy()
TestSignal = np.array(TestSignal)
TestMean = np.std(TestSignal,axis=1)






#%%
#Create Result Window
result_window = GUI.make_result_window(y_true, y_pred, Acc)

while True:
    #Monitoring window status
    event_result_window , values_result_window = result_window.read(timeout=4)
    
    if event_result_window == 'Main Menu':
        result_window.close()
        break
    if event_result_window == sg.WIN_CLOSED:
        result_window.close()
        break
    








#%% Test Section
def standardize_X(X):
    X_standardized = []
    for i in range(0,len(X)):
        X_temp = X[i].copy()
        for i in range(0,len(X_temp)):
            X_temp[i] = (X_temp[i] - np.mean(X_temp[i])) / np.std(X_temp[i])
        X_standardized.append(X_temp)
    X_standardized = np.array(X_standardized)
    return X_standardized  
  

def standardize_X_manually(X):
    X_standardized = []
    temp = []
    StandardizedValue = 0
    for i in range(0,len(X)):
        X_temp = X[i].copy()
        Means = np.mean(X_temp, axis=1)
        Stds = np.std(X_temp, axis=1)
        for j in range(0,len(X_temp)):
            for l in range(0,500):
                StandardizedValue = (X_temp[j,l] - np.mean(X_temp[j])) / np.std(X_temp[j])
                temp.append(StandardizedValue)
            X_standardized.append(temp)
            temp = []
    return X_standardized