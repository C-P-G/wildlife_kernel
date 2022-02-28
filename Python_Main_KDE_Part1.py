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

inputStreet = arcpy.GetParameterAsText(0)
inputAccidents = arcpy.GetParameterAsText(1)
inputName = arcpy.GetParameterAsText(2)

# Buffered inputStreet Dataset in Diameter D_40 + D_400
# Buffer 40
# Input variables
output_buffer = wildlifeGDB + "\\" + "bufferD40"
buffer_distance = "20 meters"
# Buffer Function
arcpy.analysis.Buffer(inputStreet, output_buffer, buffer_distance, dissolve_option = "ALL")

# Buffer 400
output_buffer = wildlifeGDB + "\\" + "bufferD400"
buffer_distance = "200 meters"
arcpy.analysis.Buffer(inputStreet, output_buffer, buffer_distance, dissolve_option = "ALL")

# Intersect inputStreet with all accidents (inputAccidents) to get the accidents lying on the inputStreet
in_features = ["bufferD40", inputAccidents]
out_feature_class = wildlifeGDB + "\\" + "intersectedAccidents"
join_attributes = "ONLY_FID"
output_type = "point"
arcpy.analysis.Intersect(in_features, out_feature_class, join_attributes)


# KERNELFUNCTION
# use the intersected accidents for calculation
in_features = "intersectedAccidents"
# KDE Function
KDE = arcpy.sa.KernelDensity(in_features, population_field="NONE", search_radius=0.01, area_unit_scale_factor="SQUARE_MAP_UNITS", out_cell_values="DENSITIES", method="PLANAR", in_barriers="")

# set a mask over the calculation
KDE = ExtractByMask(KDE, "bufferD400")
# saves the kernel in the database
KDE.save(wildlifeGDB + "\\" + inputName)
#OUTPUT #1

arcpy.AddMessage("Kernel complete")
arcpy.AddMessage (inputName + " created")

