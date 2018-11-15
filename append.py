'''
created 11/12/2018
authors
  - dmarlow and nstewart
environment info
  - machine must have esri installed, and thus must have windows os
  - intended to be run using esri's 2.7 python installation
    but was written to be compatible with python 3
purpose
  - this script is designed to merge county data
    into an aggregated RPC dataset that can be
    submitted to GeoComm's GIS Data Hub
'''

import arcpy, os, json, sys

def main():
    #Define Global Variables
    relativePath = os.getcwd()
    '''do everything that needs to be done'''
    
    # set the location where all the gdbs are
    dataLocation = r'G:\Testing\forTeamHanna\CSEC_merge\n8\HOTCOG'

    # this is where settings are stored
    config = r'C:\Workspace\CSEC\Settings\config.json'
    
    # make sure template is empty and is in proper place
    

    # read settings and prepare them for later use
    '''return interable object for layer mappings to template'''
    data, templateLayers, inputGdbs = defineInputs(dataLocation, config)

    gdbPath = checkTemplate(relativePath,templateLayers) #returns template GDB name for use in validateFields()/appendData()

    # grab data from config file
    #validateFields() checks the validity of an input field against the target input: output - WARNINGS, Log 

    #appendData(definedInputs, target) #append inputs that were defined in defineInputs()

    
    




def checkTemplate(scriptLoc, configTempLayers):
    '''iterate through features in template gdb,
    make sure all feature classes are empty
    if they're not, run Delete Features tool'''
    #Set local variables for processing
    settings = os.path.join(scriptLoc,"Settings")
    gdb = None
    iteration = 0
    good = False
    
    #Walk through folders inside the 'Settings' folder to find a GDB
    for root, dirs, files in  os.walk(settings):
        if ".gdb" in root:
            iteration += 1
            gdbPath = root
            gdb = os.path.basename(root)
            
    #Verify only one Template.GDB in settings location
    if gdb == None:
        #placeholder for logging
        print("No Template GDB found in the settings folder")
        sys.exit()
    elif iteration >1:
        #placeholder for logging
        print("Multiple GDBs found in settings folder")
        sys.exit()
    else:
        good = True
        arcpy.env.workspace = gdbPath
        layers = arcpy.ListFeatureClasses(gdb)
        for layer in layers:
            arcpy.DeletFeatures_management(layer)
        for tL in configTempLayers:
            value = configTempLayers.get(tL)
            if value in layers:
                print(value + " is properly mapped to the template GDB")
            else:
                print(value + " does not match any layer in the template GDB")       
                
    return gdbPath


def defineInputs(dataLocation, config):
    '''This function will get the inputs and structure them in a way that
    can be used by the append'''

    # access the contents of the config file
    # this will return a dictionary of dictionaries
    with open(config) as f:
        data = json.load(f)

    # obtain associated layer mappings of the template gdb
    templateLayers = data.get('template')

    # create a list of the input gdbs
    inputGdbs = [key for key in data.keys() if key != 'template']

    print inputGdbs

    return data, templateLayers, inputGdbs


def validateFields():
    '''validate source field is <= target field'''


def appendData():
    '''do the appending'''
    arcpy.Append_management (inputs, target,'NO_TEST')

    
def logging(toLog):
    '''perfoms logging for troubleshooting script issues'''
    

main()

