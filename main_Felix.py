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

# Apply Symbolog from Layer to give the right symbology to our created KDE
#KDE_buffer400 = arcpy.Raster("KDE_buffer400")
sampleSymbology = arcpy.Raster("sampleSymbology")

# Process: Apply Symbology From Layer (Apply Symbology From Layer) (management)
Updated_Symbology = arcpy.management.ApplySymbologyFromLayer(in_layer=KDE, in_symbology_layer=sampleSymbology, symbology_fields=[["VALUE_FIELD", "", ""]], update_symbology="UPDATE")[0]

# Process: Reclassify (Reclassify) (sa)
Output_raster = wildlifeGDB + "\\" + inputName + "Reclassified"
Reclassify = Output_raster
# i hab keine ahnung wieso des so verschachtelt is und wär dir um jede Erklärung dankbar... Output_Raster/Reclassify
Output_raster = arcpy.sa.Reclassify(in_raster=Updated_Symbology, reclass_field="VALUE", remap="5656,884277 57692,648788 1;57692,648788 93959,999810 2;93959,999810 129438,930159 3;129438,930159 167283,122530 4;167283,122530 206704,156250 5", missing_values="DATA")
Output_raster.save(Reclassify)
#OUTPUT #2

# Process: Raster to Polygon (Raster to Polygon) (conversion)
Output_polygon_features = wildlifeGDB + "\\" + inputName + "PolygonKDE"
PolygonKDE = Output_polygon_features
arcpy.conversion.RasterToPolygon(in_raster=Output_raster, out_polygon_features=Output_polygon_features, simplify="SIMPLIFY", raster_field="VALUE", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)
#wir brauchen zugriff auf diese daten
#OUTPUT #3

# Intersect the just created Polygon with the Buffered Street to get the final Product
in_features = ["bufferD40", Output_polygon_features]
out_feature_class = wildlifeGDB + "\\" + inputName + "intersectedAccidents"
outFeatureClass = out_feature_class
join_attributes = "ONLY_FID"
output_type = "point"
arcpy.analysis.Intersect(in_features, out_feature_class, join_attributes)
#OUTPUT #4





























