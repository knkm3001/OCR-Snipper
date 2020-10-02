import sys
from PyQt5.QtWidgets import *

from snip import Snip
from ocrChangeButton import OCRChangeButton

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
        self.ocrEngRadioButtonSetUp()

        snipButton = QPushButton("Snip",self)
        snipButton.setGeometry(25, 10, 100, 35)
        snipButton.clicked.connect(self.clickedStartButton)

        quitButton = QPushButton("Quit",self)
        quitButton.setGeometry(135, 10, 100, 35)
        quitButton.setStyleSheet("color:#ff0000;")
        quitButton.clicked.connect(self.clickedQuitButton)

        self.setGeometry(300,300,260,300) # x,y,幅,高さ
        self.setMinimumHeight(150)
        self.setMaximumHeight(150)
        self.setMinimumWidth(260)
        self.setMaximumWidth(260)
        self.setWindowTitle('OCR helper')
        self.show()

    def clickedStartButton(self):
        gcp_eng = self.ocrbutton_widget.getOcrEng()
        self.snip = Snip(args,gcp_eng)
        self.snip.showFullScreen()


    def clickedQuitButton(self):
        sys.exit(1)

    def ocrEngRadioButtonSetUp(self):
     self.ocrbutton_widget = OCRChangeButton()

     self.setCentralWidget(self.ocrbutton_widget) 

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec())