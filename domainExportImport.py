
# Export domains from one GDB to another
# designed to export from SDE DB into fGDB in ArcMap (built-in functionality exists in Pro.)
import arcpy, re, os

exportGDB = "EXPORT_DB"  # gdb to export domains from 
importGDB = "IMPORT_DB"  # gdb to import domains to  
exportFolder = "EXPORT_FOLDER" # folder to store export domain tables in.

domains = arcpy.da.ListDomains(exportGDB)

for domain in domains:
    if re.search('SEARCH_STRING', domain.name): # use desired search string here
        domainName = domain.name
        domainDesc = domain.description
        exportTable = os.path.join(exportFolder, str(domainName) + ".dbf")
        exportCheck = exportTable.split("\\")[-1:][0]
        if exportCheck not in os.listdir(exportFolder): # Prevent domains to table export if the tables already exist. 
            arcpy.DomainToTable_management(exportGDB, domainName, exportTable + ".dbf",  "code", "desc", "")
        arcpy.TableToDomain_management(exportTable, "code", "desc", importGDB, domainName, domainDesc, "APPEND")


# Correct domain code sorting if desired
'''
importedDomains = arcpy.da.ListDomains(importGDB)
for domain in importedDomains:
    arcpy.management.SortCodedValueDomain(importGDB, domain.name, "CODE", "ASCENDING")
'''