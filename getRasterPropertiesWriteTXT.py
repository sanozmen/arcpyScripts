import arcpy
outputTxtFile =  r'C:\Users\xx.txt' #output comma delimited text file
arcpy.env.workspace = r'set your env'#input raster file
rasters = arcpy.ListRasters("*")
print rasters
for raster in rasters:
    minResult = arcpy.GetRasterProperties_management(raster, "MINIMUM")
    maxResult = arcpy.GetRasterProperties_management(raster, "MAXIMUM")
    meanResult = arcpy.GetRasterProperties_management(raster, "MEAN")
    minRes = minResult.getOutput(0)
    maxRes = maxResult.getOutput(0)
    meanRes = meanResult.getOutput(0)
    f = open(outputTxtFile, 'a+') #open the text file for writing
    f.write(raster+","+minRes+","+meanRes+","+maxRes+"\n")
