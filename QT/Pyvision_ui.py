# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyVision.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgba(226, 225, 255, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuImage = QtWidgets.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMouseTracking(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.action_Close_all = QtWidgets.QAction(MainWindow)
        self.action_Close_all.setObjectName("action_Close_all")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Save_as = QtWidgets.QAction(MainWindow)
        self.action_Save_as.setObjectName("action_Save_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCambiar_brillo_y_contraste = QtWidgets.QAction(MainWindow)
        self.actionCambiar_brillo_y_contraste.setObjectName("actionCambiar_brillo_y_contraste")
        self.actionBinarizar = QtWidgets.QAction(MainWindow)
        self.actionBinarizar.setObjectName("actionBinarizar")
        self.actionBinarizar_2 = QtWidgets.QAction(MainWindow)
        self.actionBinarizar_2.setObjectName("actionBinarizar_2")
        self.actionCambiar_brillo_y_contraste_2 = QtWidgets.QAction(MainWindow)
        self.actionCambiar_brillo_y_contraste_2.setObjectName("actionCambiar_brillo_y_contraste_2")
        self.actionEspecificar_histograma = QtWidgets.QAction(MainWindow)
        self.actionEspecificar_histograma.setObjectName("actionEspecificar_histograma")
        self.actionImagen_diferencia = QtWidgets.QAction(MainWindow)
        self.actionImagen_diferencia.setObjectName("actionImagen_diferencia")
        self.actionMapa_de_cambios = QtWidgets.QAction(MainWindow)
        self.actionMapa_de_cambios.setObjectName("actionMapa_de_cambios")
        self.actionTransformaci_n_lineal_por_tramos = QtWidgets.QAction(MainWindow)
        self.actionTransformaci_n_lineal_por_tramos.setObjectName("actionTransformaci_n_lineal_por_tramos")
        self.actionEcualizar = QtWidgets.QAction(MainWindow)
        self.actionEcualizar.setObjectName("actionEcualizar")
        self.actionResumen = QtWidgets.QAction(MainWindow)
        self.actionResumen.setObjectName("actionResumen")
        self.actionHistograma = QtWidgets.QAction(MainWindow)
        self.actionHistograma.setObjectName("actionHistograma")
        self.actionHistograma_acumulativo = QtWidgets.QAction(MainWindow)
        self.actionHistograma_acumulativo.setObjectName("actionHistograma_acumulativo")
        self.actionCorrecci_n_gamma = QtWidgets.QAction(MainWindow)
        self.actionCorrecci_n_gamma.setObjectName("actionCorrecci_n_gamma")
        self.actionEspejo_vertical = QtWidgets.QAction(MainWindow)
        self.actionEspejo_vertical.setObjectName("actionEspejo_vertical")
        self.actionEspejo_horizontal = QtWidgets.QAction(MainWindow)
        self.actionEspejo_horizontal.setObjectName("actionEspejo_horizontal")
        self.actionTraspuesta = QtWidgets.QAction(MainWindow)
        self.actionTraspuesta.setObjectName("actionTraspuesta")
        self.actionRotaci_n_m_ltiplo_de_90 = QtWidgets.QAction(MainWindow)
        self.actionRotaci_n_m_ltiplo_de_90.setObjectName("actionRotaci_n_m_ltiplo_de_90")
        self.actionReescalar = QtWidgets.QAction(MainWindow)
        self.actionReescalar.setObjectName("actionReescalar")
        self.actionRotar = QtWidgets.QAction(MainWindow)
        self.actionRotar.setObjectName("actionRotar")
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Close)
        self.menuFile.addAction(self.action_Close_all)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_Save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuImage.addAction(self.actionHistograma)
        self.menuImage.addAction(self.actionHistograma_acumulativo)
        self.menuImage.addAction(self.actionResumen)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionBinarizar_2)
        self.menuImage.addAction(self.actionCambiar_brillo_y_contraste_2)
        self.menuImage.addAction(self.actionCorrecci_n_gamma)
        self.menuImage.addAction(self.actionEcualizar)
        self.menuImage.addAction(self.actionEspecificar_histograma)
        self.menuImage.addAction(self.actionImagen_diferencia)
        self.menuImage.addAction(self.actionMapa_de_cambios)
        self.menuImage.addAction(self.actionTransformaci_n_lineal_por_tramos)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionEspejo_vertical)
        self.menuImage.addAction(self.actionEspejo_horizontal)
        self.menuImage.addAction(self.actionTraspuesta)
        self.menuImage.addAction(self.actionRotaci_n_m_ltiplo_de_90)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionReescalar)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionRotar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuImage.setTitle(_translate("MainWindow", "Image"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Close.setText(_translate("MainWindow", "&Close"))
        self.action_Close_all.setText(_translate("MainWindow", "Close all"))
        self.action_Save.setText(_translate("MainWindow", "&Save "))
        self.action_Save_as.setText(_translate("MainWindow", "&Save as"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCambiar_brillo_y_contraste.setText(_translate("MainWindow", "Cambiar brillo y contraste "))
        self.actionBinarizar.setText(_translate("MainWindow", "Binarizar"))
        self.actionBinarizar_2.setText(_translate("MainWindow", "Binarizar"))
        self.actionCambiar_brillo_y_contraste_2.setText(_translate("MainWindow", "Cambiar brillo y contraste"))
        self.actionEspecificar_histograma.setText(_translate("MainWindow", "Especificar histograma"))
        self.actionImagen_diferencia.setText(_translate("MainWindow", "Imagen diferencia"))
        self.actionMapa_de_cambios.setText(_translate("MainWindow", "Mapa de cambios"))
        self.actionTransformaci_n_lineal_por_tramos.setText(_translate("MainWindow", "Transformación lineal por tramos"))
        self.actionEcualizar.setText(_translate("MainWindow", "Ecualizar"))
        self.actionResumen.setText(_translate("MainWindow", "Resumen"))
        self.actionHistograma.setText(_translate("MainWindow", "Histograma"))
        self.actionHistograma_acumulativo.setText(_translate("MainWindow", "Histograma acumulativo"))
        self.actionCorrecci_n_gamma.setText(_translate("MainWindow", "Corrección gamma"))
        self.actionEspejo_vertical.setText(_translate("MainWindow", "Espejo vertical"))
        self.actionEspejo_horizontal.setText(_translate("MainWindow", "Espejo horizontal"))
        self.actionTraspuesta.setText(_translate("MainWindow", "Traspuesta"))
        self.actionRotaci_n_m_ltiplo_de_90.setText(_translate("MainWindow", "Rotación múltiplo de 90º"))
        self.actionReescalar.setText(_translate("MainWindow", "Reescalar"))
        self.actionRotar.setText(_translate("MainWindow", "Rotar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

