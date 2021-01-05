import sys
from ocr import ocr
from PyQt5.QtCore import Qt, QPoint, QRectF, QRect, QByteArray, QBuffer
from PyQt5.QtWidgets import QWidget, QButtonGroup, QRadioButton, QLabel, QVBoxLayout,QPushButton


class OCRChangeButton(QWidget):
    def __init__(self):
        super().__init__()

        self.ocreng_dict = {'Tesseract':'tesseract','Google Cloud Vision':'gcv'}

        self.ocrEng = 'tesseract'

        self.initUI()

    def initUI(self):

        self.setGeometry(0,30,260,50) # x,y,幅,高さ
        self.setWindowTitle('OCR helper - seting')

        self.ocrEngRadioButtonSetUp()

        self.show()

    def ocrEngRadioButtonSetUp(self):

        ocr_eng_rb1 = QRadioButton("Google Cloud Vision")
        ocr_eng_rb1.toggled.connect(self.updateLabel)
        ocr_eng_rb1.setChecked(True) 


        ocr_eng_rb2 = QRadioButton("Tesseract")
        ocr_eng_rb2.toggled.connect(self.updateLabel)
        
        label = QLabel("Select OCR Engine")
        
        Vlayout = QVBoxLayout()

        Vlayout.addWidget(label)
        Vlayout.addWidget(ocr_eng_rb1)
        Vlayout.addWidget(ocr_eng_rb2)

        self.setLayout(Vlayout)

    def updateLabel(self, value):

        rbtn = self.sender()

        if rbtn.isChecked() == True:
            self.ocrEng = self.ocreng_dict[rbtn.text()]

    def getOcrEng(self):
        return self.ocrEng