from AmicaUi import Ui_AMICA
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
import os
import MainAmica
import webbrowser as web
from PyQt5.uic import loadUiType
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        MainAmica.Task_Gui()

startExe=MainThread()

class Gui_Start(QMainWindow):
    def __init(self):
        super().__init__()

        self.gui=Ui_AMICA()
        self.gui.setupUi(self)
        self.gui.QtWidgets.pushButton_start.clicked.connect(self.startTask)
        self.gui.QtWidgets.pushButton_exit.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1=QtGui.QMovie("D:\\GUIMaterial\\b2.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("D:\\GUIMaterial\\VoiceLogo.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("D:\\GUIMaterial\\b4.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        startExe.start()
        timer = QTimer(self)
        timer.timeout().connect(self.showTimeLive)
        timer.start(999)


    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time:" + time
        label_date = "Date:" + date

        self.txt_Time.setText(label_time)
        self.txt_Date.setText(label_date)

if __name__ == "__main__":
    import sys
    GuiApp = QtWidgets.QApplication(sys.argv)
    AMICA = QtWidgets.QMainWindow()
    amica_gui=Gui_Start()
    amica_gui.show()
    sys.exit(GuiApp.exec_())
