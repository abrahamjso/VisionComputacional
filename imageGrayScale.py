import Tkinter, ImageTk
from PIL import Image
from sys import argv

class Filtro(object):
    """docstring for Filtro"""
    def __init__(self, fileName):
        self.img = Image.open(fileName)
        self.rgb = self.img.convert('RGB')

    def grayScale(self):
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                r = self.rgb.getpixel((i, j))[0]
                g = self.rgb.getpixel((i, j))[1]
                b = self.rgb.getpixel((i, j))[2]
                
                media = (r+g+b)/3
                pixel = tuple([media, media, media])
                self.img.putpixel((i, j), pixel)            

        #ventana = Tkinter.Tk()
        #im2 = ImageTk.PhotoImage(self.img)
        #Tkinter.Label(ventana, image=im2).pack()
        #ventana.mainloop()

        self.img.save('grayScale.png', 'PNG')

    def grayScaleMax(self):
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                
                pixel = max(self.rgb.getpixel((i, j)))
                
                pixel = tuple([pixel, pixel, pixel])
                self.img.putpixel((i, j), pixel)            

        self.img.save('grayScaleMax.png', 'PNG')

    def grayScaleMin(self):
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                
                pixel = min(self.rgb.getpixel((i, j)))
                
                pixel = tuple([pixel, pixel, pixel])
                self.img.putpixel((i, j), pixel)            

        self.img.save('grayScaleMin.png', 'PNG')

    def binaryScale(self, umbral):
        if(umbral == None): umbral = 122
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                r = self.rgb.getpixel((i, j))[0]
                g = self.rgb.getpixel((i, j))[1]
                b = self.rgb.getpixel((i, j))[2]
                
                media = (r+g+b)/3
                pixel = tuple([media, media, media])
                self.img.putpixel((i, j), pixel)            

                if media > umbral: media = 255
                else: media = 0

                pixel = tuple([media, media, media])
                self.img.putpixel((i, j), pixel)

        self.img.save('BinaryScale.png', 'PNG')

    def negativeScale(self):
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                r = self.rgb.getpixel((i, j))[0]
                g = self.rgb.getpixel((i, j))[1]
                b = self.rgb.getpixel((i, j))[2]
                
                nr = 255 - r
                ng = 255 - g
                nb = 255 - b
                pixel = tuple([nr, ng, nb])
                self.img.putpixel((i,j), pixel)

        self.img.save('negativeScale.png', 'PNG')

    def blur(self, maxiter):
        if(maxiter == None): maxiter = 10

        iter = 0
        while iter < maxiter:
            print "Iteracion: ", iter
            for i in range(self.img.size[0]):
                for j in range(self.img.size[1]):
                    prom = []
                    k=0
                    pixel=self.img.getpixel((i, j))[0]
                    if(i-1>=0):
                        prom.append(self.img.getpixel((i-1, j))[0])
                        k+=1
                    if(i+1<self.img.size[0]):
                        prom.append(self.img.getpixel((i+1, j))[0])
                        k+=1
                    if(j+1<self.img.size[1]):
                        prom.append(self.img.getpixel((i, j+1))[0])
                        k+=1
                    if(j-1>=0):
                        prom.append(self.img.getpixel((i, j-1))[0])
                        k+=1
                    promedio = 0;
                    for valor in prom:
                        promedio+=valor
                    promedio=promedio/k
                    self.img.putpixel((i,j), (promedio,promedio,promedio))            
            iter+=1

        self.img.save('blurFilter.png', 'PNG')


def main():
    imagen = Filtro(argv[1])
    imagen.blur(None)
    imagen.grayScale()
    imagen.grayScaleMax()
    imagen.grayScaleMin()
    imagen.binaryScale(None)
    imagen.negativeScale()

main()