# OCR Snipper
スクリーンショットを取る感覚でOCRを行えるGUIツール  
TesseractとGoogle Cloud Visionのラッパーツールとしての存在

## 動作環境
- win10
- python 3.7以上
- Tesseractがインストール済み
- Google Cloud VisionのAPIキーを取得済み


## OCRエンジン
- Tesseract
- Google Cloud Vision

## 環境構築

- Tesseractのダウンロード及びパスの追加  

- pythonの準備

    ```
    pip install PyQt5 pyocr pyperclip
    ※他にもあったが...また今度詳しく書く
    ```


## exe化
これでexe化 (onefileにすると遅くなる)
```
pyinstaller main.py
```


## 参考
・[Python3 PyQt5でスクリーンキャプチャを作ろう^ω^](https://qiita.com/pto8913/items/0241b11edda260012e44)  
・[Qt official](https://www.qt.io/)  
