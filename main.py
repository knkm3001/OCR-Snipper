import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QSizePolicy

from snip import Snip

from argparse import ArgumentParser


argparser = ArgumentParser()
argparser.add_argument('-d', '--debugmode',
                    action='store_true',
                    default=False,
                    help='is debugmode on')
args = argparser.parse_args()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        snipButton = QPushButton("Snip",self)
        snipButton.setGeometry(10, 10, 60, 35)
        snipButton.clicked.connect(self.clickedStartButton)

        fileButton = QPushButton("File",self)
        fileButton.setGeometry(80, 10, 60, 35)

        settingButton = QPushButton("Setting",self)
        settingButton.setGeometry(150, 10, 60, 35)

        quitButton = QPushButton("Quit",self)
        quitButton.setGeometry(220, 10, 60, 35)
        quitButton.setStyleSheet("color:#ff0000;")
        quitButton.clicked.connect(self.clickedQuitButton)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('OCR helper')
        self.show()

        
    
    def clickedStartButton(self):

        

        self.snip = Snip(args)
        self.snip.showFullScreen()

    def clickedQuitButton(self):
        sys.exit(1)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec())