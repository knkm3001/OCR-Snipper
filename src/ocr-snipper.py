import sys
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
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
        
        self.ocr_eng_dict = {'Tesseract':'tesseract','Google Cloud Vision':'gcv'}
        self.ocr_eng = 'gcv' # 初期値
        self.window_width = 260
        self.window_height = 180
        self.is_cut_newline = False
        self.initUI()
    
    def initUI(self):

        # Snip,Quite
        snipButton = QPushButton("Snip",self)
        snipButton.clicked.connect(self.clickedSnipButton)
        quitButton = QPushButton("Quit",self)
        quitButton.setStyleSheet("color:#ff0000;")
        quitButton.clicked.connect(self.clickedQuitButton)
        snipButton.setGeometry(25, 10, 100, 35) # x,y,幅,高さ
        quitButton.setGeometry(135, 10, 100, 35)

        # OCRエンジン指定
        ocr_eng_label = QLabel("Select OCR Engine",self)
        ocr_eng_rb1 = QRadioButton("Google Cloud Vision",self)
        ocr_eng_rb1.toggled.connect(self.updateLabel)
        ocr_eng_rb1.setChecked(True) # GCVがデフォルト
        ocr_eng_rb2 = QRadioButton("Tesseract",self)
        ocr_eng_rb2.toggled.connect(self.updateLabel)

        ocr_eng_label.setGeometry(25,50,200,20)
        ocr_eng_rb1.setGeometry(30,70,200,20)
        ocr_eng_rb2.setGeometry(30,90,200,20)

        # 改行をカットするか
        cut_newline_chb = QCheckBox("Cut Newline",self)
        cut_newline_chb.stateChanged.connect(self.updateCutNewline)
        cut_newline_chb.setGeometry(25,120,100,20)


        self.resize(self.window_width,self.window_height)
        self.setMinimumHeight(self.window_height)
        self.setMaximumHeight(self.window_height)
        self.setMinimumWidth(self.window_width)
        self.setMaximumWidth(self.window_width)
        self.setWindowTitle('OCR helper')
        self.show()

    def clickedSnipButton(self):
        self.hide() # main windowを隠す
        sleep(0.2)
        self.snip = Snip(args,self)
        self.snip.showFullScreen()

    def clickedQuitButton(self):
        sys.exit(1)

    def updateLabel(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.ocr_eng = self.ocr_eng_dict[rbtn.text()]

    def updateCutNewline(self,state):
        self.is_cut_newline = True if QtCore.Qt.Checked == state else False
        print(self.is_cut_newline )

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec())