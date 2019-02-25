import os
import arcpy

# Set environment settings
rasterGDB=r'copy/drag here your raster data'
#ur addition is the most important part of the line below. ALSO \\ IS A MUST. It helped to eliminate conflict of "str+unicode" join down below at os.path.join
outRasterGDB = ur'C:\\Users\\01 - Geodatabase\\XX'
arcpy.env.workspace=rasterGDB
#filter rasters based on name
reprojRasters=arcpy.ListRasters("*rpj")
#check if correct images were selected
print reprojRasters

for raster in reprojRasters:
    oName,oExt = os.path.splitext(raster)
    print oName
    print outRasterGDB
    type(oName)
    #path to save files
    outRaster= os.path.join(outRasterGDB,oName)
    arcpy.CopyRaster_management(raster,outRaster,"#")
