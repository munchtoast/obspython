#Requirements: pywinauto, schedule, comtypes
#The hotkeys need to be changed, possibly to some insane combination of the sort.
#You have to CD in the directory of obs64, for obs to actually run...
#Flash Video (FLV) is the best format.

#Output DONT TOUCH COMPUTER
#Find the obs app without specifiying it

import os
import csv
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
    #Create application class and start program to keep track. 
    #If the application is running, connect to that window, instead of dupe-open
    try:
        app = Application().connect(path=r'obs64')

    #If not, go ahead and start the application (Application is not running)
    except:
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

#Start Streaming, scene is a STR type
def startStream(appObj, fileObj, scene):
    if (not appObj.getStream()):
        fileWrite("STREAM START: startStream(),", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F1}")
        if scene == "2":
            send_keys("^{F4}")
        else:
             send_keys("^{F3}")
        appObj.setStream(1)

#Start Recording, scene is a STR type
def startRecord(appObj, fileObj, scene):
    if (not appObj.getRecord()):
        fileWrite("RECORD START: startRecord(),", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F5}")
        if scene == "2":
            send_keys("^{F4}")
        else:
             send_keys("^{F3}")
        appObj.setRecord(1)

#Stop Streaming, scene is a STR type
def endStream(appObj, fileObj, scene):
    if (appObj.getRecord()):
        fileWrite("STREAM END: endStream(),", fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F2}")
        if scene == "2":
            send_keys("^{F4}")
        else:
             send_keys("^{F3}")
        appObj.setRecord(0)

#Stop Recording, scene is a STR type
def endRecord(appObj, fileObj, scene):
    if (appObj.getRecord()):
        fileWrite("RECORD END: endRecord(),",fileObj, today)
        obsFocus(appObj.getData(), 1)
        send_keys("^{F6}") 
        if scene == "2":
            send_keys("^{F4}")
        else:
             send_keys("^{F3}")
        appObj.setRecord(0)

def updateReference():
    userDirectory = ""
    while (not os.path.exists(r'{}'.format(userDirectory))):
        userDirectory = input("Enter OBS Directory: ")
    return userDirectory

#All Events with dates. Streams and Records will start and end at the same time.
def sunday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().sunday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().sunday.at(time_end).do(endRecord, local_appObj, local_fileObj)

    schedule.every().sunday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().sunday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def monday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().monday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().monday.at(time_end).do(endRecord, local_appObj, local_fileObj, scene)

    schedule.every().monday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().monday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def tuesday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().tuesday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().tuesday.at(time_end).do(endRecord, local_appObj, local_fileObj, scene)

    schedule.every().tuesday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().tuesday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def wednesday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().wednesday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().wednesday.at(time_end).do(endRecord, local_appObj, local_fileObj, scene)

    schedule.every().wednesday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().wednesday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def thursday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().thursday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().thursday.at(time_end).do(endRecord, local_appObj, local_fileObj, scene)

    schedule.every().thursday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().thursday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def friday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().friday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().friday.at(time_end).do(endRecord, local_appObj, local_fileObj, scene)

    schedule.every().friday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().friday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def saturday_event(local_appObj, local_fileObj, time_start, time_end, scene):
    schedule.every().saturday.at(time_start).do(startRecord, local_appObj, local_fileObj, scene)
    schedule.every().saturday.at(time_end).do(endRecord, local_appObj, local_fileObj, scene)

    schedule.every().saturday.at(time_start).do(startStream, local_appObj, local_fileObj, scene)
    schedule.every().saturday.at(time_end).do(endStream, local_appObj, local_fileObj, scene)

def main(value):
    #Check if reference text exists. If the reference text exists, read through it and get the data.
    #Ideas: find a way to disect the dates for recording and streaming, get the hotkey bindings, **Directory and OS**
    userDirectory = ""
    csvfile = open("event_schedule.csv", "r")
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

    #Schedule for starting the recordings & streams
    #Open the event csv file
    first_array = [] #Debug purposes
    #with open("event_schedule", mode="r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    row_count = 0
    for row in reader:
        #Ignore the first row
        if row_count == 0:
            first_array = row #Debug purposes
            pass
        else:
            #Count the first index in a row, always
            index_count = 0
            for item in row:
                #Ignore the empty spaces
                if item != "()": 
                    #Parse out the items, ex. (num1, num2) to [num1, num2] where num(1/2) are strings
                    disection_item = item.replace('(', "").replace(')', "").replace(' ', "").split(",")
                    time_start = disection_item[0] #num1
                    time_end = disection_item[1] #num2
                    scene = disection_item[2] #choose scene
                    print(first_array[index_count] + " " + time_start + ", " + time_end + ": " + scene)

                    #Sunday
                    if index_count == 0:
                        sunday_event(appObj, fileObj, time_start, time_end, scene)

                    #Monday
                    elif index_count == 1:
                        monday_event(appObj, fileObj, time_start, time_end, scene)
                    
                    #Tuesday
                    elif index_count == 2:
                        tuesday_event(appObj, fileObj, time_start, time_end, scene)

                    #Wednesday
                    elif index_count == 3:
                        wednesday_event(appObj, fileObj, time_start, time_end, scene)
                    
                    #Thursday
                    elif index_count == 4: 
                        thursday_event(appObj, fileObj, time_start, time_end, scene)

                    #Friday
                    elif index_count == 5:
                        friday_event(appObj, fileObj, time_start, time_end, scene)

                    #Saturday
                    else:
                        saturday_event(appObj, fileObj, time_start, time_end, scene)
                
                index_count += 1

        row_count += 1

    
    #Close the files
    refObj.close()
    csvfile.close()

    #Possibly create two files, where one tracks the user input and exits on this command prompt??

    while True:
        schedule.run_pending()
        time.sleep(1)

    fileObj.close() #This will cause fatal errors...

#When you open up obs studio, first time, when putting it on someone's computer, set the computer displays and scenes, default webcam and default video,
#you're going to need to use obspython, set it so it automatically does these things. recording format, flash video, or mp4
#This file must be ran as main
if __name__ == "__main__":
    main(0)    