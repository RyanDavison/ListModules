##NAME: ListModules.py
##AUTHOR: Ryan Davison
##DATE: 6/22/2015
##DESCRIPTION: Takes a directory containing unminified JavaScript files and searches them for Dojo and ESRI AMD module names.
## it then writes those names to a text file called modules.txt. You can use this file as input for
## the ArcGIS API for JavaScript Web Optimizer to create a custom build of the API
## https://developers.arcgis.com/javascript/jshelp/inside_web_optimizer.html


import os, re, tkFileDialog
##import re
from Tkinter import *

##from tkFileDialog import askdirectory

root = Tk()
root.withdraw()
p = re.compile(r'("(?:esri|dojo|dijit|dojox|dgrid)\/.*")')
directorypath = raw_input("Enter a directory path: ")
extension = ".js"
##directorypath = askdirectory()

matched = ""
for root, dirs, files in os.walk(directorypath):
      fileList = [os.path.join(root, fi) for fi in files if fi.endswith(extension)]
      for item in fileList:
          with open(item, 'r') as f:
            for line in f:
                x = p.search(line)
                if x:
                    print x.group(0)
                    y = x.group(1)
                    if not y.endswith(","):
                        y = y + ","
                        matched += y                       
#Clean up the string by removing spaces and quote marks, then split the string into a list
matched = matched.replace(" ", "").replace('"', "")[:-1]
#Use the set method to remove duplicate entries, convert the set back to a list, filter the list to remove any empty strings then sort the list alphabetically
matched = [x for x in sorted(filter(None, list(set(matched.split(",")))))]
print str(len(matched)) + " modules were found in " + directorypath
print "module list can be found at " + os.path.dirname(os.path.realpath(__file__))
#Write out each module to a text file on its own line
with open('modules.txt', 'wb') as output:
    for x in matched:
        output.write(x + "\n")

          

    
