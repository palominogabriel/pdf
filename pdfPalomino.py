from PIL import Image
from binascii import hexlify
import zlib

class pdf:

    def rgbImageFromBinary(self, binaryString, imgWidth, imgHeight):
        # from PIL import Image
        im = Image.new('RGB', (imgWidth, imgHeight))
        x = 0
        y = 0
        for rgb in range(0, len(binaryString), 3):
            # Gets the RGB colors from the decoded binary
            r = int(hexlify(binaryString[rgb]), 16)
            g = int(hexlify(binaryString[rgb + 1]), 16)
            b = int(hexlify(binaryString[rgb + 2]), 16)
            # Places each pixel in the correct place
            im.putpixel((x, y), (r, g, b))
            # Increment pixel position
            if x < imgWidth - 1:
                x += 1
            else:
                x = 0
                y += 1
                if y >= imgHeight:
                    break
        return im

    # Gets the number in front of myString parameter
    def getFromHeader(self, myString='', header=''):
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

    def extractImages(self, pdfPath, outputPath):
        pdf_file = open(pdfPath, 'rb')
        pdf_buffer = pdf_file.read()

        file_cursor = 0
        decompressed = 0

        while (True):
            # Checks compression algorithm
            FlateDecode = False
            fCount = -1
            DeviceRGB = False
            Depth8 = False

            # Find the stream and exit the loop case it doesn't find it
            streamStart = pdf_buffer.find("stream", file_cursor)
            if streamStart < 0:
                break
            else:
                streamStart += len('stream') + 1
            # Find endstream index
            streamEnd = pdf_buffer.find("endstream", streamStart) - 1
            if streamEnd < 0:
                print "Couldn't find end of stream!"
                break

            # Gets the stream header
            header = pdf_buffer[streamStart - 150:streamStart]

            # Checks if the header contains Height and Width (Indicates it is an image)
            iHeight = header.find('Height', 0)
            iWidth = header.find('Width', 0)
            if iHeight < 0 or iWidth < 0:
                file_cursor = streamEnd + len('endstream')
                continue

            # Gets the image width
            width = self.getFromHeader('Width', header)
            # Gets the image height
            height = self.getFromHeader('Height', header)
            # Gets the image depth
            BitsPerComponent = self.getFromHeader('BitsPerComponent', header)

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
                binary = pdf_buffer[streamStart:streamEnd]
                # FlateDecode may be applied multiple times
                for i in range(fCount):
                    binary = zlib.decompress(binary)

            im = None
            # Reconstructs the image from binary
            if DeviceRGB and Depth8:
                im = self.rgbImageFromBinary(binary, width, height)

            if im != None:
                file_write = open(outputPath + 'img' + str((decompressed + 1)) + '.png', 'wb')
                im.save(file_write, 'png')
                file_write.close()
                decompressed += 1

            file_cursor = streamEnd + len('endstream')

