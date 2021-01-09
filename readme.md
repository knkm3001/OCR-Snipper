# OCR Snipper
スクリーンショットを取る感覚でOCRを行えるGUIツール。一般的なQRコードにも対応。    
OCR実行後はクリップボードにテキストを保存する。  
OCRエンジンにはGoogle Cloud VisionとTesseractを選択可能。  
![output-palette](https://user-images.githubusercontent.com/54818379/104105916-0e945780-52f5-11eb-8bb9-c3a4c34bd296.gif)

## 動作環境
- win10 64bit(他の環境では動作未確認)
- python 3.7以上
- Google Cloud VisionのAPIキーを取得済み
- Tesseractがインストール済み

## 選択可能なOCRエンジン
- Google Cloud Vision
- Tesseract

## 環境構築
1. OCRエンジンの準備 
    - Tesseractのダウンロード及びパスの追加  [こちらを参考に](https://qiita.com/henjiganai/items/7a5e871f652b32b41a18)  
    - Google Cloud VisionのAPIキーを取得 [こちらを参考に](https://cloud.google.com/vision/docs/ocr?hl=ja)   
    APIキーは`env.py`に記入する  
1. レポジトリ クローン
    ```
    $ git clone https://github.com/knkm3001/OCR-Snipper.git
    $ cd OCR-Snipper
    ```
1.  pythonのライブラリの準備
    ```
    $ pip install PyQt5 pyocr pyperclip requests pyzbar
    ```
1. 実行
    ```
    $ python src/ocr-snipper.py
    ```


## exe化(任意)
頻繁に使うようならばexe化などしてデスクトップにショートカットを置くと便利。  

これでexe化
```
$ pyinstaller --noconsole -y  ./src/ocr-snipper.py
```


## 参考
- [Python3 PyQt5でスクリーンキャプチャを作ろう^ω^](https://qiita.com/pto8913/items/0241b11edda260012e44)  
- [Qt official](https://www.qt.io/)  
- [Google Cloud Vision](https://cloud.google.com/vision/docs/ocr?hl=ja)
- [PythonとTesseract OCRで文字認識](https://qiita.com/henjiganai/items/7a5e871f652b32b41a18)

## TODO
- 現在はスクショ対象はメインモニターのみなので、複数画面に対応させる
