#!/bin/bash

CURR=$(pwd)'/'

if [[ $# -lt 2 ]]; then
	printf "(ERROR: Missing parameters)\nShould use: ./convertPDsF2TIFF.sh pdfFileName.pdf PageToConvertNumber\n"
else
	pdfFileNameExtension=$1
	pageToConvert=$2
	pdfPath=$(pwd)"/"$pdfFileNameExtension
	#pdfFileName=$(echo $pdfFileNameExtension | cut -f 1 -d '.')
	#pdfSize=$(pdftk ${pdfFileNameExtension} dump_data|grep NumberOfPages| awk '{print $2}')

	convert -density 300 ${pdfFileNameExtension}[${pageToConvert}] -depth 8 -background white -flatten +matte ${pdfFileNameExtension}[${pageToConvert}].tiff
	tesseract ${pdfFileNameExtension}[${pageToConvert}].tiff ${pdfFileNameExtension}[${pageToConvert}] -l por
	rm ${pdfFileNameExtension}[${pageToConvert}].tiff
fi