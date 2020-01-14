# Combine PDF in cwd into single PDF

import PyPDF2
import os

# Get PDF file names
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages excluding the first
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save result to file
pdfOutput = open('Combined.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
