from PIL import Image
from binascii import hexlify

binImg = '/home/palomino/Documents/output/03.29/decompressed2'
rgb = '/home/palomino/Documents/output/03.29/rgb3'
output = '/home/palomino/Documents/output/03.29/'

bin = open(binImg, 'rb')
binBuffer = bin.read()

img = Image.new('RGB', (1009,471))

x = 0
y = 0
size = 1009*471*3
#print len(binBuffer)
#print size

for i in range(0,len(binBuffer),3):
    r=int(hexlify(binBuffer[i]), 16)
    g=int(hexlify(binBuffer[i+1]), 16)
    b=int(hexlify(binBuffer[i+2]), 16)

    try:
        img.putpixel((x,y),(r,g,b))
    except IndexError:
        print str(i) + 'r=' + str(r) + 'g=' + str(g) + 'b=' + str(b)

    if x < 1008:
        x += 1
    else:
        x = 0
        y += 1
        if y >= 471:
            break

file_writer = open(output + 'img.tiff', 'wb')
img.save(output + 'img.tiff','tiff')
