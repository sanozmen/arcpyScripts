import os
import arcpy

#rasters to be clipped
dem = 'copy/drag here your raster data'
aws='copy/drag here your raster data'
pd= r'copy/drag here your raster data'

# Polygon feature classes to be used
layers =[]
arcpy.env.workspace = r''
#dem
for layer in layers:
    #name output rasters
    outputRaster= "DEM_"+layer
    arcpy.Clip_management(dem, '#', outputRaster, layer, '#', 'ClippingGeometry')
#aws
for layer in layers:
    outputRaster= "AWS_"+layer
    arcpy.Clip_management(aws, '#', outputRaster, layer, '#', 'ClippingGeometry')
#power density
for layer in layers:
    outputRaster= "PD_"+layer
    arcpy.Clip_management(pd, '#', outputRaster, layer, '#', 'ClippingGeometry')

#get all clipped rasters and reproject them
newRasters=arcpy.ListRasters()
#checking if the rasters are received
print newRasters
#reprojecting them into ED50 Zone35N
for raster in newRasters:
    outputRaster2=raster+"rpj"
    arcpy.ProjectRaster_management(raster,outputRaster2,'drag here the reference layer')
