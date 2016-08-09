# ListModules
ListModules_Single is a Python script that takes any single, unminified JavaScript file and searches it for Dojo and ESRI AMD module names.
It then writes those names to a text file called modules.txt. You can use this file as input for
the ArcGIS API for JavaScript Web Optimizer to create a custom build of the API
https://developers.arcgis.com/javascript/jshelp/inside_web_optimizer.html

ListModules_Mulitple does the same thing but takes a directory path as input and will search the directory for multiple JavaScript files with AMD module names.

The output "modules.txt" will be placed in the root folder location where you put
the script.
