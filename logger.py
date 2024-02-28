import os
from datetime import datetime
print("this is February log")
print("STARTS AT 2/27/2023")
print("LOG STOPS AT 2/28/2024")
print("CURRENT TIME: ", datetime.now())
def createlog(logname):
    rn = datetime.now()
    print("log-date:", rn)
    filename = str(logname) + ".txt"
    open(filename, "at")
    filelist = open("filelist.txt", "at")
    filelisttext = filename + " "
    filelist.write(filelisttext)
    filelist.write(str(rn))

def ls():
    filelistls = open("filelist.txt", "r")
    print(filelistls.read())

   
def readlog(logname):
    logtoread = open(logname, "r")
    reading = logtoread.read()
    print(reading)
    
def writelog(logname):
    print("this function clears current data in a log")
    writer = open(logname, "w")
    writing = str(input("Enter your log-text here: "))
    writer.write(writing)
    
def editlog(logname):
    print("THIS FUNCTION ADDS TO CURRENTLY EXISITNG DATA OF A LOG")
    log = open(logname, "a")
    editor = str(input("ENTER ANY TEXT YOU WOULD LIKE TO ADD"))
    log.write(editor)
    
def deletelog(logname):
    print("THIS FUNCTION DELETES A LOG, YOU CANNOT UNDO THIS OPERATION FROM HERE")
    logtodelete = logname
    flrm = open("filelist.txt", "a")
    confirmation = str(input("Continue operation Y/N"))
    if confirmation == "Y":
        os.remove(logtodelete)
        flrm.write(logtodelete)
        flrm.write("has been deleted")
    else:
        print("Log will not be deleted")