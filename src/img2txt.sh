#!/bin/bash

# Gets the current directory and concatenates '/' at the end
CURR=$(pwd)'/'

# Checks the parameters
if [[ $# -lt 2 ]]; then
	printf "ERROR: Missing parameters!\n\n1st - PDF file path.\n2nd - Page number to convert.\n"
else
	# Get the paremeters
	pdfFileNameExtension=$1
	pageToConvert=$2

	# Converts the PDF page to a temporary .tiff image (Using ImageMagick)
	convert -density 72 ${pdfFileNameExtension}[${pageToConvert}] -depth 8 -background white -flatten +matte ${pdfFileNameExtension}[${pageToConvert}].tiff
	# Apply Tesseract-OCR and generates a temporary .txt output (Using Tesseract-OCR)
 	tesseract ${pdfFileNameExtension}[${pageToConvert}].tiff ${pdfFileNameExtension}[${pageToConvert}] -l por
 	# Remove the previous created .tiff file
	rm ${pdfFileNameExtension}[${pageToConvert}].tiff
fi