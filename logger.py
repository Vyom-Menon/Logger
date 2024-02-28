#Gives operating system commands
import os
#imports the date and time feature
from datetime import datetime

print("CURRENT TIME/DATE: ", datetime.now())

#Creates the log
def createlog(logname):
    #Giving date and time of log
    rn = datetime.now()
    print("log-date:", rn)
    #makes the log
    filename = str(logname) + ".txt"
    open(filename, "at")
    #Adding log to log list
    filelist = open("filelist.txt", "at")
    filelisttext = filename + " "
    filelist.write(filelisttext)
    filelist.write(str(rn))
#lists all the logs
def ls():
    filelistls = open("filelist.txt", "r")
    print(filelistls.read())

#reads a specified log   
def readlog(logname):
    logtoread = open(logname, "r")
    reading = logtoread.read()
    print(reading)

#rewrites the log by removing all previous data and inserting new data
def writelog(logname):
    #warning
    print("this function clears current data in a log")
    #Calles the file
    writer = open(logname, "w")
    writing = str(input("Enter your log-text here: "))
    writer.write(writing)
    
#adds to a log
def editlog(logname):
    print("THIS FUNCTION ADDS TO CURRENTLY EXISITNG DATA OF A LOG")
    log = open(logname, "a")
    #user input, change the value of the "editor" varibale to change the value of the data added
    editor = str(input("ENTER ANY TEXT YOU WOULD LIKE TO ADD"))
    #writes user input/value of "editor" variable
    log.write(editor)
    
#delets log
def deletelog(logname):
    #confirmation text
    print("THIS FUNCTION DELETES A LOG, YOU CANNOT UNDO THIS OPERATION FROM HERE")
    #assigns the lognamen to a variable
    logtodelete = logname
    #File list removal(flrm) Archiving log from file list
    flrm = open("filelist.txt", "a")
    #confirmation
    confirmation = str(input("Continue operation Y/N"))
    #if/then for confirmation
    if confirmation == "Y":
        #removes file
        os.remove(logtodelete)
        #Archives from file list
        flrm.write(logtodelete)
        flrm.write(" has been deleted")
    else:
        print("Log will not be deleted")