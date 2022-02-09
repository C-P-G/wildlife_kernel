# Application Development Final project
# Felix Reisinger & Claire Pfalzner-Gibbon
# purpose: Kernelfunction wildlife accidents
# created: 05.02.22
# last update: 05.02.2022

import arcpy
# Set environment settings
arcpy.env.workspace = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb"
# otherwise it spits out an error if you run the code more then once with the same output name
arcpy.env.overwriteOutput = True

# Buffer streets
# Set local variables
in_features = "streets"
# set output path
output_buffer = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb\\bufferstreets"
buffer_distance = "200 meters"
# actual buffer function
arcpy.analysis.Buffer(in_features, output_buffer, buffer_distance)


# Intersect streets with accidents

in_features = ["Roe_deer", "bufferstreets"]
out_feature_class = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb\\intersection"
join_attributes = "all"
output_type = "point"
arcpy.analysis.Intersect(in_features, out_feature_class, join_attributes, output_type)


# KERNELFUNCTION
# which one to use ?
# https://pro.arcgis.com/de/pro-app/latest/tool-reference/geostatistical-analyst/an-overview-of-the-interpolation-toolset.htm


# PRINT PDF
# output path (folder). Please change accordingly
#outPath = "C:\\Users\\clair\\Desktop\\WS_20\\GeoApp"
#generation of an empty PDF master document
#pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "kernelmap")