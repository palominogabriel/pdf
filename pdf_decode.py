import io

import StringIO
import pytesseract
from wand.image import Image as wImage
import math
sample = '/home/palomino/Documents/pdf/Seige of Vicksburg Sample OCR.pdf'
giddens = '/home/palomino/Documents/pdf/Giddens_3pages.pdf'
book = '/home/palomino/Documents/pdf/dbBook.pdf'
imgdir = '/home/palomino/Documents/giddens_png/00.png'
texto = '/home/palomino/Documents/pdf/texto.pdf'
pngpdf = '/home/palomino/Documents/pdf/png2pdf.pdf'
catalogo = '/home/palomino/Documents/pdf/pdfs/FatecCatalogo.pdf'
pp = '/home/palomino/Documents/pdf/powerPoint.pdf'
test16 = '/home/palomino/Documents/Image Samples/480x360/16BIT/test16.pdf'

# Gets the number in front of myString parameter
def getFromHeader(myString='', header=''):
    index = header.find(myString)
    if index < 0:
        return index

    sValue = header[index + len(myString) + 1:]
    ssValue = ''
    count = 0
    for c in sValue:
        if c in '0123456789':
            ssValue += c
        else:
            count += 1
        if count > 2:
            break
    if ssValue == '':
        return -1
    else:
        return int(ssValue)

import zlib
#import sys
from PIL import Image
from binascii import hexlify

#args = sys.argv

#if len(args) < 3:
#    print ('ERROR: Missing arguments!\nUsage: \n' + args[0] + '1 - Input PDF file path\n2 - Output file')
#else:
#    input = args[1]
#    output = args[2]



file_read = open(test16, 'rb')
buffer = file_read.read()

file_cursor = 0
decompressed = 0

while(True):
    # Checks compression algorithm
    FlateDecode = False
    fCount = -1
    DeviceRGB = False
    Depth8 = False

    # Find the stream and exit the loop case it doesn't find it
    streamStart = buffer.find("stream", file_cursor)
    if streamStart < 0:
        break
    else:
        streamStart += len('stream') + 1
    # Find endstream index
    streamEnd = buffer.find("endstream", streamStart) - 1
    if streamEnd < 0:
        print "Couldn't find end of stream!"
        break

    # Gets the stream header
    header = buffer[streamStart-150:streamStart]

    # Checks if the header contains Height and Width (Indicates it is an image)
    iHeight = header.find('Height', 0)
    iWidth = header.find('Width', 0)
    if iHeight < 0 or iWidth < 0:
        file_cursor = streamEnd + len('endstream')
        continue

    # Gets the image width
    width = getFromHeader('Width', header)
    # Gets the image height
    height = getFromHeader('Height', header)
    # Gets the image depth
    BitsPerComponent = getFromHeader('BitsPerComponent',header)

    # Checks the compression algorithm
    if 'FlateDecode' in header:
        FlateDecode = True
        fCount = header.count('FlateDecode')  # Gets how many times FlateDecode is applied
    # Checks the colorspace
    if 'DeviceRGB' in header:
        DeviceRGB = True
    # Checks image depth
    if BitsPerComponent == 8:
        Depth8 = True

    # Decode FlateDecode compressed image
    if FlateDecode:
        binary = buffer[streamStart:streamEnd]
        # FlateDecode may be applied multiple times
        for i in range(fCount):
            binary = zlib.decompress(binary)

    im = None
    # Reconstructs the image from binary
    if DeviceRGB and Depth8:
        im = Image.new('RGB',(width,height))
        x = 0
        y = 0
        for rgb in range(0,len(binary),3):
            # Gets the RGB colors from the decoded binary
            r = int(hexlify(binary[rgb]), 16)
            g = int(hexlify(binary[rgb + 1]), 16)
            b = int(hexlify(binary[rgb + 2]), 16)
            # Places each pixel in the correct place
            im.putpixel((x,y),(r,g,b))
            # Increment pixel position
            if x < width-1:
                x += 1
            else:
                x = 0
                y += 1
                if y >= height:
                    break
        #im = im.resize((width*2, height*2), Image.ANTIALIAS)
        #im = im.convert('L')
        #txt = pytesseract.image_to_string(
        #    im,
        #    lang='por'
        #)
       # print txt
    if im != None:
        file_write = open('/home/palomino/Documents/output/03.31/decompressed' + str((decompressed + 1)) + '.png', 'wb')
        im.save(file_write,'png')
        file_write.close()
        decompressed += 1
    file_cursor = streamEnd + len('endstream')

#decompress = zlib.decompress(buffer)
#file_write = open(output, 'w')
#file_write.write(decompress)