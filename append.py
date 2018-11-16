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

import arcpy, os, json, sys, shutil

def main():
    '''do everything that needs to be done'''
    
    #Define Global Variables
    relativePath = os.getcwd()
    
    # set the location where all the gdbs are
    dataLocation = r'G:\Testing\forTeamHanna\CSEC_merge\n8\HOTCOG'

    # this is where settings are stored
    config = r'C:\Workspace\CSEC\Settings\config.json'
    
    # read settings and prepare them for later use
    '''return data (dictionary of entire config file),
        templateLayers (names of template layers),
        and inputGdbs, a list of input gdbs that can be used to access attributes'''
    data, templateLayers, inputGdbs = defineInputs(dataLocation, config)

    #gdbPath = checkTemplate(relativePath,templateLayers) #returns template GDB name for use in validateFields()/appendData()

    # grab data from config file
    #validateFields(templateLayers, inputGdbs, gdbPath) #checks the validity of an input field against the target input: output - WARNINGS, Log 

    # append!
    #appendData(gdbPath, data, templateLayers, inputGdbs) 


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

    print('\nObtaining settings from configuration file')

    # access the contents of the config file
    # this will return a dictionary of dictionaries
    with open(config) as f:
        data = json.load(f)

    # obtain associated layer mappings of the template gdb
    templateLayers = data.get('template')

    # create a list of the input gdbs
    inputGdbs = sorted([key for key in data.keys() if key != 'template'])

    return data, templateLayers, inputGdbs


def validateFields(tempLayers, inGdbs, gdbPath):
    #hurting my brain, will have to hold off on this
    '''validate source field is <= target field'''
    
    templateMap = [tL for tL in tempLayers]
    
    for tM in templateMap:
        value = tempLayers.get(tM)
        
    


def appendData(gdbPath, data, templateLayers, inputGdbs):
    '''do the appending, one gdb at a time'''

    finalGdb = r'G:\Testing\forTeamHanna\CSEC_merge\n8\HOTCOG\HOTCOG_merged.gdb'

    # check if finalGdb exists before deleting it
    if os.path.exists(finalGdb):
        print '\nDeleting previous merged gdb'
        shutil.rmtree(finalGdb)
        
    # copy template into gdb that will be used for appending
    shutil.copytree(gdbPath, finalGdb)

    # iterate through input gdbs
    for gdb in inputGdbs:
        print('\nAppending ' + gdb)
        
        # set the path
        inputPath = os.path.join(r'G:\Testing\forTeamHanna\CSEC_merge\n8\HOTCOG\InputGDBs', gdb)

        # get the dictionary with this gdb's layers
        gdbDict = data.get(gdb)

        # iterate through layers
        for layer in sorted(gdbDict):

            # get the names of the layers to append
            inputName = gdbDict.get(layer)
            targetName = templateLayers.get(layer)
            print ('\t {} -> {}').format(inputName, targetName)

            # do the append
            arcpy.Append_management(os.path.join(inputPath, inputName),
                                    os.path.join(finalGdb, targetName), 'NO_TEST')

    print('\nDone with appending')

    
def logging(toLog):
    '''perfoms logging for troubleshooting script issues'''
    

main()

