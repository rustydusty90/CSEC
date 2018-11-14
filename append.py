'''
created 11/12/2018
authors
  - dmarlow and nstewart
environment info
  - machine must have esri installed
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
    dataLocation = r'G:\Testing\forTeamHanna\CSEC_merge'

    # this is where settings are stored
    config = r'C:\Workspace\CSEC\config.json'

    # grab data from config file
    
    # make sure template is empty and is in proper place
    checkTemplate(templateGdb)'''returns template GDB name for use in validateFields()/appendData()'''

    defineInputs()'''return interable object for layer mappings to template'''

    validateFields()'''checks the validity of an input field against the target input: output - WARNINGS, Log '''

    appendData(definedInputs, target)'''append inputs that were defined in defineInputs()'''



def logging(toLog):
    '''perfoms logging for troubleshooting script issues'''

def checkTemplate(gdb):
    '''iterate through features in template gdb,
        make sure all feature classes are empty
        if they're not, run Delete Features tool'''

    if arcpy.Exists(gdb) == False:
        print 'CANT find it'
        sys.exit()
    

def appendData():
    '''do the appending'''
    Append_management (inputs, target,'NO_TEST')

    

def validateFields():
    '''validate source field is <= target field'''

def defineInputs():
    '''This function will get the inputs and structure them in a way that
    can be used by the append'''
    with open(config) as f:
        data = json.load(f)

    templateDict = data['template']
    templateGdb = os.path.join(dataLocation, templateDict.get('gdb'))
    






    

main()
