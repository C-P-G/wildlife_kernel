# Application Development Final project
# Felix Reisinger & Claire Pfalzner-Gibbon
# purpose: Kernelfunction wildlife accidents
# created: 05.02.22
# last update: 05.02.2022

import arcpy
# Set environment settings
from arcpy.sa import KernelDensity

# need for saving kernel later
wildlifeGDB = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb"
arcpy.env.workspace = wildlifeGDB
# otherwise it spits out an error if you run the code more then once with the same output name
arcpy.env.overwriteOutput = True

# Buffer streets
# Set local variables
in_features = "streets"
# set output path
output_buffer = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb\\bufferstreets"#buffer_distance = "200 meters"
# actual buffer function
#arcpy.analysis.Buffer(in_features, output_buffer, buffer_distance)


# Intersect streets with accidents

in_features = ["bufferstreets", "Roe_deer"]
out_feature_class = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb\\intersection"
join_attributes = "ONLY_FID"
output_type = "polyline"
arcpy.analysis.Intersect(in_features, out_feature_class, join_attributes)


# KERNELFUNCTION
in_features = "intersection"
populationfield = "none"
out_cell_values = "DENSITIES"
# leave out cell size and search radius for now, does not work with it
cell_size = 10
search_radius = 400

kd = KernelDensity(in_features, populationfield)

# saves the kernel in the database
kd.save(wildlifeGDB + "\\" + in_features + "_kd")

# PRINT PDF
# output path (folder). Please change accordingly
#outPath = "C:\\Users\\clair\\Desktop\\WS_20\\GeoApp"
#generation of an empty PDF master document
#pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "kernelmap")