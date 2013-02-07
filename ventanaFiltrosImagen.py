from Tkinter import * 
from PIL import ImageTk, Image
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

        self.img.save('grayScale.png', 'PNG')
        return self.img

    def grayScaleMax(self):
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                
                pixel = max(self.rgb.getpixel((i, j)))
                
                pixel = tuple([pixel, pixel, pixel])
                self.img.putpixel((i, j), pixel)            

        self.img.save('grayScaleMax.png', 'PNG')
        return self.img

    def grayScaleMin(self):
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                
                pixel = min(self.rgb.getpixel((i, j)))
                
                pixel = tuple([pixel, pixel, pixel])
                self.img.putpixel((i, j), pixel)            

        self.img.save('grayScaleMin.png', 'PNG')
        return self.img

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
        return self.img

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
        return self.img


path_image = sys.argv[1]
debug = True
imagen = Filtro(path_image)#Instanciamos la imagen de la clase filtro

def main():
    window()

def window():
	root = Tk()
	frame = Frame()
	frame.pack(fill=X, padx=5, pady=5)
	root.title("Imagen Original")

	call(Image.open(path_image)) #Ponemos la imagen original

	panel1 = Button(text="Original", command=original)
	panel1.pack(in_=frame, side=LEFT)

	panel2 = Button(text="GrayScale", command=grayScale)
	panel2.pack(in_=frame, side=LEFT)

	panel3 = Button(text="GrayScaleMin", command=grayScaleMin)
	panel3.pack(in_=frame, side=LEFT)

	panel4 = Button(text="GrayScaleMax", command=grayScaleMax)
	panel4.pack(in_=frame, side=LEFT)
	
	panel5 = Button(text="BinaryScale", command=binaryScale)
	panel5.pack(in_=frame, side=LEFT)

	panel6 = Button(text="Negative", command=negativeScale)
	panel6.pack(in_=frame, side=LEFT)
	
	root.mainloop()

def call(im): #Metodo que limpia la ventana para poner la nueva imagen
    global panel
    img = ImageTk.PhotoImage(im)
    panel = Label(image = img)
    panel.pict = img
    panel.pack() 

def original(): #Metodo del Boton para llamar la imagen Original
	panel.destroy()   #Destruimos el panel para poner la nueva
	return call(Image.open(path_image)) 

def grayScale(): #Metodo del Boton para llamar la escala de grises
	global imagen
	panel.destroy()
	call(imagen.grayScale()) # de nuestro objeto imagen mandamos llamar la funcion

def grayScaleMin(): #Metodo del Boton para llamar la escala de grises de min
	global imagen
	panel.destroy()
	call(imagen.grayScaleMin())

def grayScaleMax(): #Metodo del Boton para llamar la escala de grises de max
	global imagen
	panel.destroy()
	call(imagen.grayScaleMax())

def binaryScale(): #Metodo del Boton para llamar la escala binaria
	global imagen
	panel.destroy()
	call(imagen.binaryScale(None))

def negativeScale(): #Metodo del Boton para llamar la imagen en negativo
	global imagen
	panel.destroy()
	call(imagen.negativeScale())

if __name__ == '__main__':
    main()