import arcpy
aprx = arcpy.mp.ArcGISProject("C:\\Users\\felix\\OneDrive\\Desktop\\FinalProject_ApplicationDevelopment\\Final_Assignment_Pfalzner-Gibbon_Reisinger\\Final_Assignment_Pfalzner-Gibbon_Reisinger.aprx")
m = aprx.listMaps()[0]
lyrSBG = m.listLayers()[1]
lyt = aprx.listLayouts()[0]
print(lyt.name)
mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
outPath = "C:\\Users\\felix\\OneDrive\\Desktop\\FinalProject_ApplicationDevelopment\\PDF_CREATOR\\"
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "district502_municipalities.pdf")
cur = arcpy.da.SearchCursor(lyrSBG.dataSource, ["SHAPE@", "GRIDCODE"], 'GRIDCODE = 4')
print (lyrSBG.dataSource)
for row in cur:
    mf.camera.setExtent(row[0].extent)
    name = row[1]
    aprx.save
    lyt.exportToPDF(outPath + "name" +".PDF", 100)
    pdfDoc.appendPages (outPath + "name" +".PDF")
pdfDoc.saveAndClose()
print ("PDF Mapbook created")
del pdfDoc
del aprx
del m
del lyt
del row
del cur