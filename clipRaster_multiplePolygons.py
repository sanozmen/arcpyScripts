import os
import arcpy

#rasters to be clipped
dem = 'add image1'
aws='add image2'
pd= r'add image3'

# Polygon feature classes to be used
layers =['add polygon layers']
arcpy.env.workspace = r'add work space'
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
    outputRaster2="rpj"+raster
    arcpy.ProjectRaster_management(raster,outputRaster2,'add one layer to be used as Spatial reference')
