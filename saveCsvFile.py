import csv
from tkinter import filedialog
from tkinter import *

def saveFile(finalMainAnswer,direction,streetName):
    # root = Tk()
    # root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv file","*.csv"),("all files","*.*")))
    # with open(root.filename+".json","w") as newFile:
    #         json.dump(finalMainAnswer, newFile, indent = 4)

    myFile = open(direction+'_'+streetName+'.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(finalMainAnswer)