from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLabel, QWidget, QMdiArea, QMdiSubWindow
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

    def open_action_handler(self):
        filename, trash = QFileDialog.getOpenFileName()
        self.open_image(filename)

    def brilloContraste_action_handler(self):
        popup = QMessageBox()
        popup.setWindowTitle("Cambiar brillo y contraste")
        popup.setStandarButton(QMessageBox.Ok|QMessageBox.Cancel)
        
        x = popup.exec_()
    
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
