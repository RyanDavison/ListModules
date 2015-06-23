##NAME: ListModules.py
##AUTHOR: Ryan Davison
##DATE: 6/22/2015
##DESCRIPTION: Takes any single JavaScript file and searches it for Dojo and ESRI AMD module names.
## it then writes those names to a text file called modules.txt. You can use this file as input for
## the ArcGIS API for JavaScript Web Optimizer to create a custom build of the API
## https://developers.arcgis.com/javascript/jshelp/inside_web_optimizer.html


import os
import re
from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()
root.withdraw()
p = re.compile(r'(["](?:esri|dojo|dijit|dojox)[\/].*["][,]?)')
file_path = askopenfilename(filetypes=[("Text files","*.js")], initialdir=(os.path.expanduser('~user')))

with open(file_path, 'r') as f:
    matched = ""
    for line in f:
        x = p.search(line)
        if x:
            y = x.group(1)
            if not y.endswith(","):
                y = y + ","
            matched += y
    #Clean up the string by removing spaces and quote marks, then split the string into a list
    matched = matched.replace(" ", "").replace('"', "").split(',')
    #Use the set method to remove duplicate entries, convert the set back to a list, filter the list to remove any empty strings then sort the list alphabetically
    matched = [x for x in sorted(filter(None, list(set(matched))))]

    #Write out each module to a text file on its own line
    with open('modules.txt', 'wb') as output:
        for x in matched:
            output.write(x + "\n")

    
