import os
import copy
from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader

outputDirName = "./frontCoverOutput" + \
    str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
os.mkdir(outputDirName)

for item in os.listdir("./coverOriginal_pdf"):
    item_path = os.path.join("./coverOriginal_pdf", item)
    print("item name is {}".format(item))
    print("file full path is {}".format(item_path))
    
    pdfCover = PdfFileReader(open(item_path, 'rb'))
    pdfCoverPages = pdfCover.getNumPages()
    print("{} file have {} pages".format(item, pdfCoverPages))

    pdf_writer = PdfFileWriter()

    halfPageFlag = 0
    page = pdfCover.getPage(0)
    _upperRightX = page.mediaBox.getUpperRight_x()
    _upperRightY = page.mediaBox.getUpperRight_y()
    cutPoint = (_upperRightY - 728) / 2
    wingPoint = 283
    widthPoint = 533

    print(_upperRightX, _upperRightY, cutPoint)

    page.cropBox.lowerLeft = (_upperRightX - cutPoint - wingPoint - widthPoint, cutPoint)
    page.cropBox.upperRight = (_upperRightX - cutPoint - wingPoint, _upperRightY - cutPoint)
    pdf_writer.addPage(page)

    with open(os.path.join(outputDirName, "앞표지_" + item), "wb") as f:
        pdf_writer.write(f)
