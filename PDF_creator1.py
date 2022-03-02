# imports the Python side package for geographical analysis
import arcpy
#link to the Project you want to work on
aprx = arcpy.mp.ArcGISProject (r"C:\Users\clair\Documents\ArcGIS\Projects\wildlifekernel\wildlifekernel.aprx")
gdb = "C:\\Users\\clair\\Documents\\ArcGIS\\Projects\\wildlifekernel\\wildlifekernel.gdb"
print(gdb)
m = aprx.listMaps()[0]
lyrSBG = m.listLayers()[0]
#lyrProject = m.listLayers()[1]

input = arcpy.GetParameterAsText(0)

#print (lyrSBG)
#for object in lyrProject:
#    print(object)
#lyrKDE = m.listLayers()[2]
lyt = aprx.listLayouts()[0]
print(lyt.name)
mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
outPath =  "C:\\Users\\clair\\Desktop\\WS_20\\GeoApp\\output\\"
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "KDE_compiled1.pdf")
cur = arcpy.da.SearchCursor(lyrSBG.dataSource, ["SHAPE@", "GRIDCODE", "ID"], 'GRIDCODE = 4')
#cur2 = arcpy.da.SearchCursor(lyrProject, 'OBJECT = Kernel*')

print(lyrSBG.dataSource)
for row in cur:
    mf.camera.setExtent(row[0].extent)
    name = row[2]
    print(name)
    aprx.save
    lyt.exportToPDF(outPath + str(name) +".PDF", 100)
    pdfDoc.appendPages (outPath + str(name) +".PDF")
pdfDoc.saveAndClose()
print ("PDF Mapbook created")
del pdfDoc
del aprx
del m
del lyt
del row
del cur