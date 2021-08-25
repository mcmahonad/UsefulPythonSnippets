# Template for dropping and adding fields with arcpy. 

import arcpy, re, os

arcpy.env.workspace = "" # Set desired working directory

assets = arcpy.ListFeatureClasses()
assets = assets[:-1] # In this case the last feature class wasn't needed. 

# delete a handful of fields that aren't needed
fieldsDel = ("created_user", "created_date", "last_edited_user", "last_edited_date", "FieldObserved")
for asset in assets:
    for field in fieldsDel:
        try:
            arcpy.DeleteField_management(asset, field)
        except:
            print("Unable to delete field")

# add new fields, use re wildcards to only add fields to the desired feature class 
for asset in assets:
        if re.search('Ditch.+', asset):
            arcpy.AddField_management(in_table = asset, field_name="corr_ditchCrossSection", field_alias = "Corr. Cross Section Shape", field_type = "TEXT", field_domain = "swDitchShape")
            arcpy.AddField_management(in_table = asset, field_name="corr_ditchMaterial", field_alias = "Corr. Ditch Material", field_type = "TEXT", field_domain = "swDitchMaterial")
            arcpy.AddField_management(in_table = asset, field_name="corr_ditchType", field_alias = "Corr. Ditch Type", field_type = "TEXT", field_domain = "swDitchType")
        if re.search('Main.+', asset):
            arcpy.AddField_management(in_table = asset, field_name="corr_mainType", field_alias = "Corr. Main Type", field_type = "TEXT", field_domain = "swMainType")
            arcpy.AddField_management(in_table = asset, field_name="corr_mainMaterial", field_alias = "Corr. Main Material", field_type = "TEXT", field_domain = "swMainMaterial")
            arcpy.AddField_management(in_table = asset, field_name="corr_mainDia", field_alias = "Corr. Main Diameter", field_type = "TEXT", field_domain = "swMainDiameter")
            arcpy.AddField_management(in_table = asset, field_name="corr_mainDim", field_alias = "Corr. Main Dimensions (non-circular pipe)", field_type = "TEXT")
            arcpy.AddField_management(in_table = asset, field_name="corr_mainShape", field_alias = "Corr. Main Cross Section Shape", field_type = "TEXT", field_domain = "swMainCrossShape")
            arcpy.AddField_management(in_table = asset, field_name="corr_mainNumPipes", field_alias = "Corr. Num. Main Pipes", field_type = "TEXT", field_domain = "swMainNumber")
        if re.search('Inlet.+', asset):
            arcpy.AddField_management(in_table = asset, field_name="corr_inletType", field_alias = "Corr. Inlet Type", field_type = "TEXT", field_domain = "swInletType")
            arcpy.AddField_management(in_table = asset, field_name="corr_inType", field_alias = "Corr. Inlet Structure Type", field_type = "TEXT", field_domain = "swInType")
        if re.search('Outlet.+', asset):
            arcpy.AddField_management(in_table = asset, field_name="corr_outletType", field_alias = "Corr. Outlet Type", field_type = "TEXT", field_domain = "swOutletType")
            arcpy.AddField_management(in_table = asset, field_name="corr_outletEndType", field_alias = "Corr. Outlet End Type", field_type = "TEXT", field_domain = "swEndType")
        if re.search('Structure.+', asset):
            arcpy.AddField_management(in_table = asset, field_name="corr_structureType", field_alias = "Corr. Structure Type", field_type = "TEXT", field_domain = "swStructureType")




