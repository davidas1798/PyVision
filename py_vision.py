from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLabel, QWidget, QMdiArea, QMdiSubWindow, QMessageBox, QUndoStack
from Pyvision_ui import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PIL.ImageQt import ImageQt
import pyimage


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    window_count = 0

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("PyVision")
        
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.images = []    # images[x][0] -> Pyimage nº x, images[x][1] -> Qimage nº x
        self.action_Open.triggered.connect(self.open_action_handler)
        self.actionBinarizar_2.triggered.connect(self.binarizar_action_handler)
        self.actionCambiar_brillo_y_contraste_2.triggered.connect(self.brillo_contraste_action_handler)
        self.actionEcualizar.triggered.connect(self.ecualizar_action_handler)
        self.actionEspecificar_histograma.triggered.connect(self.especificar_histograma_action_handler)
        self.actionImagen_diferencia.triggered.connect(self.imagen_diferencia_action_handler)
        self.actionMapa_de_cambios.triggered.connect(self.mapa_cambios_action_handler)
        self.actionTransformaci_n_lineal_por_tramos.triggered.connect(self.transformacion_lineal_action_handler)
        self.actionHistograma.triggered.connect(self.histograma_action_handler)
        self.actionHistograma_acumulativo.triggered.connect(self.histograma_acumulativo_action_handler)
        self.actionResumen.triggered.connect(self.resumen_action_handler)
        self.actionCorrecci_n_gamma.triggered.connect(self.correccion_gamma_action_handler)
        self.action_Save.triggered.connect(self.guardar_action_handler)
        self.actionRotaci_n_m_ltiplo_de_90.triggered.connect(self.ninety_rotation_action_handler)
        self.actionEspejo_vertical.triggered.connect(self.vertical_flip_action_handler)
        self.actionEspejo_horizontal.triggered.connect(self.horizontal_flip_action_handler)
        self.actionTraspuesta.triggered.connect(self.transpose_action_handler)
        self.actionReescalar.triggered.connect(self.resize_action_handler)
        self.actionRotar.triggered.connect(self.rotation_action_handler)

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent: x=%d, y=%d' % (event.x(), event.y()))

    def open_action_handler(self):
        filename, trash = QFileDialog.getOpenFileName()
        self.open_image(filename)

    def binarizar_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage

        umbral = 10
        H = 255
        L = 0
        new_umbral, ok = QInputDialog.getInt(self, 'Binarizar imagen', 'Introducir umbral')
        if ok:
            umbral = new_umbral
        new_H, ok = QInputDialog.getInt(self, 'Binarizar imagen', 'Introducir valor alto')
        if ok:
            H = new_H
        new_L, ok = QInputDialog.getInt(self, 'Binarizar imagen', 'Introducir valor bajo')
        if ok:
            L = new_L

        new_image = window_image.binary(umbral, H, L)
        self.show_image(new_image)

    def brillo_contraste_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage

        brightness = window_image.get_brightness()
        contrast = window_image.get_contrast()
        new_brightness, ok = QInputDialog.getDouble(self, 'Cambiar brillo', 'Introducir brillo:')
        if ok:
            brightness = new_brightness
        new_contrast, ok = QInputDialog.getDouble(self, 'Cambiar contraste', 'Introducir contraste')
        if ok:
            contrast = new_contrast

        new_image = window.pyimage.set_brightness_contrast(brightness, contrast)
        self.show_image(new_image)

    def especificar_histograma_action_handler(self):
        filename, trash = QFileDialog.getOpenFileName()
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        reference_image = pyimage.PyImage.open(filename)
        result_image = window_image.histogram_specification(reference_image)

        self.show_image(result_image)

    def imagen_diferencia_action_handler(self):
        filename, trash = QFileDialog.getOpenFileName()
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        other_image = pyimage.PyImage.open(filename)
        result_image = window_image.difference(other_image)

        self.show_image(result_image)

    def mapa_cambios_action_handler(self):
        window = self.mdi.activeSubWindow()
        filename, trash = QFileDialog.getOpenFileName()
        umbral = 10
        new_umbral, ok = QInputDialog.getInt(self, 'Mapa de cambios', 'Introducir umbral de detección de cambios')
        if ok:
            umbral = new_umbral
        window_image = window.pyimage
        other_image = pyimage.PyImage.open(filename)
        result_image = window_image.difference_map(other_image, umbral)

        self.show_image(result_image)

    def transformacion_lineal_action_handler(self):
        window = self.mdi.activeSubWindow()
        tramos = 2
        new_tramos, ok = QInputDialog.getInt(self, 'Transformación lineal por tramos', 'Introducir nº de tramos')
        if ok:
            tramos = new_tramos
        coordinates = []
        for i in range(tramos):
            xi, ok = QInputDialog.getInt(self, 'Tramo ' + str(i+1), 'Xi')
            if ok:
                xf, ok = QInputDialog.getInt(self, 'Tramo ' + str(i+1), 'Xf')
                if ok:
                    yi, ok = QInputDialog.getInt(self, 'Tramo ' + str(i+1), 'Yi')
                    if ok:
                       yf, ok = QInputDialog.getInt(self, 'Tramo ' + str(i+1), 'Yf') 
                       if ok:
                           coordinates.append(xi)
                           coordinates.append(xf)
                           coordinates.append(yi)
                           coordinates.append(yf)


        window_image = window.pyimage
        result_image = window_image.linear_transformation(coordinates)

        self.show_image(result_image)

    def ecualizar_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        new_image = window_image.equalize()
        self.show_image(new_image)

    def histograma_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        pg.plot(window_image.histogram)

    def histograma_acumulativo_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        pg.plot(window_image.c_histogram)

    def correccion_gamma_action_handler(self):
        gamma = 1
        new_gamma, ok = QInputDialog.getDouble(self, 'Corrección gamma', 'Introducir gamma:')
        if ok:
            gamma = new_gamma
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        new_image = window_image.gamma_correction(gamma)
        self.show_image(new_image)

    def resumen_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        resumen = QMessageBox()
        resumen.setWindowTitle("Resumen")
        resumen.setText("Tamaño: " + str(window_image.width) + "x" + str(window_image.height) + "\nBrillo: " + str(window_image.brightness) + "\nContraste: " + str(window_image.contrast))
        resumen.setInformativeText("Max: " + str(window_image.max_gray()) + "\nMin: " + str(window_image.min_gray()))
        resumen.setIcon(QMessageBox.Information)

        x = resumen.exec_()

    def vertical_flip_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        new_image = window_image.vertical_flip()
        self.show_image(new_image)
        
    def horizontal_flip_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        new_image = window_image.horizontal_flip()
        self.show_image(new_image)

    def transpose_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        new_image = window_image.transpose()
        self.show_image(new_image)

    def ninety_rotation_action_handler(self):
        window = self.mdi.activeSubWindow()

        directions = ("Izquierda", "Derecha")
        direction = "Izquierda"
        angles = ("90º", "180º", "270º")
        angle = "90º"

        new_angle, ok = QInputDialog.getItem(self, 'Rotación múltiplo de 90º', 'Seleccione el ángulo en el que rotará la imagen', angles, 0, False)
        if ok:
            angle = new_angle
        
        new_direction, ok = QInputDialog.getItem(self, 'Rotación múltiplo de 90º', 'Seleccione la dirección en la que rotará la imagen', directions, 0, False)
        if ok:
            direction = new_direction
        
        if angle == "90º":
            times = 1
        elif angle == "180º":
            times = 2
        else:
            times = 3
        
        mode = direction == "Izquierda"
        window_image = window.pyimage
        new_image = window_image.ninety_rotation(times, mode)
        self.show_image(new_image)

    def resize_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        methods = ("Vecino más próximo", "Bilineal")
        
        size_x, ok = QInputDialog.getInt(self, 'Reescalar imagen', 'Introducir nuevo ancho de imagen:')
        if ok:
            size_y, ok = QInputDialog.getInt(self, 'Reescalar imagen', 'Introducir nuevo alto de imagen:')
            if ok:
                method, ok = QInputDialog.getItem(self, 'Reescalar imagen', 'Seleccione el método de interpolación', methods, 0, False)
                if ok:
                    mode = method == "Bilineal"
                    new_image = window_image.resize(size_x, size_y, mode)
                    self.show_image(new_image)

    def rotation_action_handler(self):
        window = self.mdi.activeSubWindow()
        window_image = window.pyimage
        directions = ("Izquierda", "Derecha")
        methods = ("Vecino más próximo", "Bilineal")
        
        direction_str, ok = QInputDialog.getItem(self, 'Rotar imagen', 'Introducir dirección de rotación:', directions, 0, False)
        if ok:
            alpha, ok = QInputDialog.getDouble(self, 'Rotar imagen', 'Introducir ángulo de rotación:')
            if ok:
                method, ok = QInputDialog.getItem(self, 'Rotar imagen', 'Seleccione el método de interpolación', methods, 0, False)
                if ok:
                    mode = method == "Bilineal"
                    direction = direction_str == "Izquierda"
                    new_image = window_image.rotation(alpha, direction, mode)
                    self.show_image(new_image)


    def open_image(self, filename):
        image = pyimage.PyImage.open(filename)
        self.show_image(image)

    def guardar_action_handler(self):
        filename, ok = QInputDialog.getText(self, 'Guardar imagen', 'Introducir nombre de fichero') 

    def show_image(self, image):
        qimage = ImageQt(image.image)
        self.images.append((image, qimage))

        pix = QtGui.QPixmap.fromImage(qimage)

        label = QLabel()
        label.setPixmap(pix)

        MainWindow.window_count += 1
        sub_window = QMdiSubWindow()
        sub_window.pyimage = image
        sub_window.setWidget(label)
        
        sub_window.setWindowTitle("Image " + str(MainWindow.window_count))
        sub_window.resize(pix.width(), pix.height())
        label.setScaledContents(True)

        self.mdi.addSubWindow(sub_window)
        sub_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
