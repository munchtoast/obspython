#Requirements: pywinauto, schedule, comtypes
#TODO: open() the path and the chdir need to be changed. Find a way to get the general location.
#The hotkeys need to be changed, possibly to some insane combination of the sort.

import os
import time
import schedule
from node import *
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from datetime import datetime

#Initalize Globals
appObj = item(0)
REF_FILE = "reference.txt"
LOG_FILE = "log.txt"
EVENT_FILE = "event.txt"
today = datetime.now()

#Write to a file:
def fileWrite(strObj, fileObj, today):
    fileObj.write("{}: {}\n".format(today.strftime("%d/%m/%Y %H:%M:%S"), strObj))
    
#Open up OBS and return the object of the Application class in pywinauto
def obsOpen(userDirectory):
    myDirectory = r'{}'.format(userDirectory)
    print(myDirectory)
    os.chdir(r'{}'.format(myDirectory))
    #Create application class and start program. Keep track of the program
    app = Application().start(r'obs64')
    #Maximize the window and focus so that the keypresses can be handled
    obsFocus(app, 1)

    #Return the object
    return app

#bring focus on app
def obsFocus(appObj, max):
    app_dialog = appObj.top_window()
    if max:
        app_dialog.maximize()
    app_dialog.set_focus()

#Start Streaming
def startStream(appObj, fileObj):
    if (not appObj.getStream()):
        fileWrite("STREAM START, startStream()", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F1}")
        appObj.setStream(1)

#Start Recording
def startRecord(appObj, fileObj):
    if (not appObj.getRecord()):
        fileWrite("RECORD START, startRecord()", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F5}")
        appObj.setRecord(1)

#Stop Streaming
def endStream(appObj, fileObj):
    if (appObj.getRecord()):
        fileWrite("STREAM END, endStream()", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F2}")
        appObj.setRecord(0)

#Stop Recording
def endRecord(appObj, fileObj):
    if (appObj.getRecord()):
        fileWrite("RECORD END, endRecord()", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F6}") 
        appObj.setRecord(0)

def updateReference():
    userDirectory = ""
    while (not os.path.exists(r'{}'.format(userDirectory))):
        userDirectory = input("Enter OBS Directory: ")
    return userDirectory

def monday_event(local_appObj, local_fileObj, time_start, time_end):
    schedule.every().monday.at(time_start).do(startRecord, local_appObj, local_fileObj)
    schedule.every().monday.at(time_end).do(endRecord, local_appObj, local_fileObj)

    schedule.every().monday.at(time_start).do(startStream, local_appObj, local_fileObj)
    schedule.every().monday.at(time_end).do(endStream, local_appObj, local_fileObj)

def monday_event(local_appObj, local_fileObj, time_start, time_end):
    schedule.every().monday.at(time_start).do(startRecord, local_appObj, local_fileObj)
    schedule.every().monday.at(time_end).do(endRecord, local_appObj, local_fileObj)

    schedule.every().monday.at(time_start).do(startStream, local_appObj, local_fileObj)
    schedule.every().monday.at(time_end).do(endStream, local_appObj, local_fileObj)

def main(value):
    #Check if reference text exists. If the reference text exists, read through it and get the data.
    #Ideas: find a way to disect the dates for recording and streaming, get the hotkey bindings, **Directory and OS**
    userDirectory = ""
    if not os.path.exists(REF_FILE):
        refObj = open(REF_FILE, "w")
        #Add directory to reference file
        userDirectory = updateReference()
        refObj.write(userDirectory)
        
    else:
        refObj = open(REF_FILE, "r")
        state = 0
        #Loop through all lines in refObj
        for element in refObj:
            if (not state) and (element != ""):
                userDirectory = element
                state = 1

            #If you can't find anything, add onto the existing file
            else:
                userDirectory = updateReference()
                
    #Create Logs: Put the date and time when OBS started recording 
    if not os.path.exists(LOG_FILE):
        fileObj = open(LOG_FILE, "w")
        fileWrite("Called from obs.py", fileObj, time) if (value == 200) else fileWrite("Called from main.py", fileObj, time)
        fileWrite("Creating Log File", fileObj, today)
    else:
        fileObj = open(LOG_FILE, "a")
        fileWrite("Called from obs.py", fileObj, time) if (value == 200) else fileWrite("Called from main.py", fileObj, time)
        fileWrite("Opening Log File", fileObj, today)

    #Open up OBS
    myObj = obsOpen(userDirectory)
    appObj.setData(myObj)

    #schedule_event = open(EVENT_FILE, "r")

    #for row in schedule_event:
    #    for column in row:
    #        print(column)
    #Schedule for starting the recordings & streams
    #TODO: Copy and paste for streaming.
    #T,TR: 2PM - 4PM
    schedule.every().tuesday.at("14:00").do(startRecord, appObj, fileObj)
    schedule.every().tuesday.at("16:00").do(endRecord, appObj, fileObj)

    schedule.every().thursday.at("14:00").do(startRecord, appObj, fileObj)
    schedule.every().thursday.at("16:00").do(endRecord, appObj, fileObj)

    #M,W,F: 10AM - 11AM
    schedule.every().monday.at("10:00").do(startRecord, appObj, fileObj)
    schedule.every().monday.at("11:00").do(endRecord, appObj, fileObj)

    schedule.every().wednesday.at("10:00").do(startRecord, appObj, fileObj)
    schedule.every().wednesday.at("11:00").do(endRecord, appObj, fileObj)

    schedule.every().friday.at("10:00").do(startRecord, appObj, fileObj)
    schedule.every().friday.at("11:00").do(endRecord, appObj, fileObj)
    
    refObj.close()

    #Possibly create two files, where one tracks the user input and exits on this command prompt??

    while True:
        schedule.run_pending()
        time.sleep(1)

    fileObj.close()

#When you open up obs studio, first time, when putting it on someone's computer, set the computer displays and scenes, default webcam and default video,
#you're going to need to use obspython, set it so it automatically does these things. recording format, flash video, or mp4
#This file must be ran as main
if __name__ == "__main__":
    main(0)    