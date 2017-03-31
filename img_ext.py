import imghdr
import StringIO

sample = '/home/palomino/Documents/pdf/Seige of Vicksburg Sample OCR.pdf'
giddens = '/home/palomino/Documents/pdf/Giddens_3pages.pdf'
book = '/home/palomino/Documents/pdf/dbBook.pdf'
imgdir = '/home/palomino/Documents/giddens_png/00.png'
texto = '/home/palomino/Documents/pdf/texto.pdf'
pngpdf = '/home/palomino/Documents/pdf/png2pdf.pdf'
catalogo = '/home/palomino/Documents/pdf/pdfs/FatecCatalogo.pdf'
pp = '/home/palomino/Documents/pdf/powerPoint.pdf'

#pdf = file(giddens,'rb').read()

#istream = pdf.find('stream',0)
#iendstream = pdf.find('endstream',istream)

pdf = file(pp, "rb").read()

startmark = "\xff\xd8\xff"
startfix = 0
endmark = "\xff\xd9"
endfix = 2
i = 0

njpg = 0
while True:
    istream = pdf.find("stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    #iend = pdf.find(endmark, iend - 20)
    #if iend < 0:
    #    raise Exception("Didn't find end of JPG!")

    istart += startfix
    #iend += endfix
    print "JPG %d from %d to %d" % (njpg, istart, iend)
    print imghdr.what(StringIO.StringIO(pdf[istart:iend]))
    jpg = pdf[istart:iend]
    jpgfile = file("jpg%d.jpg" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()

    njpg += 1
    i = iend


'''

pdf = file(book, "rb").read()

startmark = "\xff\xd8\xff"
startfix = 0
endmark = "\xff\xd9"
endfix = 2
i = 0

njpg = 0
while True:
    istream = pdf.find("stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
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
    print "JPG %d from %d to %d" % (njpg, istart, iend)
    print imghdr.what(StringIO.StringIO(pdf[istart:iend]))
    jpg = pdf[istart:iend]
    jpgfile = file("jpg%d.jpg" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()

    njpg += 1
    i = iend

'''

#######################
# GIF 1
startmark = "\x47\x49\x46\x38\x37\x61"
startfix = 0
endmark = "\x00\x3B"
endfix = 2
i = 0

njpg = 0
while True:
    print 'In gif loop'
    istream = pdf.find("stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend - 20)
    if iend < 0:
        raise Exception("Didn't find end of GIF!")

    istart += startfix
    iend += endfix
    print "GIF %d from %d to %d" % (njpg, istart, iend)
    print imghdr.what(StringIO.StringIO(pdf[istart:iend]))
    jpg = pdf[istart:iend]
    jpgfile = file("gif%d.gif" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()

    njpg += 1
    i = iend

#######################
# GIF 2
startmark = "\x47\x49\x46\x38\x39\x61"
startfix = 0
endmark = "\x00\x3B"
endfix = 2
i = 0

njpg = 0
while True:
    print 'In gif2 loop'
    istream = pdf.find("stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend - 20)
    if iend < 0:
        raise Exception("Didn't find end of GIF!")

    istart += startfix
    iend += endfix
    print "GIF %d from %d to %d" % (njpg, istart, iend)
    print imghdr.what(StringIO.StringIO(pdf[istart:iend]))
    jpg = pdf[istart:iend]
    jpgfile = file("gif%d.gif" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()

    njpg += 1
    i = iend

#######################
# PNG
startmark = "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
startfix = 0
endmark = "\x49\x45\x4E\x44\xAE\x42\x60\x82"
endfix = 2
i = 0

njpg = 0
while True:
    print 'In png loop'
    istream = pdf.find("stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend - 20)
    if iend < 0:
        raise Exception("Didn't find end of PNG!")

    istart += startfix
    iend += endfix
    print "PNG %d from %d to %d" % (njpg, istart, iend)
    print imghdr.what(StringIO.StringIO(pdf[istart:iend]))
    jpg = pdf[istart:iend]
    jpgfile = file("gif%d.png" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()

    njpg += 1
    i = iend

#######################
# JB2
startmark = "\x97\x4A\x42\x32\x0D\x0A\x1A\x0A"
startfix = 0
endmark = "\x03\x33\x00\x01\x00\x00\x00\x00"
endfix = 2
i = 0

njpg = 0
while True:
    print 'In jb2 loop'

    istream = pdf.find("stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find("endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend - 20)
    if iend < 0:
        raise Exception("Didn't find end of JB2!")

    istart += startfix
    iend += endfix
    print "JB2 %d from %d to %d" % (njpg, istart, iend)
    print imghdr.what(StringIO.StringIO(pdf[istart:iend]))
    jpg = pdf[istart:iend]
    jpgfile = file("jb2%d.jb2" % njpg, "wb")
    jpgfile.write(jpg)
    jpgfile.close()

    njpg += 1
    i = iend



'''

for i in range(44):
    print (t1[istream + len('stream') + 1:iendstream])

    istream = t1.find('stream', iendstream)
    iendstream = t1.find('endstream', istream)
    print imghdr.what(None,t1[istream+len('stream')+1:iendstream])

#t2 = t1[0:]

#print imghdr.what(None,t2)
'''