#batch conversion of shapefile features into google earth kml format
import arcpy

arcpy.env.workspace = r'set your workspace'
workspace= arcpy.env.workspace
Features= ["fill in with your features"]
#first to layers
for feature in Features:
    print type(feature)
    outlayer = feature+ ".lyr"
    arcpy.SaveToLayerFile_management(feature, outlayer, "ABSOLUTE")

#list .lyr's
layers = arcpy.ListFiles("*.lyr*")
#then to kml || kmz
for layer in layers:
    oName, oExt = os.path.splitext(layer)
    outKML = oName+ ".kmz"
    arcpy.LayerToKML_conversion(layer, outKML)
