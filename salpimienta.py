from PIL import Image
from sys import argv
import math, time
from random import randrange, random

class Filtro(object):
    """docstring for Filtro"""
    def __init__(self, fileName):
        self.img = Image.open(fileName)
        self.pixel = self.img.load()
        
    def grayScale(self):
        start = time.time()
        w, h = self.img.size
        
        for i in range(w):
            for j in range(h):
                r = self.pixel[i,j][0]
                g = self.pixel[i,j][1]
                b = self.pixel[i,j][2]
                media = (r+g+b)/3
                self.pixel[i,j] = (media, media, media)

        self.img.save('grayScale.png', 'PNG')
        end = time.time()
        
        print 'Tiempo tomado: '+str(end-start)
        return self.img

    def blurFilter(self, repeticiones):
        w, h =  self.img.size
        self.pixel = self.img.load()
        if(repeticiones == None): repeticiones = 5
        for n in range(repeticiones):
            for i in range(w):
                for j in range(h):
                    array_prom = []
                    if(i-1 >= 0):
                        array_prom.append(self.pixel[i-1,j][0])
                    if(i+1 < w):
                        array_prom.append(self.pixel[i+1,j][0])
                    if(j-1 >= 0):
                        array_prom.append(self.pixel[i,j-1][0])
                    if(j+1 < h):
                        array_prom.append(self.pixel[i,j+1][0])
                    npixel = sum(array_prom)/len(array_prom)
                    self.pixel[i,j] = (npixel, npixel, npixel)

        self.img.save('blurFilter.png', 'PNG')
        return selg.img
        
    def sal_pimienta(self, inensidad):
        start = time.time()
        w, h = self.img.size
        self.pixel = self.img.load()
        intesidad = 0.01
        for i in range(w):
            for j in range(h):
                if(random() <= intesidad):
                    if(randrange(1,3) == 1):
                        self.pixel[i,j] = (0, 0, 0)
                    else:
                        self.pixel[i,j] = (255, 255, 255)                        
        self.img.save('salPimienta05.png', 'PNG')
        end = time.time()
        
        print 'Tiempo tomado: '+str(end-start)
        return self.img

    def remove_sal_pimienta(self):
        start = time.time()
        w, h = self.img.size
        self.pixel = self.img.load()
        for i in range(w):
            for j in range(h):
                p_a = []

                actual = []
                arriba = []
                abajo = []
                izq = []
                der = []

                actual = [self.pixel[i,j][0], self.pixel[i,j][1], self.pixel[i,j][2]]
                p_a.append(get_Media(actual, 1))
                
                if(i-1 >= 0):
                    izq = [self.pixel[i-1,j][0], self.pixel[i-1,j][1], self.pixel[i-1,j][2]]
                    p_a.append(get_Media(izq, 1))

                if(i+1 < w):
                    der = [self.pixel[i+1,j][0], self.pixel[i+1,j][1], self.pixel[i+1,j][2]]
                    p_a.append(get_Media(der, 1))

                if(j-1 >= 0):
                    arriba = [self.pixel[i,j-1][0], self.pixel[i,j-1][1], self.pixel[i,j-1][2]]
                    p_a.append(get_Media(arriba, 1))

                if(j+1 < h):
                    abajo = [self.pixel[i,j+1][0], self.pixel[i,j+1][1], self.pixel[i,j+1][2]]
                    p_a.append(get_Media(abajo, 1))                    
                
                p_a.sort()
                p = p_a[int(len(p_a)/2)]
                self.pixel[i,j] = (p, p, p)

        self.img.save('quitarSalPimienta.png', 'PNG')
        end = time.time()
        
        print 'Tiempo tomado: '+str(end-start)
        return self.img

def get_Media(lista, posicion):
    lista.sort()
    return lista[posicion]

def main():
    im = argv[1]

    imagen = Filtro(im)
    imagen.grayScale()
    imagen.sal_pimienta(5)
    imagen.remove_sal_pimienta()
main()
