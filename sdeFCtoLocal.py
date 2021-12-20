import arcpy
from datetime import date
import os

exportFolder = "EXPORT_FOLDER"                                               # this is the local GIS folder that data will  be exported to
os.chdir(exportFolder)                                                       # set working directory to this folder
outFolderName = "Infrastructure_" + str(date.today())                        # get today's date to name the new folder and gdb
os.mkdir(outFolderName)                                                      # create the folder the gdb will be stored within. 
outGDB = arcpy.management.CreateFileGDB(outFolderName,outFolderName)         # create a file gdb with the same name within the folder

arcpy.env.workspace = "GIS_SDE_DB"                                           # set env workspace variable to SDE DB
stormwaterFC = arcpy.ListFeatureClasses(feature_dataset='FEATURE_DATASET')   # create feature dataset variable to export to new GDB.

for fc in stormwaterFC:                                                      # export to new GDB. Refine dataset? I probably don't need all feature classes. 
    arcpy.FeatureClassToGeodatabase_conversion(fc, outGDB)