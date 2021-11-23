# Shorthand wrapper functions to reduce verbosity of arcpy function calls I use a lot. 

import arcpy

def lf(fc):
        return arcpy.ListFields(fc)

def lfNames(fc):
    return([field.name for field in lf(fc)])

def lfLen(fc):
    fieldList = lf(fc)
    return("object contains " + str(len(fieldList)) + " fields")

def lfc():
    return arcpy.ListFeatureClasses()