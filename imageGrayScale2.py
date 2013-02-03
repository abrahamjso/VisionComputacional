from PIL import Image
from sys import argv
import numpy

def getImage(fileName):
    im = Image.open(fileName)
    rgb = im.convert('RGB')

    h, w = im.size[0]/2, im.size[1]/2
    size = (h,w)
    img = Image.new('RGB', size) #

    for i in range(0, im.size[0], 2):
        for j in range(0, im.size[1], 2):
            r = rgb.getpixel((i, j))[0]
            g = rgb.getpixel((i, j))[1]
            b = rgb.getpixel((i, j))[2]

            rr = rgb.getpixel((i+1, j))[0]
            gg = rgb.getpixel((i+1, j))[1]
            bb = rgb.getpixel((i+1, j))[2]

            rrr = rgb.getpixel((i, j+1))[0]
            ggg = rgb.getpixel((i, j+1))[1]
            bbb = rgb.getpixel((i, j+1))[2]

            rrrr = rgb.getpixel((i+1, j+1))[0]
            gggg = rgb.getpixel((i+1, j+1))[1]
            bbbb = rgb.getpixel((i+1, j+1))[2]

            nr = (r+rr+rrr+rrrr)/4
            ng = (g+gg+ggg+gggg)/4
            nb = (b+bb+bbb+bbbb)/4

            pixel = tuple([nr, ng, nb])

            img.putpixel((i, j), pixel)

    img.save('escala.png', 'PNG')

def main():
    getImage('a2.png')

main()
    
