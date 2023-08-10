
# import os
# import sys
# import matplotlib.image as img
# import Speech_to_list_functions as sl
# import Text_to_image as ti
# from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QLabel,QDialog,QMessageBox
# from PyQt5 import uic
# import time

# class UI(QMainWindow):
#     def __init__(self):
#         super(UI, self).__init__()
#         uic.loadUi(r"ElpoGui.ui", self)
#         self.pushButton.clicked.connect(self.speechtoText)
#         # try:
           
#         self.show()
#         # except:    
#         #      self.errorMssg("Try pronounce your sentence once more")
#     def speechtoText(self):
#         try:
#             list_text = sl.speech('output.wav')
#             print(list_text)

#             # textImage = ti.imgDisplay(list_text)
#             # print(textImage)
#             # myimage=img.imread(textImage[0])
#             # self.widget.canvas.axes.clear()
#             # self.widget.canvas.axes.imshow(myimage,cmap='gray')
#             # self.widget.canvas.draw()
#             # self.lineEdit_2.setText(str(list_text[0]))
#             textImage = ti.imgDisplay(list_text)  # Assuming this function works as expected
#             for i in range(len(textImage)):
#                 myimage = img.imread(textImage[i])
#                 self.widget.canvas.axes.clear()
#                 self.widget.canvas.axes.imshow(myimage, cmap='gray')
#                 self.widget.canvas.draw()
#                 self.lineEdit_2.setText(str(list_text[i]))
#                 time.sleep(10)  # Wait for 10 seconds before displaying the next image


#         except Exception as e:
#              print("Try again")

#     def errorMssg(self, txt):
#             QMessageBox.critical(self, "Error", txt)                

# app = QApplication(sys.argv)
# UIWindow = UI()
# app.exec_()   


import os
import sys
import matplotlib.image as img
import Speech_to_list_functions as sl
import Text_to_image as ti
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QDialog, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"ElpoGui.ui", self)
        self.pushButton.clicked.connect(self.speechtoText)
        self.show()

    def speechtoText(self):
        try:
            self.list_text = sl.speech('output.wav')
            print(self.list_text)
            self.textImage = ti.imgDisplay(self.list_text)  # Assuming this function works as expected
            self.image_index = 0
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_image)
            self.timer.start(5000)  # Update the image every 10 seconds
        except Exception as e:
            print("Try again")

    def update_image(self):
        myimage = img.imread(self.textImage[self.image_index])
        self.widget.canvas.axes.clear()
        self.widget.canvas.axes.imshow(myimage, cmap='gray')
        self.widget.canvas.draw()
        self.lineEdit_2.setText(str(self.list_text[self.image_index]))
        self.image_index += 1
        if self.image_index >= len(self.textImage):
            self.timer.stop()

    def errorMssg(self, txt):
        QMessageBox.critical(self, "Error", txt)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
