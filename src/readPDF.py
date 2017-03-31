import PyPDF2
import time
import os
import sys

# Get the program start time
start = time.time()

# Get current program directory
if (len(sys.argv[0].split('/')) > 1):
    path = sys.argv[0].replace(sys.argv[0].split('/')[-1],'')
else:
    path = os.getcwd()

# Check program file and parameters dependency
if (len(sys.argv) < 4):
    print('ERROR: Missing parameters!\n\n1st = Input PDF file path\n2nd = Output file path\n3rd = Output file name')
elif ('img2txt.sh' not in os.listdir(path)):
    print('ERROR: Missing file!\n\n"img2txt.sh"')
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

    pdfFileObj.close()
    txtFile.close()

    # Prints the program elapsed time
    print('ELAPSED TIME: ' + str(time.time() - start))