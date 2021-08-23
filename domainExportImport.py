
# Export domains from one GDB to another
# designed to export from outdated SDE into FGDB since SDE isn't accessible to copy domains in ArcGIS Pro. 
 
import arcpy, re, os

exportGDB = ""  # gdb to export domains from 
importGDB = ""  # gdb to import domains to  
exportFolder = "" # folder to store export domain tables in. Could also store in memory.

domains = arcpy.da.ListDomains(exportGDB)

for domain in domains:
    if re.search('sw.+', domain.name):
        domainName = domain.name
        domainDesc = domain.description
        exportTable = os.path.join(exportFolder, str(domainName) + ".dbf")
        exportCheck = exportCheck = exportTable.split("\\")[-1:][0]
        if exportCheck not in os.listdir(exportFolder): # Prevent domains to table export if the tables already exist. 
            arcpy.DomainToTable_management(exportGDB, domainName, exportTable + ".dbf",  "code", "desc", "")
        arcpy.TableToDomain_management(exportTable, "code", "desc", importGDB, domainName, domainDesc, "APPEND")

