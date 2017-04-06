sample = '/home/palomino/Documents/pdf/Seige of Vicksburg Sample OCR.pdf'
giddens = '/home/palomino/Documents/pdf/Giddens_3pages.pdf'
book = '/home/palomino/Documents/pdf/dbBook.pdf'
imgdir = '/home/palomino/Documents/giddens_png/00.png'
texto = '/home/palomino/Documents/pdf/texto.pdf'
pngpdf = '/home/palomino/Documents/pdf/png2pdf.pdf'
catalogo = '/home/palomino/Documents/pdf/pdfs/FatecCatalogo.pdf'
pp = '/home/palomino/Documents/pdf/powerPoint.pdf'
test16 = '/home/palomino/Documents/Image Samples/480x360/16BIT/test16.pdf'

from pdfPalomino import pdf
import zlib


pdf().extractImages(pp, '/home/palomino/Documents/output/04.06/')