import sys
from ocr import ocr
from PyQt5.QtCore import Qt, QPoint, QRectF, QRect, QByteArray, QBuffer
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QScreen, QPainter, QPainterPath, QBrush, QColor, QGuiApplication

class Snip(QWidget):
    startPos = QPoint(0, 0)
    endPos = QPoint(0, 0)
    def __init__(self,args,gcp_eng,mainwindow_controller):
        super().__init__()

        self.args = args
        self.gcp_eng = gcp_eng

        screen = QApplication.primaryScreen()

        # TODO 複数スクリーンに対応
        # 関数screenShotのsnipScreen.copyあたりでID指定できればいけそう
        # screens = [screen for screen in QGuiApplication.screens()]

        self.snipScreen = screen.grabWindow(
          QApplication.desktop().winId()
        )

        mainwindow_controller.show() # 実態はMainWindowのself.show()


    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen) # 描画しない
        rectSize = QApplication.desktop().screenGeometry() # 切り抜く場所の大きさを決める
        painter.drawPixmap(rectSize,self.snipScreen) # snipScreenを描写
        painterPath = QPainterPath() 
        painterPath.addRect(QRectF(rectSize))
        painterPath.addRoundedRect(QRectF(self.startPos, self.endPos), 0, 0) # 範囲指定箇所を指定
        painter.setBrush(QBrush(QColor(0, 0, 0, 180)))
        painter.drawPath(painterPath)

    def mousePressEvent(self, event):
        self.startPos = event.pos()
    
    def mouseMoveEvent(self, event):
        self.endPos = event.pos()
        self.repaint()
    
    def mouseReleaseEvent(self, event):
        self.endPos = event.pos()
        self.capture()

    def capture(self):
        
        # 右下から左上に選択したときの処理
        if self.startPos.x() > self.endPos.x():
            self.startPos, self.endPos = self.endPos, self.startPos


        # QPixmap で選択座標をコピー
        pmap = self.snipScreen.copy(QRect(self.startPos, self.endPos))
        
        # QPixmap -> Qimage -> binary
        qimg = pmap.toImage()
        image_format = 'PNG'
        bits = QByteArray()
        buffer = QBuffer(bits)
        qimg.save(buffer, image_format)

        # OCR
        ocr(buffer.data(),self.args.debugmode,self.gcp_eng)

        self.close()


    def keyPressEvent(self, event):
        """ ESCボタンでキャプチャ終了 """
        if event.key() == Qt.Key_Escape:
            self.close()
