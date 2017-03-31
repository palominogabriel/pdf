import base64
import imghdr
import PyPDF2

import io

sample = '/home/palomino/Documents/pdf/Seige of Vicksburg Sample OCR.pdf'
giddens = '/home/palomino/Documents/pdf/Giddens.pdf'
book = '/home/palomino/Documents/pdf/dbBook.pdf'

t1 = open('/home/palomino/Documents/giddens_png/00.png','rb').read()
print imghdr.what(None,t1)

dst_pdf = PyPDF2.PdfFileWriter()

pdf2 = open(book, 'rb')
pdf = file(book, 'rb').read()

startmark = "\xff\xd8"
startfix = 0
endmark = "\xff\xd9"
endfix = 2
i = 0

flag = True

njpg = 0
while True:
    istream = pdf.find("stream", i)

    if istream < 0:
        break
    iendstream = pdf.find("endstream",istream)

    image_raw = pdf2.read(istream+len('stream'))
    print image_raw

    for j in range((istream+1),iendstream) :
        image_raw += pdf2.read(j)

   # x = open(base64.b64encode(image_raw),'rb', buffering=-1).read()

    img = PIL.Image.open(image_raw)
    img.show()
    '''
    pdf_bytes = io.BytesIO()
    dst_pdf.
    dst_pdf.write(pdf[(istream+len('stream')):(iendstream-len('endstream'))])
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)
    print pdf_bytes
    '''

    #image_raw = base64.b64decode(pdf[(istream+len('stream')):(iendstream-len('endstream'))])

    imghdr.what('',h=x)
    istart = pdf.find(startmark, istream, istream + 20)
    if (flag):
        #print pdf[istream:(istream+20)]
        flag = False
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend - 20)
    if iend < 0:
        raise Exception("Didn't find end of JPG!")

    istart += startfix
    iend += endfix
    #print "JPG %d from %d to %d" % (njpg, istart, iend)
    jpg = pdf[istart:iend]
    print imghdr.what(jpg)

    njpg += 1
    i = iend

