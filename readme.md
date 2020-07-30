# OCR Snipper
スクリーンショットを取る感覚でOCRを行えるGUIツール

## 動作環境
- win10
- python 3.7以上
- Tesseractがインストールされておりパスが入ってること


## OCRエンジン
- Tesseract
- Google Cloud Vision(今後対応)

## 環境構築

- Tesseractのダウンロード及びパスの追加  

- pythonの準備

    ```
    pip install PyQt5 pyocr pyperclip
    ※他にもあったが...
    ```


## exe化
これでexe化 (onefileにすると遅くなる)
```
pyinstaller main.py
```


## 参考
・[Python3 PyQt5でスクリーンキャプチャを作ろう^ω^](https://qiita.com/pto8913/items/0241b11edda260012e44)  
・[Qt official](https://www.qt.io/)  