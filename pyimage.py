import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sn
import copy

# ANOTACIONES: 
#   - Cambiar la clase para que los objetos se construyan con imagenes y no con path
#   - Cambiar la clase para que las funciones devuelvan PyImages y no imagenes
#   - Arreglar problema histogram_specification si se abre una imagen de distinto tamaño

class PyImage:
    def __init__(self, pil_image):
        self.image = pil_image
        self.update()
    
    def update(self):
        self.width, self.height = self.image.size
        if(self.image.mode != 'L'):
            self.grayscale()
        self.histogram = self.get_histogram()
        self.brightness = self.get_brightness()
        self.contrast = self.get_contrast()
        self.c_histogram = [None] * len(self.histogram)
        before = 0
        for i in range(len(self.histogram)):
            self.c_histogram[i] = self.histogram[i] + before
            before = self.c_histogram[i]

    @staticmethod
    def open(path):
        imagen = Image.open(path)
        pyimagen = PyImage(imagen)
        return pyimagen

    def show(self):
        self.image.show()

    def grayscale(self):
        image_copy = self.image.convert('L')
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.image.getpixel((i, j))
                gris = int(0.222*r + 0.70*g + 0.0071*b)
                image_copy.putpixel((i, j), gris)
        self.image = image_copy

    def set_brightness_contrast(self, new_brightness, new_contrast):
        a = new_contrast / self.contrast
        b = new_brightness - a * self.brightness
        LUT = [None] * len(self.histogram)
        for i in range(len(self.histogram)):
            LUT[i] = a * i + b
        image_copy = self
        for i in range(image_copy.width):
            for j in range(image_copy.height):
                gray_value = image_copy.getpixel((i, j))
                new_gray_value = int(LUT[gray_value])
                if(new_gray_value > 255):
                    new_gray_value = 255
                elif(new_gray_value < 0):
                    new_gray_value = 0
                image_copy.putpixel((i, j), new_gray_value)
        return image_copy

    def binary(self, umbral):
        LUT = [None] * len(self.histogram)
        for i in range(umbral):
            LUT[i] = 0
        for i in range(umbral, len(self.histogram)):
            LUT[i] = 255
        image_copy = self
        for i in range(image_copy.width):
            for j in range(image_copy.height):
                gray_value = image_copy.getpixel((i,j))
                new_gray_value = LUT[gray_value]
                image_copy.putpixel((i,j), new_gray_value)
        image_copy.update()
        return image_copy

    def linear_transformation(self, sections):
        image_copy = self
        for i in range(sections):
            print("Tramo " + str(i + 1))
            xi = int(input("Xi: "))
            xf = int(input("Xf: "))
            yi = int(input("Yi: "))
            yf = int(input("Yf: "))

            a = (yf - yi) / (xf - xi)
            b = yi - a * xi
            LUT = self.histogram
            for i in range(xi, xf):
                LUT[i] = a * i + b
        for i in range(self.width):
            for j in range(self.height):
                gray_value = image_copy.getpixel((i, j))
                new_gray_value = int(LUT[gray_value])
                image_copy.putpixel((i, j), new_gray_value)
        return image_copy

    def histogram_specification(self, reference_image_path):
        reference_image = PyImage.open(reference_image_path)
        reference_image.show_c_histogram()
        image_copy = self
        LUT = [None] * len(self.c_histogram)
        for i in range(len(self.c_histogram)):
            value = self.c_histogram[i]
            for j in range(len(reference_image.c_histogram)):
                current = reference_image.c_histogram[j]
                if(current == value or current > value):
                    new_gray_value = j
                    break
            LUT[i] = new_gray_value
        for i in range(self.width):
            for j in range(self.height):
                gray_value = image_copy.getpixel((i, j))
                new_gray_value = LUT[gray_value]
                image_copy.putpixel((i, j), new_gray_value)
        image_copy.update()
        return image_copy

    def difference(self, other_image):
        image_copy = self
        for i in range(self.width):
            for j in range(self.height):
                current_pixel = self.getpixel((i, j))
                other_pixel = other_image.getpixel((i, j))
                new_pixel = abs(current_pixel - other_pixel)
                image_copy.putpixel((i, j), new_pixel)
        image_copy.update()
        return image_copy

    def difference_map(self, other_image, umbral):
        image_copy = copy.deepcopy(self)
        image_copy.image = image_copy.image.convert('RGB')
        for i in range(self.width):
            for j in range(self.height):
                current_pixel = self.getpixel((i, j))
                other_pixel = other_image.getpixel((i, j))
                diff_pixel = abs(current_pixel - other_pixel)
                if(diff_pixel > umbral):
                    red_pixel = (255, 0, 0)
                    image_copy.putpixel((i, j), red_pixel)
                else:
                    current_pixel_rgb = (current_pixel, current_pixel, current_pixel)
                    image_copy.putpixel((i, j), current_pixel_rgb)
        return image_copy

    def max_gray(self):
        image_copy = self.image
        maximo = np.max(np.asarray(image_copy))
        return maximo

    def min_gray(self):
        image_copy = self.image
        minimo = np.min(np.asarray(image_copy))
        np.asarray(image_copy)
        return minimo

    def get_histogram(self):
        hist = self.image.histogram()
        return hist

    def show_histogram(self):
        plt.plot(self.histogram)
        plt.show()

    def show_c_histogram(self):
        plt.plot(self.c_histogram)
        plt.show()

    def get_brightness(self):
        result = 0
        for i in range(len(self.histogram)):
            result += self.histogram[i] * i
        result /= (self.width * self.height)
        return result

    def get_contrast(self):
        result = 0
        for i in range(len(self.histogram)):
            result += self.histogram[i] * (i - self.get_brightness())**2
        result /= (self.width * self.height)
        result = np.sqrt(result)

        return result

    def get_image(self):
        return self.image

    def getpixel(self, xy):
        return self.image.getpixel(xy)

    def putpixel(self, xy, pixel):
        self.image.putpixel(xy, pixel)

    def convert(self, mode):
        image_copy = self
        image_copy.image = image_copy.image.convert(mode)
        return image_copy
    
# imagen = PyImage.open(sys.argv[1])
# imagen.show()
# imagen2 = PyImage.open(sys.argv[2])
# imagen2.show()
# imagen.difference_map(imagen2, 20).show()
# other = imagen.histogram_specification(sys.argv[2])
# other_py_image = PyImage(other)
# other_py_image.show()
# other_py_image.show_c_histogram()
#print(imagen.min_gray())
#print(imagen.max_gray())
#imagen.linear_transformation(2).show()
#print(len(imagen.histogram))
