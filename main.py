
import os
import sys
import matplotlib.image as img
import Speech_to_list_functions as sl
import Text_to_image as ti
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QLabel,QDialog,QMessageBox
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"ElpoGui.ui", self)
        self.pushButton.clicked.connect(self.speechtoText)
        # try:
           
        self.show()
        # except:    
        #      self.errorMssg("Try pronounce your sentence once more")
    def speechtoText(self):
        list_text = sl.speech('output.wav')
        print(list_text)

        textImage = ti.imgDisplay(list_text)
        print(textImage)
        myimage=img.imread(textImage[0])
        self.widget.canvas.axes.clear()
        self.widget.canvas.axes.imshow(myimage,cmap='gray')
        self.widget.canvas.draw()
        self.lineEdit_2.setText(str(list_text[0]))
    def errorMssg(self, txt):
            QMessageBox.critical(self, "Error", txt)                

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()   
