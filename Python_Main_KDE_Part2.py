# Application Development Final project
# Felix Reisinger & Claire Pfalzner-Gibbon
# purpose: Kernelfunction wildlife accidents
# created: 05.02.22
# last update: 05.02.2022
# KDE = Kernel Density Estimation

import arcpy
# Set environment settings
from arcpy.sa import KernelDensity, ExtractByMask
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

# set a Geodatabase: Needed for saving the KernelDensityEstimation later
wildlifeGDB = r"C:\Users\felix\OneDrive\Dokumente\ArcGIS\Projects\Final_Assignment\Final_Assignment.gdb"
# set a workspace
arcpy.env.workspace = wildlifeGDB
# otherwise it spits out an error if you run the code more then once with the same output name
arcpy.env.overwriteOutput = True

# get input datasets
inputStreet = arcpy.GetParameterAsText(0)
inputKDE_newSymbology_Polygon = arcpy.GetParameterAsText(1)
outputName = arcpy.GetParameterAsText(2)

# Buffered inputStreet Dataset in Diameter D_40 + D_400
# Buffer 40
# Input variables
output_buffer = wildlifeGDB + "\\" + "bufferD40"
buffer_distance = "20 meters"
# Buffer Function
arcpy.analysis.Buffer(inputStreet, output_buffer, buffer_distance, dissolve_option = "ALL")

#Reclassification has to be done

# Process: Raster to Polygon (Raster to Polygon) (conversion)
Output_polygon_features = wildlifeGDB + "\\" + outputName + "PolygonKDE"
PolygonKDE = Output_polygon_features
arcpy.conversion.RasterToPolygon(in_raster=inputKDE_newSymbology_Polygon, out_polygon_features=Output_polygon_features, simplify="SIMPLIFY", raster_field="VALUE", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)
#OUTPUT #3

# Intersect the just created Polygon with the Buffered Street to get the final Product
in_features = [Output_polygon_features, "bufferD40"]
out_feature_class = wildlifeGDB + "\\" + outputName + "intersectedAccidents"
outFeatureClass = out_feature_class
join_attributes = "ALL"
output_type = "point"
arcpy.analysis.Intersect(in_features, out_feature_class, join_attributes)
#OUTPUT #4

arcpy.AddMessage (outputName + "created" )
arcpy.AddMessage ("File can be found under:" + "\n" + out_feature_class)


