# Shorthand syntax for those annoyinging long ArcPy calls that get used a lot in terminal.

import arcpy

# return properties of a feature class

def lf(fc):
        return arcpy.ListFields(fc)

def lfNames(fc):
    return([field.name for field in lf(fc)])

def lfLen(fc):
    fieldList = lf(fc)
    return("object contains " + str(len(fieldList)) + " fields")

#  change arcpy workspace

def setWksp(directory):
    arcpy.env.workspace = (directory)

# return objects in workspace

def lFc():
    return arcpy.ListFeatureClasses()

def lDat():
    return arcpy.ListDatasets()

def lTab():
    return arcpy.ListTables()


