# OCR Snipper
スクリーンショットを取る感覚でOCRを行えるGUIツール  
OCR実行後はクリップボードにテキストを保存する  
OCRエンジンにはTesseractとGoogle Cloud Visionを選択可能  
TesseractとGoogle Cloud Visionのラッパーツールみたいなかんじ  
![output-palette](https://user-images.githubusercontent.com/54818379/89716566-01430c00-d9e9-11ea-8a4c-eb6d9f6d187e.gif)
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
1.  pythonの準備
    ```
    pip install PyQt5 pyocr pyperclip requests
    ```
1. 実行
    ```
    python main.py
    ```


## exe化(任意)
頻繁に使うようならばexe化などしてデスクトップにショートカットを置くと便利。  
pyファイルを実行してもOK

これでexe化
```
pyinstaller --noconsole -y  ocr-snipper.py
```


## 参考
- [Python3 PyQt5でスクリーンキャプチャを作ろう^ω^](https://qiita.com/pto8913/items/0241b11edda260012e44)  
- [Qt official](https://www.qt.io/)  
- [Google Cloud Vision](https://cloud.google.com/vision/docs/ocr?hl=ja)
- [PythonとTesseract OCRで文字認識](https://qiita.com/henjiganai/items/7a5e871f652b32b41a18)

## TODO
- 現在は必要最小限なので設定ボタンでいろいろカスタムできるようにする
