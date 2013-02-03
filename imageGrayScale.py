from PIL import Image
from sys import argv

def getImage(fileName):
    im = Image.open(fileName)
    rgb = im.convert('RGB')
 
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            r = rgb.getpixel((i, j))[0]
            g = rgb.getpixel((i, j))[1]
            b = rgb.getpixel((i, j))[2]

            #escala de grises
            media = (r+g+b)/3
            
            #umbral checarlo o cambiarlo ya que varia
            if media > 150: media = 0
            else: media = 255
            #

            pixel = tuple([media, media, media])
            im.putpixel((i, j), pixel)

    im.save('a3.png', 'PNG')


def main():
    getImage('a2.png')

main()
    
