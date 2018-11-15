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

import arcpy, os, json


def main():
    '''do everything that needs to be done'''
    
    # set the location where all the gdbs are
    dataLocation = r'G:\Testing\forTeamHanna\CSEC_merge\n8\HOTCOG'

    # this is where settings are stored
    config = r'C:\Workspace\CSEC\Settings\config.json'
    
##    # make sure template is empty and is in proper place
##    '''returns template GDB name for use in validateFields()/appendData()'''
##    checkTemplate(templateGdb)
    templateGdb = os.path.join(dataLocation, 'Settings', 'HOTCOG_TEMPLATE.gdb')

    # read settings and prepare them for later use
    '''return interable object for layer mappings to template'''
    data, templateLayers, inputGdbs = defineInputs(dataLocation, templateGdb, config)

##    # grab data from config file
##    '''checks the validity of an input field against the target input: output - WARNINGS, Log '''
##    validateFields()
##
##    # do the appending
##    '''append inputs that were defined in defineInputs()'''
##    appendData(definedInputs, target)



def checkTemplate(gdb):
    '''iterate through features in template gdb,
        make sure all feature classes are empty
        if they're not, run Delete Features tool'''

    if arcpy.Exists(gdb) == False:
        print 'CANT find it'
        sys.exit()


def defineInputs(dataLocation, templateGdb, config):
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
