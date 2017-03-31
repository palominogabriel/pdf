import PyPDF2
import time
import os
import sys

from wand.image import Image
from PIL import Image as PI
import io
import pytesseract

# Get the program start time
start = time.time()

def pdf_page_to_jpeg(src_pdf, pagenum = 0, resolution = 72, ):
    """
    Returns specified PDF page as wand.image.Image png.
    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
    :param int pagenum: Page number to take.
    :param int resolution: Resolution for resulting png in DPI.
    """
    pdfReader = PyPDF2.PdfFileReader(src_pdf)

    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(pdfReader.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file = pdf_bytes, resolution = resolution)
    img.convert("jpeg")

    return img

# Get current program directory
if (len(sys.argv[0].split('/')) > 1):
    path = sys.argv[0].replace(sys.argv[0].split('/')[-1],'')
else:
    path = os.getcwd()

# Check program file and parameters dependency
if (len(sys.argv) < 4):
    print('ERROR: Missing parameters!\n\n1st = Input PDF file path\n2nd = Output file path\n3rd = Output file name')
else:
    # Output file path
    oFileName = sys.argv[3]
    outputPath = sys.argv[2]
    oFilePath = outputPath + oFileName

    # Input file path
    iFileName = sys.argv[1].split('/')[-1]
    iFilePath = sys.argv[1]

    # Open input file
    pdfFileObj = open(iFilePath, 'rb')

    # Read PDF file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Create output file
    txtFile = open(oFilePath, 'wb+')

    # Read the entire PDF page by page
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i) # Get pdf page
        # Verify if the PDF page has an Image attribute
        print str(pageObj)
        '''
        if 'Im'  in str(pageObj):
            print 'Image found at page ' + str((i+1))
            print 'Converting PDF page ' + str((i+1)) + ' to JPEG...'
            image_pdf_page = pdf_page_to_jpeg(src_pdf=iFilePath, pagenum=i, resolution=300)

            print 'Converting image to text (Tesseract-OCR)...'
            img_page = Image(image=image_pdf_page).convert('RGB')
            img_page.save(filename='page'+str(i+1)+'.jpeg')
            req_image = img_page.make_blob(format='jpeg')

            txt = pytesseract.image_to_string(PI.open(io.BytesIO(req_image)), lang='por')
            txtFile.write(txt)
            print 'Page ' + str((i+1)) + ' DONE!'
        '''

        # Write the page text to the output text file
        txtFile.write(pageObj.extractText().replace('\n',' ').encode('utf-8'))

    pdfFileObj.close()
    txtFile.close()

    # Prints the program elapsed time
    print('ELAPSED TIME: ' + str(time.time() - start))


'''
Convert and Tesseract with python wrapers
#######################

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[1]

req_image = []
final_text = []

image_pdf = Image(filename=iFilePath, resolution=300)
image_jpeg = image_pdf.convert('jpeg')

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

    for img in req_image:
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)

txtFile.write(str(final_text))

#######################
'''

'''
Convert and Tesseract-OCR via shell script
#######################

# Read the entire PDF page by page
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i) # Get pdf page
        # Verify if the PDF page has an Image attribute
        if 'image' or 'im'  in str(pageObj).lower():
            # Runs script that read the PDF page that contains an image and runs Tesseract OCR
            # to extract the text from the image
            os.system('bash ' + path + '/' + 'img2txt.sh ' + iFilePath + ' ' + str(i))
            # Reads the created output file from the script containing the extracted text
            fp = open(iFilePath + '[' + str(i) + '].txt', 'rb')
            # Writes the script output file, to the final output file
            for line in fp:
                txtFile.write(line)
            fp.close()
            # Remove from disk the script output file
            os.system('rm ' + iFilePath + '[' + str(i) + '].txt')
        # Write the page text to the output text file
        txtFile.write(pageObj.extractText().replace('\n',' ').encode('utf-8'))

#######################
'''

'''
Last Work backup
#######################
 # Read the entire PDF page by page
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i) # Get pdf page
        # Verify if the PDF page has an Image attribute
        if 'image' or 'im'  in str(pageObj).lower():
            print 'There is an image'
            #req_image = []
            final_text = []

            #image_pdf = Image(filename=iFilePath, resolution=300)
            #image_pdf = Image(image=pageObj, resolution=300)
            print 'PDF file loaded\nLoading PDF page...'
            #image_pdf_page = image_pdf.sequence[i]
            image_pdf_page = pdf_page_to_png(src_pdf=iFilePath,pagenum=i,resolution=72)
            #print 'PDF page Loaded\nConverting to JPEG...'
            #image_jpeg = image_pdf_page.convert('jpeg')
            #print 'Convertion successful!'

            print 'Loading PNG Blob...'
            img_page = Image(image=image_pdf_page)
            req_image = img_page.make_blob(format='png')

            print 'Converting image to text (Tesseract-OCR)...'
            txt = pytesseract.image_to_string(
                PI.open(io.BytesIO(req_image)),
                lang='por'
            )
            print 'Convertion successful\nWriting in output file...'
            txtFile.write(txt)
            print 'Page ' + str(i) + ' DONE!'

        # Write the page text to the output text file
        txtFile.write(pageObj.extractText().replace('\n',' ').encode('utf-8'))

#######################
'''