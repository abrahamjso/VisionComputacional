from PIL import ImageTk, Image
from sys import argv
import math, time

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

    def border_image(self, typeMask):
        w, h = self.img.size
        self.pixel = self.img.load()
        
        if(typeMask == 1 or typeMask == None): #Escogemos el tipo de Mascara a aplicar ya sea Sobel en x & y o Prewitt en x & y
            MascaraX, MascaraY = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]), ([1, 2, 1], [0, 0, 0], [-1, -2, -1])  # Sobel
            nameImage = 'borderTest.png'
        else:
            MascaraX, MascaraY = ([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]), ([1, 1, 1], [0, 0, 0], [-1, -1, -1])  #Prewitt
            nameImage = 'borderPrewitt.png'
        
        for i in range(w):
            for j in range(h):
                gX = self.matrixMult(i, j, MascaraX) #Hacemos la multiplicacion de la matrix en x escogida por el pixel seleccionado
                gY = self.matrixMult(i, j, MascaraY) #Hacemos la multiplicacion de la matrix en y escogida por el pixel seleccionado
                    
                g = int(math.sqrt(gX + gY)) #Aplicamos la formula para obtener el gradiente
                    
                self.pixel[i,j] = (g, g, g) #nuevo Pixel creado   
  
        self.img.save(nameImage)

    def matrixMult(self, x, y, matrix): #Funcion donde hacemos la multiplicacion de matrices
        suma = 0   
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                try:
                    suma += matrix[i][j]*self.pixel[x+i, y+j][0] #Vamos sumando el resultado de la multiplicacion de la mascara seleccionada a nuestro pixel actual
                except:
                    suma += 0 #Sumamos 0 en dado caso que nos salgamos de la posicion
                 
        return pow(suma, 2) #Aplicamos formula, al regresar la potencia de la matriz obtenida  
        
def main():
	im = argv[1]

	imagen = Filtro(im)
	imagen.grayScale()
    imagen.blurFilter(None)
	imagen.border_image(None)
	
main()
