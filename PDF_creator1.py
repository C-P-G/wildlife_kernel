# imports the Python side package for geographical analysis
import arcpy
#link to the Project you want to work on
aprx = arcpy.mp.ArcGISProject(r"C:\Users\felix\OneDrive\Desktop\FinalProject_ApplicationDevelopment\Final_Assignment_Pfalzner-Gibbon_Reisinger\Final_Assignment_Pfalzner-Gibbon_Reisinger.gdb\Final_Assignment_Pfalzner-Gibbon_Reisinger.aprx")
gdb = r"C:\Users\felix\OneDrive\Desktop\FinalProject_ApplicationDevelopment\Final_Assignment_Pfalzner-Gibbon_Reisinger\Final_Assignment_Pfalzner-Gibbon_Reisinger.gdb"
print(gdb)
m = aprx.listMaps()[0]
lyrSBG = m.listLayers()[1]
lyrProject = m.listLayers ()
#print (lyrSBG)
for object in lyrProject:
    print(object)
#lyrKDE = m.listLayers()[2]
lyt = aprx.listLayouts()[1]
print(lyt.name)
mf = lyt.listElements("MAPFRAME_ELEMENT")[0]
outPath = "C:\\Users\\felix\\OneDrive\\Desktop\\FinalProject_ApplicationDevelopment\\PDF_CREATOR\\"
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath + "KDE_compiled1.pdf")
cur = arcpy.da.SearchCursor(lyrSBG.dataSource, ["SHAPE@", "GRIDCODE", "ID"], 'GRIDCODE = 5')
#cur2 = arcpy.da.SearchCursor(lyrProject, 'OBJECT = Kernel*')
#for row in cur2:
#    print(row)
#del cur2
# cur1 = arcpy.da.SearchCursor(lyrKDE.dataSource, ["SHAPE@", "GRIDCODE", "ID"], 'GRIDCODE = 4')
print (lyrSBG.dataSource)
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