from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLabel, QWidget, QMdiArea, QMdiSubWindow, QMessageBox
from Pyvision_ui import *
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
        self.actionCambiar_brillo_y_contraste_2.triggered.connect(self.brillo_contraste_action_handler)
        self.actionEspecificar_histograma.triggered.connect(self.especificar_histograma_action_handler)
        self.actionImagen_diferencia.triggered.connect(self.imagen_diferencia_action_handler)
        self.actionMapa_de_cambios.triggered.connect(self.mapa_cambios_action_handler)
        self.actionTransformaci_n_lineal_por_tramos.triggered.connect(self.transformacion_lineal_action_handler)

    def open_action_handler(self):
        filename, trash = QFileDialog.getOpenFileName()
        self.open_image(filename)

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
        filename, trash = QFileDialog.getOpenFileName()
        umbral = 10
        new_umbral, ok = QInputDialog.getInt(self, 'Mapa de cambios', 'Introducir umbral de detección de cambios')
        if ok:
            umbral = new_umbral
        window = self.mdi.activeSubWindow()
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


    def open_image(self, filename):
        image = pyimage.PyImage.open(filename)
        self.show_image(image)

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
        # menubar = QtWidgets.QMenuBar()
        # transformButton = menubar.addMenu("Transform")
        # transformButton.addAction("Grayscale")
        sub_window.resize(pix.width(), pix.height())
        
        label.setScaledContents(True)

        self.mdi.addSubWindow(sub_window)
        sub_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
