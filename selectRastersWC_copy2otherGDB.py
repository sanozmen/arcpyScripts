import os
import arcpy

# Set environment settings
rasterGDB=r'C:\Users\xxx\Desktop\xxx\xxxx\01 - Geodatabase\xx.gdb'
#ur addition is the most important part of the line below. It helped to eliminate conflict of "str+unicode" join down below at os.path.join
outRasterGDB = ur'C:\\Users\\xxxx\\Desktop\\1st\\xxx\\01 - Geodatabase\\xxxx.gdb'
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