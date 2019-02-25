import os
import arcpy

#rasters to be clipped
dem = 'raster1'
aws='raster2'
pd= 'raster3'

# Polygon feature classes to be used
layers = []

arcpy.env.workspace = 'set your workspace'

for layer in layers:
    #name output rasters
    outputRaster= "DEM_"+layer
    arcpy.Clip_management(dem, '#', outputRaster, layer, '#', 'ClippingGeometry')

for layer in layers:
    outputRaster= "AWS_"+layer
    arcpy.Clip_management(dem, '#', outputRaster, layer, '#', 'ClippingGeometry')

for layer in layers:
    outputRaster= "PD_"+layer
    arcpy.Clip_management(dem, '#', outputRaster, layer, '#', 'ClippingGeometry')

#get all clipped rasters and reproject them
newRasters=arcpy.ListRasters()
#checking if the rasters are received
print newRasters
for raster in newRasters:
    outputRaster2=raster+"rpj"
    arcpy.ProjectRaster_management(raster,outputRaster2,'template layer used as projection reference')
