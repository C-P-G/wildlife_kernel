# Application Development Final project
# Felix Reisinger & Claire Pfalzner-Gibbon
# purpose: Kernelfunction wildlife accidents
# created: 05.02.22
# last update: 05.02.2022

import arcpy
# Set environment settings
env.workspace = ""


# Buffer streets
# Set local variables
in_features = "streets"
# set output path
output_buffer = "c:/output/output.gdb/bufferstreets"
buffer_distance = "200 meters"
# actual buffer function
arcpy.analysis.Buffer(in_features, output_buffer, buffer_distance)


# Intersect streets with accidents
in_features = ["bufferstreets", "wildlife_accidents"]
out_feature_class = "output.gdb/intersection"
join_attributes = "NO_FID"
arcpy.analysis.Intersect(in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})


# KERNELFUNCTION
# which one to use ?
# https://pro.arcgis.com/de/pro-app/latest/tool-reference/geostatistical-analyst/an-overview-of-the-interpolation-toolset.htm


# PRINT PDF
# output path (folder). Please change accordingly
outPath = "C:\\Users\\clair\\Desktop\\WS_20\\GeoApp"
#generation of an empty PDF master document
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "kernelmap")