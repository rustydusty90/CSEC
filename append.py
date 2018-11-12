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
    with open(config) as f:
        data = json.load(f)

    templateDict = data['template']
    templateGdb = os.path.join(dataLocation, templateDict.get('gdb'))


    # make sure template is empty
    checkTemplate(templateGdb)



def checkTemplate(gdb):
    '''iterate through features in template gdb,
        make sure all feature classes are empty
        if they're not, run Delete Features tool'''

    if arcpy.Exists(gdb):
        print 'found it'


def appendData():
    '''do the appending'''

    

main()
