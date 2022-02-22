# Open Broadcaster Studio (OBS) Automator

Python script to run scheduled events for starting live streams, and recordings supplied a CSV. 

## Description

This program is used to replace subscription-based streaming services, with a more light-weight and free option. The program does not require you to modify any directories on OBS except for the hotkey layout. Step-by-step instructions on modifying this can be found below under **Executing program**. Optional modifications through the OBSPython library have been included with this repository. 

## Getting Started

### Dependencies

* **Windows 10**
* **Open Broadcaster Studio (OBS)**
* **Python 3.6.0**
* **pywinauto**
* **schedule**
* **comtypes**
* **datetime**

### Installing

* You can install the latest version of Python by navigating to this link: https://www.python.org/
* Open Broadcaster Studio is also free to install by navigating to this link: https://obsproject.com/
* For installing the required libraries for Python, execute these commands in a terminal:
    * **pip install pywinauto**
    * **pip install schedule**
    * **Comtypes will be installed with pywinauto**
    * **datetime is included in native libraries!**

### Executing program

* Running the program can be done by opening up a terminal on your computer:
    * Navigate to the directory of the file
    * Run "**python main.py**"
    * First time run:
        * You will need to supply the install location of your OBS folder.
            * You can do this by navigating to the start menu, and typing in "OBS", then "File location"
            * Get the location of the shortcut, by properties and "file location"
            * Copy the entire directory, and paste this inside the program (Should be in .../bin/64-bit)
        
* To make modifications, and record/stream at certain times:
    * Open "**"event_schedule.csv"**" with an IDE or Text Editor, and modify the contents as required.
    * The format is as followed: (Recording_Start, Recording_End, Scene) where Scene specifies the certain Scene in OBS that you would like to set at the recording.
    
    * Examples: If you would like to record at 9AM, and end at 12PM on Monday, make sure this is the entry: **"(09:00,12:00,1)"** at the second column. (This uses 24-hour format!)

## Help

* If "**main.py**" does not run properly try: "**python3 main.py**"
* If there are errors with importing the libraries, try these steps below:
    * Open a file explorer, navigate to the "**site-packages**", and copy the directory location
    * Open up the Environment Variables, and insert this into the **PATH**
    * You may also be missing the packages, which you can do by following "**Installing**" section above
* If the program is crashing instantly, and you have changed the directory of OBS, reinput this in the "***reference.txt**" file
* The program does not accept the CSV file format:
    * Make sure that you have followed the precise format:
    * The days of the week start at Sunday (1st columnn) to Saturday (7th column)
    * Inputted schedules are separated by a comma, and must not have any whitespacing.
    * No recordings can be specified as "**()**" without the quotes

## Version History

* 0.3
    * Schedule library has been provided, as issues with importing the library
* 0.2
    * Various bug fixes and optimizations with running the script
    * Example CSV file has been provided
* 0.1
    * Initial Release, Log features and reference

## License

This project is licensed under the MIT License - see the LICENSE.md file for details