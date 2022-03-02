# imports the Python side package for geographical analysis
import arcpy
#link to the Project you want to work on
aprx = arcpy.mp.ArcGISProject (r"C:\Users\felix\OneDrive\Dokumente\ArcGIS\Projects\Final_Assignment\Final_Assignment.aprx")
gdb = r"C:\Users\felix\OneDrive\Dokumente\ArcGIS\Projects\Final_Assignment\Final_Assignment.gdb"
print(gdb)
m = aprx.listMaps()[0]
lyrSBG = m.listLayers()[0]
lyrProject = m.listLayers ()[0]

input = arcpy.GetParameterAsText(0)


lyt = aprx.listLayouts()[0]
print(lyt.name)
mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
# set output path
outPath = "C:\\Users\\felix\\OneDrive\\Desktop\\FinalProject_ApplicationDevelopment\\PDF_CREATOR\\"
# file path of end result
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "KDE_compiled1.pdf")
# set the extent of the map
cur = arcpy.da.SearchCursor(lyrSBG.dataSource, ["SHAPE@", "GRIDCODE", "ID"], 'GRIDCODE = 5')
#cur2 = arcpy.da.SearchCursor(lyrProject, 'OBJECT = Kernel*')
#for row in cur2:
#    print(row)
#del cur2
# cur1 = arcpy.da.SearchCursor(lyrKDE.dataSource, ["SHAPE@", "GRIDCODE", "ID"], 'GRIDCODE = 4')
print (lyrSBG.dataSource)
for row in cur:
    # set the extent
    mf.camera.setExtent(row[0].extent)
    name = row[2]
    print(name)
    aprx.save
    # export layer to PDF
    lyt.exportToPDF(outPath + str(name) +".PDF", 100)
    # and append the page to the complete document
    pdfDoc.appendPages (outPath + str(name) +".PDF")
pdfDoc.saveAndClose()
print ("PDF Mapbook created")
del pdfDoc
del aprx
del m
del lyt
del row
del cur