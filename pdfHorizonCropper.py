import os
import copy
from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader

outputDirName = "./output" + \
    str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
os.mkdir(outputDirName)

for item in os.listdir("./original_pdf"):
    item_path = os.path.join("./original_pdf", item)
    print("item name is {}".format(item))
    print("file full path is {}".format(item_path))
    pdfLeft = PdfFileReader(open(item_path, 'rb'))
    pdfRight = PdfFileReader(open(item_path, 'rb'))

    numberLeftPages = pdfLeft.getNumPages()
    numberRightPages = pdfRight.getNumPages()
    print("{} file have {} pages".format(item, numberLeftPages))
    print("{} file have {} pages".format(item, numberRightPages))

    pdf_writer = PdfFileWriter()
    for i in range(numberLeftPages):
        pageLeft = pdfLeft.getPage(i)
        pageRight = pdfRight.getPage(i)

        _upperRightX = pageLeft.mediaBox.getUpperRight_x()
        _upperRightY = pageLeft.mediaBox.getUpperRight_y()

        pageLeft.cropBox.lowerLeft = (0, 0)
        pageLeft.cropBox.upperRight = (_upperRightX / 2, _upperRightY)
        pdf_writer.addPage(pageLeft)

        pageRight.cropBox.lowerLeft = (_upperRightX / 2, 0)
        pageRight.cropBox.upperRight = (_upperRightX, _upperRightY)
        pdf_writer.addPage(pageRight)

    with open(os.path.join(outputDirName, "output_" + item), "wb") as f:
        pdf_writer.write(f)
