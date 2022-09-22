from ctypes.wintypes import MSG
from email import message
import os
from distutils import extension
from fileinput import filename
from importlib.resources import path
from os import listdir
import shutil
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox, QPushButton
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):#classe 

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Organizer")

        self.file = ''

        self.btn_open.clicked.connect(self.open_path)
        self.btn_organize.clicked.connect(self.organizer)

    def open_path(self):
        
        self.file = QFileDialog.getExistingDirectory(self, str("pasta xml"),
                                                '/home',
                                                QFileDialog.ShowDirsOnly |
                                                QFileDialog.DontResolveSymlinks)

        self.txt_path.setText(self.file)
        self.file = str(self.file) 

    def organizer(self):
        
        path = self.file
        files = listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos Organizados com sucesso!")
        msg.exec_()



if __name__  == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
