# ListModules
ListModules is a Python script that takes any single JavaScript file and searches it for Dojo and ESRI AMD module names.
it then writes those names to a text file called modules.txt. You can use this file as input for
the ArcGIS API for JavaScript Web Optimizer to create a custom build of the API
https://developers.arcgis.com/javascript/jshelp/inside_web_optimizer.html

A file selection dialog is provided to easily navigate to and select you JavaScript file.

The output "modules.txt" will be placed in the root folder location where you put
the script.
