import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sn
import math
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
        self.histogram = self.image.histogram()
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

    def save(path):
        self.image.save(path)

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
        image_copy = copy.deepcopy(self)
        for i in range(image_copy.width):
            for j in range(image_copy.height):
                gray_value = image_copy.getpixel((i, j))
                new_gray_value = int(LUT[gray_value])
                if(new_gray_value > 255):
                    new_gray_value = 255
                elif(new_gray_value < 0):
                    new_gray_value = 0
                image_copy.putpixel((i, j), new_gray_value)
        image_copy.update()
        return image_copy

    def binary(self, umbral, H, L):
        LUT = [None] * len(self.histogram)
        for i in range(umbral):
            LUT[i] = L
        for i in range(umbral, len(self.histogram)):
            LUT[i] = H
        image_copy = copy.deepcopy(self)
        for i in range(image_copy.width):
            for j in range(image_copy.height):
                gray_value = image_copy.getpixel((i,j))
                new_gray_value = LUT[gray_value]
                image_copy.putpixel((i,j), new_gray_value)
        image_copy.update()
        return image_copy

    def linear_transformation(self, sections):
        image_copy = copy.deepcopy(self)
        for i in range(0, len(sections), 4):
            print("Tramo " + str(i + 1))
            xi = sections[i]
            xf = sections[i+1]
            yi = sections[i+2]
            yf = sections[i+3]

            a = (yf - yi) / (xf - xi)
            b = yi - a * xi
            LUT = list(range(256))
            for i in range(xi, xf):
                LUT[i] = int(a * i + b)
            print(LUT)
        for i in range(self.width):
            for j in range(self.height):
                gray_value = self.getpixel((i, j))
                new_gray_value = int(LUT[gray_value])
                image_copy.putpixel((i, j), new_gray_value)
        image_copy.update()
        return image_copy

    def equalize(self):
        image_copy = copy.deepcopy(self)
        LUT = [None] * len(self.histogram)
        for i in range(len(self.histogram)):
            LUT[i] = max(0, int(256 / (self.width * self.height) * self.c_histogram[i])- 1)
        for i in range(self.width):
            for j in range(self.height):
                current_value = self.getpixel((i,j))
                new_value = LUT[current_value]
                image_copy.putpixel((i, j), new_value)
        image_copy.update()
        return image_copy

    def histogram_specification(self, reference_image):
        image_copy = copy.deepcopy(self)
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

    def gamma_correction(self, gamma):
        image_copy = copy.deepcopy(self)
        LUT = [None] * len(self.histogram)
        for i in range(len(LUT)):
            LUT[i] = int(i ** gamma)
        for i in range(self.width):
            for j in range(self.height):
                gray_value = self.getpixel((i, j))
                new_gray_value = LUT[gray_value]
                image_copy.putpixel((i, j), new_gray_value)
        image_copy.update()
        return image_copy

    def difference(self, other_image):
        image_copy = copy.deepcopy(self)
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

    def vertical_flip(self):
        image_copy = copy.deepcopy(self)
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.getpixel((i, j))
                image_copy.putpixel((self.width - 1 - i, j), pixel)
        image_copy.update()
        return image_copy

    def horizontal_flip(self):
        image_copy = copy.deepcopy(self)
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.getpixel((i, j))
                image_copy.putpixel((i, self.height - 1 - j), pixel)
        image_copy.update()
        return image_copy

    def transpose(self):
        image_copy = copy.deepcopy(self)
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.getpixel((i, j))
                image_copy.putpixel((j, i), pixel)
        image_copy.update()
        return image_copy

    def ninety_rotation(self):
        image_copy = copy.deepcopy(self)
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.getpixel((i, j))
                image_copy.putpixel((self.height - 1 - j, i), pixel)
        image_copy.update()
        return image_copy

    def resize(self, x_resize, y_resize, mode):
        new_width = x_resize * self.width // 100
        new_height = y_resize * self.height // 100

        new_pil_image = Image.new('L', (new_width, new_height))
        new_image = PyImage(new_pil_image)
        # mode = 0 => vecino más cercano
        # mode = 1 => bilineal
        if(not mode):
            for i in range(new_image.width):
                for j in range(new_image.height):
                    new_x = int(i / (x_resize / 100))
                    new_y = int(j / (y_resize / 100))
                    pixel = self.getpixel((new_x, new_y))
                    new_image.putpixel((i, j), pixel)
        else:
            for i in range(new_image.width):
                for j in range(new_image.height):
                    x = i / (x_resize / 100)
                    y = j / (y_resize / 100)
                    X = i // (x_resize / 100)
                    Y = j // (y_resize / 100)
                    p = x - X
                    q = y - Y
                    A = self.getpixel((X, Y + 1))
                    B = self.getpixel((X + 1, Y + 1))
                    C = self.getpixel((X, Y))
                    D = self.getpixel((X + 1, Y))
                    pixel = int(C + (D - C) * p + (A - C) * q + (B + C - A - D) * p * q)
                    new_image.putpixel((i, j), pixel)
        return new_image

    def max_gray(self):
        image_copy = self.image
        maximo = np.max(np.asarray(image_copy))
        return maximo

    def min_gray(self):
        image_copy = self.image
        minimo = np.min(np.asarray(image_copy))
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

    def get_entropy(self):
        result = 0 
        for i in range(len(self.histogram)):
            p = self.histogram[i] / self.width * self.height
            if(p == 0):
                p = 0.001
            result += p * math.log(p, 2)
        return -result

    def get_image(self):
        return self.image

    def getpixel(self, xy):
        x = xy[0]
        y = xy[1]
        if xy[0] >= self.width:
            x = self.width - 1
        if xy[1] >= self.height:
            y = self.height - 1
        return self.image.getpixel((x, y))

    def putpixel(self, xy, pixel):
        self.image.putpixel(xy, pixel)

    def convert(self, mode):
        image_copy = self
        image_copy.image = image_copy.image.convert(mode)
        return image_copy


image = PyImage.open(sys.argv[1])
image.show()
image.resize(200,200, 0).show()
image.resize(200,200, 1).show()