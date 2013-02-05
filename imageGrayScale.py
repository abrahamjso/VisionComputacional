from PIL import Image
from sys import argv

def getImage(fileName):
    im = Image.open(fileName)
    rgb = im.convert('RGB')

    #escala grises
    size = (im.size[0], im.size[1])
    img = Image.new('RGB', size)

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            r = rgb.getpixel((i, j))[0]
            g = rgb.getpixel((i, j))[1]
            b = rgb.getpixel((i, j))[2]

            #Escala de Grises
            media = (r+g+b)/3
            pixelg = tuple([media, media, media])
            img.putpixel((i, j), pixelg)            

            #Filtro Umbral
            if media > 127: media = 255
            else: media = 0
            
            pixelu = tuple([media, media, media])
            im.putpixel((i, j), pixelu)

    img.save('grayScale.png', 'PNG')
    im.save('umbral.png', 'PNG')

def main():
    getImage(argv[1])

main()
    
