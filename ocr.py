
from PIL import Image,ImageOps
import pyocr
import pyocr.builders
from io import BytesIO
import pyperclip

def ocr(binary_data):

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    #print("Using '%s'" % (tools[0].get_name()))

    img = Image.open(BytesIO(binary_data))

    # 画像から日本語文字を読み取る
    text = tools[0].image_to_string(
        img,
        lang="jpn",                                             # 日本語を設定
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)  # 結果をテキストとして受け取る
    )
    print(text+'\n')
    pyperclip.copy(text)