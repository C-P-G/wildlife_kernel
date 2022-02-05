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
inFeatures = "streets"
# set output path
outFeatureClass = "c:/output/output.gdb/multibufferstreets"
buffer_distance_or_field = [200, meters]

arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance_or_field)


# Intersect streets with accidents
# Kernelfunction
# print pdf
# output path (folder). Please change accordingly
outPath = "C:\\Users\\clair\\Desktop\\WS_20\\GeoApp"
#generation of an empty PDF master document
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "")